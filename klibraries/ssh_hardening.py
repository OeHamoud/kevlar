import os

def apply():
    print("SSH hardening")

    config = """
PasswordAuthentication no
PermitRootLogin no
ChallengeResponseAuthentication no
UsePAM yes
MaxAuthTries 3
"""

    os.system('echo "{}" | sudo tee -a /etc/ssh/sshd_config'.format(config.strip()))
    os.system("sudo systemctl restart ssh")