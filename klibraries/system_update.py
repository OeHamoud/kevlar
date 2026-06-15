#This is for full system update and cleanup
#It is an important step before starting hardening

import os
def update():
    os.system("sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y && sudo apt clean")
    print("\033[92m✔\033[0m Full system update Done")