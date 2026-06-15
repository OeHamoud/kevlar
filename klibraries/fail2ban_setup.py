import os

def install():
    print("Installing Fail2Ban")

    os.system("sudo apt update -y")
    os.system("sudo apt install -y fail2ban")

    print("Creating custom SSH jail config")

    config = """[sshd]
enabled = true
backend = systemd
port = ssh
maxretry = 3
findtime = 10m
bantime = 1h
ignoreip = 127.0.0.1/8
"""

    with open("/tmp/sshd.local", "w") as f:
        f.write(config)
        
    os.system("sudo mv /tmp/sshd.local /etc/fail2ban/jail.d/sshd.local")

    print("Enabling service")
    os.system("sudo systemctl enable fail2ban")
    os.system("sudo systemctl restart fail2ban")

    print("Status")
    os.system("sudo fail2ban-client status sshd")

    print("\033[92m✔\033[0m Fail2Ban Setup")