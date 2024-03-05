import subprocess

def security_hardening():
    # Update package lists
    subprocess.run(['sudo', 'apt', 'update'])

    # Upgrade installed packages
    subprocess.run(['sudo', 'apt', 'upgrade', '-y'])

    # Enable firewall (ufw)
    subprocess.run(['sudo', 'ufw', 'enable'])

    # Allow SSH connections
    subprocess.run(['sudo', 'ufw', 'allow', 'OpenSSH'])

    # Enable automatic security updates
    subprocess.run(['sudo', 'apt', 'install', '-y', 'unattended-upgrades'])
    subprocess.run(['sudo', 'dpkg-reconfigure', 'unattended-upgrades'])

    # Disable root SSH login
    with open('/etc/ssh/sshd_config', 'a') as ssh_config:
        ssh_config.write("\nPermitRootLogin no\n")

    # Set up password policy (complexity, expiration, etc.)
    subprocess.run(['sudo', 'apt', 'install', '-y', 'libpam-pwquality'])
    with open('/etc/pam.d/common-password', 'a') as pam_config:
        pam_config.write("\npassword requisite pam_pwquality.so retry=3\n")
        pam_config.write("password requisite pam_unix.so sha512 shadow use_authtok\n")
        pam_config.write("password required pam_deny.so\n")

    # Restrict access to sensitive files and directories
    subprocess.run(['sudo', 'chmod', '600', '/etc/shadow'])
    subprocess.run(['sudo', 'chmod', '600', '/etc/gshadow'])
    subprocess.run(['sudo', 'chmod', '644', '/etc/passwd'])
    subprocess.run(['sudo', 'chmod', '644', '/etc/group'])
    subprocess.run(['sudo', 'chmod', '700', '/etc/ssh'])

    print("Security hardening tasks completed successfully.")

if __name__ == "__main__":
    security_hardening()
