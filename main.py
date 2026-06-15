from ui.banner import welcome
from ui.multiselect import multiselect
from klibraries import apparmor_enforce, auditd_setup, permissions_hardening, security_probe as sp, service_pruning, ssh_hardening, sysctl_hardening, time_sync
from klibraries import system_update
from klibraries import selinux_setup
from klibraries import ufw_setup
from klibraries import unnecessary_packages
from klibraries import ssh_allowlist
from klibraries import fail2ban_setup
from klibraries import automatic_updates

#Kevlar banner
welcome()

#option menu
chosen =multiselect(
    [
        "Full System Update & autoremove",
        "Remove Unnecessary Packages",

        "SELinux Setup",
        "AppArmor Enforce",

        "Default UFW Setup",
        "Webserver UFW Setup",

        "SSH Hardening",
        "SSH Allow List",

        "Fail2Ban Setup",
        "Automatic system updates",

        "Kernel Hardening (sysctl)",
        "Auditd Setup",
        "Service Pruning",
        "Time Sync Hardening",
        "Permissions Hardening",
    ],
    groups=[[4, 5], [2,3]]
)

if "Full System Update & autoremove" in chosen:
    system_update.update()

if "Remove Unnecessary Packages" in chosen:
    unnecessary_packages.remove()

if "SELinux Setup" in chosen:
    selinux_setup.install()

if "AppArmor Enforce" in chosen:
    apparmor_enforce.enable()

if "Default UFW Setup" in chosen:
    ufw_setup.default_install()

if "Webserver UFW Setup" in chosen:
    ufw_setup.webserver_install()

if "SSH Hardening" in chosen:
    ssh_hardening.apply()

if "SSH Allow List" in chosen:
    ssh_allowlist.implement()

if "Fail2Ban Setup" in chosen:
    fail2ban_setup.install()

if "Automatic system updates" in chosen:
    automatic_updates.install()

if "Kernel Hardening (sysctl)" in chosen:
    sysctl_hardening.apply()

if "Auditd Setup" in chosen:
    auditd_setup.install()

if "Service Pruning" in chosen:
    service_pruning.apply()

if "Time Sync Hardening" in chosen:
    time_sync.apply()

if "Permissions Hardening" in chosen:
    permissions_hardening.apply()