import subprocess

def check_service_status(services):
    for service in services:
        result = subprocess.run(['systemctl', 'status', service], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print(f"{service} is running.")
        else:
            print(f"{service} is not running.")

if __name__ == "__main__":
    services = ["ssh", "httpd", "nginx"]
    check_service_status(services)
