import os

def install():
    print("Installing auditd")
    os.system("sudo apt update -y")
    os.system("sudo apt install -y auditd audispd-plugins")
    os.system("sudo systemctl enable --now auditd")