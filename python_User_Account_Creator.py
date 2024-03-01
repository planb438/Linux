import subprocess

def create_user(username, password):
    subprocess.run(['useradd', '-m', username])
    subprocess.run(['passwd', '--stdin', username], input=password.encode())

if __name__ == "__main__":
    username = "newuser"
    password = "password"
    create_user(username, password)
