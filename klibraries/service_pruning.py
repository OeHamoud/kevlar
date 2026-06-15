import os

def apply():
    print("Disabling Unused Services")

    services = [
        "cups",
        "avahi-daemon",
        "bluetooth"
    ]

    for s in services:
        os.system(f"sudo systemctl disable --now {s} || true")
        print("\033[92m✔\033[0m Removed Unused Services")