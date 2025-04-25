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
#############################################################################################3
#How to Use
#Here's how to mount and use the NFS share on client machines.

#🧰 On the NFS Server (just for reference)You’ve already created and shared the directory:
#/srv/nfs/kubedata *(rw,sync,no_subtree_check,no_root_squash).This means any client can mount it with read/write access.

#🖥️ On the NFS Client (e.g., your Kubernetes nodes or another Ubuntu machine)
#1. 🔧 Install NFS client tools

#sudo apt update
#sudo apt install -y nfs-common
#2. 🔍 Discover available NFS shares (optional)

#showmount -e <NFS_SERVER_IP>
#Example:
#showmount -e 10.0.0.231
#3. 📁 Create a mount point

#sudo mkdir -p /mnt/nfs/kubedata
#4. 🔗 Mount the NFS share

#sudo mount <NFS_SERVER_IP>:/srv/nfs/kubedata /mnt/nfs/kubedata
#Example:

#sudo mount 10.0.0.231:/srv/nfs/kubedata /mnt/nfs/kubedata
#You can now use /mnt/nfs/kubedata just like any local folder.

#5. 🔁 (Optional) Add it to /etc/fstab for auto-mount at boot
#Add the following line:

#10.0.0.231:/srv/nfs/kubedata /mnt/nfs/kubedata nfs defaults 0 0
#Then reload fstab or reboot:
#sudo mount -a
###########################################################################
