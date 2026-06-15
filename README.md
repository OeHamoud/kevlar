# [kevlar 🪖]()


[![SELinux](https://img.shields.io/badge/SELinux-5A5A5A?style=for-the-badge)](#)
[![AppArmor](https://img.shields.io/badge/AppArmor-2E86C1?style=for-the-badge)](#)
[![UFW](https://img.shields.io/badge/UFW-Firewall-E74C3C?style=for-the-badge)](#)
[![Fail2Ban](https://img.shields.io/badge/Fail2Ban-Bruteforce%20Protection-8E44AD?style=for-the-badge)](#)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=fff)](#)
[![Debian](https://img.shields.io/badge/Debian-A81D33?style=for-the-badge&logo=debian&logoColor=white)](#)

Linux Security Automation Toolkit for Debian-based systems.

Kevlar automates system hardening, firewall configuration, intrusion protection, and system maintenance in a modular Python framework.


## ⚙️ Installation

```bash
git clone https://github.com/yourname/kevlar.git
cd kevlar
```
## ▶️ Usage

Run the main interface:
```
sudo python3 main.py
```
Controls:

- space → select
- enter → confirm
- q → quit

## 🔐 Security Modules
**Firewall**
- UFW default deny incoming
- Optional webserver profile (80/443)
- SSH rate limiting

**Intrusion Protection**
- Fail2Ban SSH jail
- Brute-force mitigation

**System Hardening**
- sysctl kernel protections
- SSH lockdown
- file permission tightening

**Audit & Monitoring**
- auditd logging
- system service pruning

**Time Security**
- chrony NTP synchronization

## 🧩 Project Structure
```
kevlar
├── klibraries
│   ├── apparmor_enforce.py
│   ├── auditd_setup.py
│   ├── automatic_updates.py
│   ├── fail2ban_setup.py
│   ├── __init__.py
│   ├── permissions_hardening.py
│   ├── restart.py
│   ├── security_probe.py
│   ├── selinux_setup.py
│   ├── service_pruning.py
│   ├── ssh_allowlist.py
│   ├── ssh_hardening.py
│   ├── sysctl_hardening.py
│   ├── system_update.py
│   ├── time_sync.py
│   ├── ufw_setup.py
│   └── unnecessary_packages.py
├── main.py
├── README.md
└── ui
    ├── banner.py
    └── multiselect.py

3 directories, 21 files
```
## 📌 Goal
When setting up a server I allways get bored with the long installs so I automated it.

Yes that's that

anyways look at this funny picture that i found when researching about this project

![image alt](https://github.com/OeHamoud/kevlar/blob/main/meme_01.png)

