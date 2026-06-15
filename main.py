import os
import shutil
from ui.banner import welcome
from ui.multiselect import multiselect
from klibraries import security_probe as sp
from klibraries import system_update

#Kevlar banner
welcome()

#option menu
chosen =multiselect(
    ["Option A", "Option B", "Option C"],
    preselected=[0],    # indices to pre-check
)

print(chosen)  # ['Option A', 'Option C']


#server update & upgrade
system_update.update()


#UFW setup
print("Installing UFW")
os.system("sudo apt-get install ufw")

#Optionnal for debain based Distros install SELinux

if sp.is_apparmor_active():
    print("AppArmor active")
else:
    print("no")