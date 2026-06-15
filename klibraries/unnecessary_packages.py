import os

def remove():
    print("removing unnecessary packages")
    os.system("sudo apt purge telnet rsh-client rsh-redone-client talk ntalk")

    print("cleaning up")
    os.system("sudo apt autoremove --purge")
    print("\033[92m✔\033[0m Removed unnecessary Packages")
