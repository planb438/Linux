import paramiko

def ssh_connect(hostname, port, username, password):
    try:
        # Create SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the SSH server
        client.connect(hostname, port=port, username=username, password=password)

        print("SSH connection established successfully.")

        # Execute commands (optional)
        stdin, stdout, stderr = client.exec_command("ls -l")
        for line in stdout:
            print(line.strip())

        # Close the connection
        client.close()
    except paramiko.AuthenticationException:
        print("Authentication failed.")
    except paramiko.SSHException as e:
        print(f"SSH connection failed: {e}")

if __name__ == "__main__":
    # Provide SSH server details
    hostname = "example.com"
    port = 22
    username = "username"
    password = "password"

    # Establish SSH connection
    ssh_connect(hostname, port, username, password)
