import os

def apply():
    print("Permissions Hardening")

    os.system("sudo chmod 600 /etc/shadow")
    os.system("sudo chmod 644 /etc/passwd")
    os.system("sudo chmod 600 /etc/ssh/sshd_config")
    print("\033[92m✔\033[0m  Permissions Hardening Done")