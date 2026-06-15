import os


def default_install():
    print("updating")
    os.system("sudo apt update -y")

    print("installing ufw")
    os.system("sudo apt install -y ufw")

    print("configuring ufw")

    os.system("sudo ufw default deny incoming")
    os.system("sudo ufw default allow outgoing")

    print("limiting ssh port to reduce brute-force")
    os.system("sudo ufw limit 22/tcp")

    print("enabling ufw")
    os.system("sudo ufw enable")

    print("status")
    os.system("sudo ufw status verbose")

    print("\033[92m✔\033[0m Ufw Setup")

def webserver_install():

    print("custom install")

    print("updating")
    os.system("sudo apt update -y")

    print("installing ufw")
    os.system("sudo apt install -y ufw")

    print("configuring ufw")

    os.system("sudo ufw default deny incoming")
    os.system("sudo ufw default allow outgoing")

    print("limiting ssh port to reduce brute-force")
    os.system("sudo ufw limit 22/tcp")

    print("Webserver config")
    os.system("ufw allow 80/tcp")
    os.system("ufw allow 443/tcp")

    print("enabling ufw")
    os.system("sudo ufw enable")

    print("status")
    os.system("sudo ufw status verbose")