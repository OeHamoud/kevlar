import os

def install():
    print("installing unattended upgrades")
    os.system("sudo apt update -y")
    os.system("sudo apt install -y unattended-upgrades apt-listchanges")

    print("enabling automatic updates")
    os.system("sudo dpkg-reconfigure -f noninteractive unattended-upgrades")

    print("writing config")

    config = """APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Unattended-Upgrade "1";
"""

    with open("/tmp/20auto-upgrades", "w") as f:
        f.write(config)

    os.system("sudo mv /tmp/20auto-upgrades /etc/apt/apt.conf.d/20auto-upgrades")

    print("status check")
    os.system("systemctl status unattended-upgrades --no-pager")
    print("\033[92m✔\033[0m Automatic Updates")