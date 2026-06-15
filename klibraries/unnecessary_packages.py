import os

def remove():
    print("removing unnecessary packages")
    os.system("apt purge telnet rsh-client rsh-redone-client talk ntalk")

    print("cleaning up")
    os.system("apt autoremove --purge")
