import subprocess

def check_connectivity(hosts):
    for host in hosts:
        result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print(f"{host} is reachable.")
        else:
            print(f"{host} is unreachable.")

if __name__ == "__main__":
    hosts = ["example.com", "google.com", "localhost"]
    check_connectivity(hosts)
