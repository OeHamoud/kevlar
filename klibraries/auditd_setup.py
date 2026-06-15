import os

def install():
    print("Installing Auditd")
    os.system("sudo apt update -y")
    os.system("sudo apt install -y auditd audispd-plugins")
    os.system("sudo systemctl enable --now auditd")
    print("\033[92m✔\033[0m Auditd Setup")