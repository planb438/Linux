#!/usr/bin/env python3

import subprocess

def run_command(command, shell=True):
    print(f"Running: {command}")
    result = subprocess.run(command, shell=shell, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error:\n{result.stderr}")
    else:
        print(result.stdout)

def setup_nfs_server():
    print("🛠️  Installing NFS server packages...")
    run_command("sudo apt update && sudo apt install -y nfs-kernel-server")

    print("📁 Creating shared directory...")
    run_command("sudo mkdir -p /srv/nfs/kubedata")
    run_command("sudo chown nobody:nogroup /srv/nfs/kubedata")

    print("📝 Configuring /etc/exports...")
    export_entry = "/srv/nfs/kubedata *(rw,sync,no_subtree_check,no_root_squash)\n"
    with open("/tmp/exports", "w") as f:
        f.write(export_entry)
    run_command("sudo tee -a /etc/exports < /tmp/exports")

    print("📡 Exporting file system and starting NFS server...")
    run_command("sudo exportfs -rav")
    run_command("sudo systemctl enable nfs-server")
    run_command("sudo systemctl restart nfs-server")

    print("✅ NFS Server setup complete!")

if __name__ == "__main__":
    setup_nfs_server()
