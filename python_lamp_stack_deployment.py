import subprocess

def install_lamp_stack():
    # Update package lists
    subprocess.run(['sudo', 'apt', 'update'])

    # Install Apache
    subprocess.run(['sudo', 'apt', 'install', '-y', 'apache2'])

    # Install MySQL (MariaDB)
    subprocess.run(['sudo', 'apt', 'install', '-y', 'mysql-server', 'mysql-client'])

    # Install PHP and modules
    subprocess.run(['sudo', 'apt', 'install', '-y', 'php', 'libapache2-mod-php', 'php-mysql'])

    # Restart Apache
    subprocess.run(['sudo', 'systemctl', 'restart', 'apache2'])

    print("LAMP stack installation completed successfully.")

if __name__ == "__main__":
    install_lamp_stack()
