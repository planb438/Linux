import subprocess

def check_firewall_configuration():
    try:
        # Run iptables command to list rules
        output = subprocess.check_output(['iptables', '-L', '-n'], stderr=subprocess.STDOUT)
        print("Firewall configuration:\n", output.decode())
    except subprocess.CalledProcessError as e:
        print("Error:", e.output.decode())

if __name__ == "__main__":
    check_firewall_configuration()
