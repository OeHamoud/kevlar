import os
import shutil

def apply():
    print("Time Synchronization Hardening")

    if shutil.which("chronyd") is None:
        os.system("sudo apt update")
        os.system("sudo apt install -y chrony")

    os.system("sudo chronyc makestep")
    os.system("sudo systemctl enable --now chrony")
    os.system("chronyc tracking")
    print("\033[92m✔\033[0m Time Sync")