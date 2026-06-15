from ui.banner import welcome
from ui.multiselect import multiselect
from klibraries import security_probe as sp
from klibraries import system_update
from klibraries import selinux_setup
from klibraries import ufw_setup
from klibraries import unnecessary_packages
from klibraries import automatic_updates

#Kevlar banner
welcome()

#option menu
chosen =multiselect(
    [
     "Full System Update & autoremove",
     "Remove Unnecessary Packages",
     "SELinux Setup",
     "Default ufw setup",
     "Webserver ufw setup",
     "Automatic system updates",
     ],
    preselected=[0],    # indices to pre-check
)

#server update & autoremove
if "Full System Update & autoremove" in chosen:
    system_update.update()

#Remove Unnecessary Packages
if "Remove Unnecessary Packages" in chosen:
    unnecessary_packages.remove()

#automatic system updates
if "Automatic system updates" in chosen:
    automatic_updates.install()

#SELinux setup
if "SELinux Setup" in chosen:
    selinux_setup.install()

#UFW setup
if "Default ufw setup" in chosen:
    ufw_setup.default_install()

if "Webserver ufw setup" in chosen:
    ufw_setup.webserver_install()

