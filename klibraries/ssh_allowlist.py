import os

def implement():
    print("SSH allowlist configuration")

    ips = input("Enter allowed IPs/hosts (comma separated): ")

    allowed = [x.strip() for x in ips.split(",") if x.strip()]

    deny_rule = "sshd: ALL\n"
    allow_rules = "\n".join([f"sshd: {ip}" for ip in allowed]) + "\n"

    print("Writing /etc/hosts.deny")
    os.system(f'echo "{deny_rule}" | sudo tee /etc/hosts.deny')

    print("Writing /etc/hosts.allow")
    os.system(f'echo "{allow_rules}" | sudo tee /etc/hosts.allow')

    print("Done")