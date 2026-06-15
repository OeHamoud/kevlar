import os

def apply():
    print("Disabling unused services")

    services = [
        "cups",
        "avahi-daemon",
        "bluetooth"
    ]

    for s in services:
        os.system(f"sudo systemctl disable --now {s} || true")