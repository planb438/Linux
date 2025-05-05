import subprocess
import os

def disable_swap_now():
    print("[*] Turning off swap...")
    subprocess.run(["sudo", "swapoff", "-a"], check=True)
    print("[+] Swap is now off for the current session.")

def disable_swap_permanently():
    fstab_path = "/etc/fstab"
    backup_path = "/etc/fstab.bak"

    print("[*] Backing up /etc/fstab to /etc/fstab.bak...")
    subprocess.run(["sudo", "cp", fstab_path, backup_path], check=True)

    print("[*] Disabling swap in /etc/fstab...")
    with open(fstab_path, "r") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        if "swap" in line and not line.strip().startswith("#"):
            new_lines.append("# " + line)  # Comment out the swap line
        else:
            new_lines.append(line)

    with open("/tmp/fstab_new", "w") as f:
        f.writelines(new_lines)

    subprocess.run(["sudo", "cp", "/tmp/fstab_new", fstab_path], check=True)
    print("[+] Swap has been disabled permanently in /etc/fstab.")

if __name__ == "__main__":
    disable_swap_now()
    disable_swap_permanently()
