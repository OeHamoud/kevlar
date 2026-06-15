from klibraries import security_probe as sp
import os

RED = "\033[91m"
RESET = "\033[0m"

def install():
    print("Installing SELinux")

    os.system("sudo apt update")

    os.system("sudo apt install -y \
        selinux-basics \
        selinux-policy-default \
        policycoreutils \
        policycoreutils-python-utils \
        checkpolicy \
        semodule-utils \
        auditd")

    print("Disabling AppArmor...")

    os.system("systemctl disable --now apparmor || true")

    print("Activating SELinux")

    print("selinux-activate")

    if sp.is_apparmor_active():
        print(f"{RED}Error:{RESET} AppArmor still active")
    else:
        print("CHECK: AppArmor disabled")

    if sp.is_selinux_installed():
        print("Check: SELinux installed")
    else:
        print(f"{RED}Error:{RESET} SElinux not installed")

    if sp.is_selinux_enforcing():
        print("Check: SELinux enforced")
    else:
        print(f"{RED}Error:{RESET} SELinux not enforced")