import os

def install():
    print("installing unattended upgrades")
    os.system("sudo apt update -y")
    os.system("sudo apt install -y unattended-upgrades apt-listchanges")
    
    print("enabling automatic updates")
    os.system("sudo dpkg-reconfigure -f noninteractive unattended-upgrades")
    
    print("writing config")
    os.system('echo \'APT::Periodic::Update-Package-Lists "1";\' | sudo tee /etc/apt/apt.conf.d/20auto-upgrades')
    os.system('echo \'APT::Periodic::Unattended-Upgrade "1";\' | sudo tee -a /etc/apt/apt.conf.d/20auto-upgrades')
    
    print("status check")
    os.system("systemctl status unattended-upgrades --no-pager")