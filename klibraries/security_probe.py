import os
import shutil

def is_apparmor_active():
    return os.system("sudo systemctl is-active --quiet apparmor") == 0

def is_selinux_installed():
    return shutil.which("sudo sestatus") is not None

def is_selinux_enforcing():
    if not is_selinux_installed():
        return False
    return os.system("sudo sestatus 2>/dev/null | grep -q 'enabled'") == 0