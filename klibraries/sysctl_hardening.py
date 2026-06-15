import os

def apply():
    print("Kernel hardening")

    config = """
net.ipv4.ip_forward=0
net.ipv4.conf.all.accept_redirects=0
net.ipv4.conf.all.send_redirects=0
net.ipv4.conf.all.accept_source_route=0
kernel.kptr_restrict=2
kernel.dmesg_restrict=1
fs.protected_hardlinks=1
fs.protected_symlinks=1
"""

    os.system('echo "{}" | sudo tee /etc/sysctl.d/99-hardening.conf'.format(config.strip()))
    os.system("sudo sysctl -p /etc/sysctl.d/99-hardening.conf")