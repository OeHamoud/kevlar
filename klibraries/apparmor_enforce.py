import os

def enable():
    print("Enforcing AppArmor")
    os.system("sudo systemctl enable apparmor")
    os.system("sudo systemctl restart apparmor")
    os.system("sudo aa-enforce /etc/apparmor.d/*")
    print("\033[92m✔\033[0m AppArmor Enforcement")