import os

def apply():
    print("Permissions hardening")

    os.system("sudo chmod 600 /etc/shadow")
    os.system("sudo chmod 644 /etc/passwd")
    os.system("sudo chmod 600 /etc/ssh/sshd_config")