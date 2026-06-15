import os

def apply():
    print("Time synchronization hardening")

    os.system("sudo systemctl enable --now systemd-timesyncd")