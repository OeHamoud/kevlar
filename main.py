import os
import shutil
from ui.banner import welcome
from ui.multiselect import multiselect
from klibraries import security_probe as sp
from klibraries import system_update
from klibraries import selinux_setup
from klibraries import ufw_setup

#Kevlar banner
welcome()

#option menu
chosen =multiselect(
    ["Full System Update & autoremove", "SELinux Setup", "Default ufw setup", "Webserver ufw setup"],
    preselected=[0],    # indices to pre-check
)

# test
#server update & autoremove
if "Full System Update & autoremove" in chosen:
    system_update.update()

#SELinux setup
if "SELinux Setup" in chosen:
    selinux_setup.install()

#UFW setup
if "Default ufw setup" in chosen:
    ufw_setup.default_install()

if "Webserver ufw setup" in chosen:
    ufw_setup.webserver_install()
