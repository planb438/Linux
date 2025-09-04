#!/usr/bin/env python3
"""
CloudKanata MicroK8s Bootstrap Script
Enhanced version with better error handling, idempotency, and security features
"""

import os
import sys
import subprocess
import argparse
import logging
import time
from pathlib import Path
import shutil

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("/var/log/cloudkanata-bootstrap.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def run_command(cmd, check=True, capture_output=True, retries=1, delay=5):
    """Run a shell command with retries and better error handling"""
    for attempt in range(retries + 1):
        try:
            logger.info(f"Running: {cmd}")
            result = subprocess.run(
                cmd, 
                shell=True, 
                check=check, 
                capture_output=capture_output, 
                text=True,
                executable='/bin/bash'
            )
            if capture_output and result.stdout:
                logger.debug(f"Command output: {result.stdout}")
            return result
        except subprocess.CalledProcessError as e:
            logger.warning(f"Command failed (attempt {attempt + 1}/{retries + 1}): {cmd}")
            if attempt < retries:
                logger.info(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                logger.error(f"Command failed after {retries + 1} attempts: {e}")
                if check:
                    sys.exit(1)
                return e

def check_installed(tool):
    """Check if a tool is already installed"""
    return shutil.which(tool) is not None

def install_microk8s(channel="1.28/stable"):
    """Install MicroK8s with idempotency check"""
    if check_installed("microk8s"):
        logger.info("MicroK8s is already installed")
        return
    
    logger.info("Installing MicroK8s...")
    
    # Install snap if not present
    if not check_installed("snap"):
        run_command("apt-get update && apt-get install -y snapd")
        # Wait for snap to be available
        time.sleep(10)
    
    # Install MicroK8s
    run_command(f"sudo snap install microk8s --classic --channel={channel}")
    
    # Wait for MicroK8s to be ready with timeout
    logger.info("Waiting for MicroK8s to be ready...")
    for i in range(30):  # Wait up to 5 minutes
        result = run_command("sudo microk8s status", check=False)
        if result.returncode == 0:
            break
        logger.info(f"Waiting for MicroK8s to start... ({i+1}/30)")
        time.sleep(10)
    else:
        logger.error("MicroK8s failed to start within expected time")
        sys.exit(1)
    
    logger.info("MicroK8s installed successfully")

def enable_addons(addons=None):
    """Enable MicroK8s addons with idempotency"""
    if addons is None:
        addons = ["dns", "storage", "dashboard", "registry", "metrics-server", "rbac"]
    
    logger.info("Enabling MicroK8s addons...")
    
    # Check which addons are already enabled
    result = run_command("sudo microk8s status --format short", capture_output=True)
    enabled_addons = []
    if result.returncode == 0:
        for line in result.stdout.split('\n'):
            if 'enabled' in line:
                addon_name = line.split()[0].strip(':')
                enabled_addons.append(addon_name)
    
    for addon in addons:
        if addon in enabled_addons:
            logger.info(f"{addon} is already enabled")
            continue
            
        logger.info(f"Enabling {addon}...")
        run_command(f"sudo microk8s enable {addon}", retries=3)
        time.sleep(5)  # Brief pause between addons
    
    logger.info("Addons enabled successfully")

def setup_kubectl():
    """Set up kubectl configuration with proper permissions"""
    logger.info("Setting up kubectl...")
    
    # Create .kube directory
    home = str(Path.home())
    kube_dir = f"{home}/.kube"
    os.makedirs(kube_dir, exist_ok=True)
    
    # Add current user to microk8s group for sudo-less access
    run_command("sudo usermod -a -G microk8s $USER")
    run_command("sudo chown -f -R $USER ~/.kube")
    run_command("newgrp microk8s")

        # Get kubeconfig with proper permissions
    run_command("sudo microk8s kubectl config view --raw > /tmp/kubeconfig.yaml")
    run_command(f"sudo mv /tmp/kubeconfig.yaml {kube_dir}/config")
    run_command(f"sudo chown $(id -u):$(id -g) {kube_dir}/config")
    run_command(f"chmod 600 {kube_dir}/config")
    
    # Add alias to bashrc if not already present
    bashrc = f"{home}/.bashrc"
    alias_line = "alias kubectl='microk8s kubectl'"
    
    with open(bashrc, 'r+') as f:
        content = f.read()
        if alias_line not in content:
            f.write(f"\n# Kubernetes aliases\n{alias_line}\n")
            logger.info("Added kubectl alias to .bashrc")
    
    logger.info("kubectl setup completed")

def install_helm():
    """Install Helm with version check"""
    if check_installed("helm"):
        logger.info("Helm is already installed")
        return
        
    logger.info("Installing Helm...")
    
    run_command("curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3")
    run_command("chmod 700 get_helm.sh")
    run_command("./get_helm.sh")
    run_command("rm get_helm.sh")
    
    logger.info("Helm installed successfully")

def security_hardening():
    """Apply security hardening measures"""
    logger.info("Applying security hardening...")
    
    # Disable swap permanently
    run_command("sudo swapoff -a")
    if os.path.exists("/etc/fstab"):
        run_command("sudo sed -i '/ swap / s/^/#/' /etc/fstab")
    
    # Configure kernel parameters
    kernel_params = {
        "net.ipv4.ip_forward": "1",
        "net.bridge.bridge-nf-call-iptables": "1",
        "net.bridge.bridge-nf-call-ip6tables": "1",
        "fs.inotify.max_user_watches": "524288",
        "vm.overcommit_memory": "1",
        "vm.panic_on_oom": "0"
    }
    
    sysctl_conf = []
    for param, value in kernel_params.items():
        run_command(f"sudo sysctl -w {param}={value}")
        sysctl_conf.append(f"{param}={value}")
    
    # Write to sysctl.conf
    with open("/tmp/99-kubernetes.conf", "w") as f:
        f.write("\n".join(sysctl_conf) + "\n")
    
    run_command("sudo mv /tmp/99-kubernetes.conf /etc/sysctl.d/99-kubernetes.conf")
    
    # Configure firewall
    run_command("sudo ufw allow 22/tcp", check=False)  # SSH
    run_command("sudo ufw allow 80/tcp", check=False)  # HTTP
    run_command("sudo ufw allow 443/tcp", check=False) # HTTPS
    run_command("sudo ufw allow 6443/tcp", check=False) # Kubernetes API
    run_command("sudo ufw allow 10250/tcp", check=False) # Kubelet API
    run_command("sudo ufw --force enable", check=False)
    
    # Configure container runtime security
    run_command("sudo apt-get install -y apparmor apparmor-utils", check=False)
    
    logger.info("Security hardening completed")

def setup_cloudkanata_apps():
    """Setup CloudKanata applications with idempotency"""
    logger.info("Setting up CloudKanata applications...")
    
    # Add Helm repositories
    repos = {
        "argo": "https://argoproj.github.io/argo-helm",
        "prometheus-community": "https://prometheus-community.github.io/helm-charts",
        "grafana": "https://grafana.github.io/helm-charts",
        "jetstack": "https://charts.jetstack.io"  # cert-manager
    }
    
    for name, url in repos.items():
        result = run_command(f"helm repo list | grep {name}", check=False)
        if result.returncode != 0:
            run_command(f"helm repo add {name} {url}")
        else:
            logger.info(f"Helm repo {name} already exists")
    
    run_command("helm repo update")
    
    logger.info("CloudKanata apps setup completed")

def create_example_manifests():
    """Create example deployment manifests for testing"""
    logger.info("Creating example manifests...")
    
    manifests_dir = os.path.expanduser("~/cloudkanata-manifests")
    os.makedirs(manifests_dir, exist_ok=True)
    
    # Create namespace
    with open(f"{manifests_dir}/namespace.yaml", "w") as f:
        f.write("""apiVersion: v1
kind: Namespace
metadata:
  name: cloudkanata
  labels:
    name: cloudkanata
""")
    
    # Create test deployment
    with open(f"{manifests_dir}/test-deployment.yaml", "w") as f:
        f.write("""apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-test
  namespace: cloudkanata
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
        ports:
        - containerPort: 80
        resources:
          requests:
            memory: "64Mi"
            cpu: "50m"
          limits:
            memory: "128Mi"
            cpu: "100m"
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
  namespace: cloudkanata
spec:
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
""")
    
    logger.info(f"Example manifests created in {manifests_dir}")

def verify_installation():
    """Verify the installation was successful"""
    logger.info("Verifying installation...")
    
    # Check MicroK8s status
    run_command("sudo microk8s status")
    
    # Check nodes
    run_command("sudo microk8s kubectl get nodes")
    
    # Check pods in all namespaces
    run_command("sudo microk8s kubectl get pods -A")
    
    logger.info("Verification completed successfully")

def main():
    parser = argparse.ArgumentParser(description="Bootstrap MicroK8s cluster for CloudKanata")
    parser.add_argument("--channel", default="1.28/stable", help="MicroK8s channel")
    parser.add_argument("--addons", nargs="+", 
                        default=["dns", "storage", "dashboard", "registry", "metrics-server", "rbac"],
                        help="MicroK8s addons to enable")
    parser.add_argument("--skip-hardening", action="store_true", help="Skip security hardening")
    parser.add_argument("--skip-verification", action="store_true", help="Skip final verification")
    
    args = parser.parse_args()
    
    logger.info("Starting CloudKanata MicroK8s bootstrap...")
    
    try:
        # Check if running as root
        if os.geteuid() == 0:
            logger.warning("Running as root is not recommended. Consider running as a regular user.")
        
        install_microk8s(args.channel)
        enable_addons(args.addons)
        setup_kubectl()
        install_helm()
        
        if not args.skip_hardening:
            security_hardening()
        
        setup_cloudkanata_apps()
        create_example_manifests()
        
        if not args.skip_verification:
            verify_installation()
        
        logger.info("✅ Bootstrap completed successfully!")
        logger.info("\nNext steps:")
        logger.info("1. Log out and back in for group changes to take effect")
        logger.info("2. Run: kubectl get nodes")
        logger.info("3. Run: kubectl get pods -A")
        logger.info("4. Deploy applications from ~/cloudkanata-manifests/")
        logger.info("5. Access dashboard: kubectl proxy --port=8080 --address='0.0.0.0' --accept-hosts='.*'")
        
    except Exception as e:
        logger.error(f"Bootstrap failed: {e}")
        logger.exception("Detailed error traceback:")
        sys.exit(1)

if __name__ == "__main__":
    main()
