import os
import subprocess
import argparse

def check_ssh_root_login():
    result = subprocess.getoutput("grep -i '^PermitRootLogin' /etc/ssh/ssh_config || echo 'PermitRootLogin not found'")
    return result.strip()

def check_ssh_protocol():
    result = subprocess.getoutput("grep -i '^Protocol' /etc/ssh/ssh_config || echo 'Protocol not set'")
    return result.strip()

def check_password_auth():
    result = subprocess.getoutput("grep -i '^PasswordAuthentication' /etc/ssh/ssh_config || echo 'PasswordAuthentication not found'")
    return result.strip()

def check_firewall():
    result = subprocess.getoutput("ufw status || echo 'UFW not installed'")
    return result.strip()

def check_password_policy():
    result = subprocess.getoutput("grep -E 'PASS_MAX_DAYS|PASS_MIN_DAYS' /etc/login.defs")
    return result.strip()

def check_unused_filesystems():
    fs_list = ["cramfs", "squashfs", "udf"]
    disabled = []
    for fs in fs_list:
        status = subprocess.getoutput(f"lsmod | grep {fs}")
        if not status:
            disabled.append(fs)
    return disabled

def check_autoupdate():
    result = subprocess.getoutput("grep -i 'Unattended-Upgrade' /etc/apt/apt.conf.d/* || echo 'Unattended-Upgrade not set'")
    return result.strip()

def check_ntp_status():
    if os.path.exists("/usr/sbin/ntpd"):
        return "NTP installed"
    elif os.path.exists("/usr/sbin/chronyd"):
        return "Chrony installed"
    else:
        return "No time sync service found"

def check_ipv6_status():
    result = subprocess.getoutput("sysctl net.ipv6.conf.all.disable_ipv6")
    return result.strip()

def check_root_path_integrity():
    path = os.environ["PATH"].split(":")
    issues = [p for p in path if p in [".", ""] or not os.path.isdir(p)]
    return issues if issues else "PATH integrity good"

def check_passwd_shadow_permissions():
    passwd = subprocess.getoutput("stat -c '%a %n' /etc/passwd")
    shadow = subprocess.getoutput("stat -c '%a %n' /etc/shadow")
    return passwd, shadow

def audit():
    print("[+] Auditing Ubuntu system:")
    print(f" - SSH Root Login: {check_ssh_root_login()}")
    print(f" - SSH Protocol: {check_ssh_protocol()}")
    print(f" - Password Authentication: {check_password_auth()}")
    print(f" - Firewall Status: {check_firewall()}")
    print(f" - Password Policy: {check_password_policy()}")
    print(f" - Unused Filesystems: {check_unused_filesystems()}")
    print(f" - Auto Updates: {check_autoupdate()}")
    print(f" - Time Sync Service: {check_ntp_status()}")
    print(f" - IPv6 Status: {check_ipv6_status()}")
    print(f" - Root PATH Integrity: {check_root_path_integrity()}")
    passwd, shadow = check_passwd_shadow_permissions()
    print(f" - /etc/passwd perms: {passwd}")
    print(f" - /etc/shadow perms: {shadow}")
    print("[!] Run this command with harden to fix steps .")
def harden():
    print("[+] Hardening system (manual approval for now)...")
    # Placeholder for hardening functions
    # Examples:
    # subprocess.run(["ufw", "enable"])
    # subprocess.run(["sed", "-i", "s/^#PermitRootLogin.*/PermitRootLogin no/", "/etc/ssh/ssh_config"])
    print("[!] Hardening steps would go here — skipped by request.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ubuntu CIS Auditor Tool")
    parser.add_argument("--harden", action="store_true", help="Apply CIS-based hardening")
    args = parser.parse_args()

    audit()
    if args.harden:
        harden()
