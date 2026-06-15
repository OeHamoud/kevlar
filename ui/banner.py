COLOR_CYAN  = "\033[96m"
COLOR_GRAY  = "\033[2m"
RESET       = "\033[0m"


BANNER = """
    ██╗  ██╗███████╗██╗   ██╗██╗      █████╗ ██████╗ 
    ██║ ██╔╝██╔════╝██║   ██║██║     ██╔══██╗██╔══██╗
    █████╔╝ █████╗  ██║   ██║██║     ███████║██████╔╝
    ██╔═██╗ ██╔══╝  ╚██╗ ██╔╝██║     ██╔══██║██╔══██╗
    ██║  ██╗███████╗ ╚████╔╝ ███████╗██║  ██║██║  ██║
    ╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
"""
SUBTITLE = "  Linux system hardening toolkit  ·  harden fast, stay secure"

def welcome():
    print(COLOR_CYAN + BANNER + RESET)
    print(COLOR_GRAY + SUBTITLE + RESET + "\n")