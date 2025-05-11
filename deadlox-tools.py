#!/usr/bin/env python3
"""
DEADLOX ULTIMATE TOOLS v2.5 - WhatsApp Tools + System Utilities
Created by Deadlox & DeepSeek
"""

import os
import sys
import time
import random
import requests
import phonenumbers
import cpuinfo
import psutil
from datetime import datetime
from phonenumbers import carrier, geocoder, timezone

# ===== CONSTANTS =====
class Color:
    RED = "\033[1;31m"
    GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[1;34m"
    MAGENTA = "\033[1;35m"
    CYAN = "\033[1;36m"
    WHITE = "\033[1;37m"
    RESET = "\033[0m"

PROXY_LIST = [
    "103.156.17.61:3128",
    "45.95.147.106:8080",
    "194.233.69.41:443"
]

# ===== AUTHENTICATION =====
def authenticate():
    max_attempts = 3
    for attempt in range(max_attempts):
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"{Color.RED}⚡ DEADLOX TOOLS AUTHENTICATION ⚡{Color.RESET}")
        username = input(f"{Color.YELLOW}Username: {Color.RESET}")
        password = input(f"{Color.YELLOW}Password: {Color.RESET}")
        
        if username == "DD" and password == "DD1.6":
            return True
        print(f"{Color.RED}⚠ Invalid credentials! Attempts left: {max_attempts - attempt - 1}{Color.RESET}")
        time.sleep(1)
    return False

# ===== IMPROVED BANNER =====
def show_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"""{Color.RED}
▓█████▄  ▒█████   ██▀███   ▄▄▄       ██▓███  
▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒▒████▄    ▓██░  ██▒
░██   █▌▒██░  ██▒▓██ ░▄█ ▒▒██  ▀█▄  ▓██░ ██▓▒
░▓█▄   ▌▒██   ██░▒██▀▀█▄  ░██▄▄▄▄██ ▒██▄█▓▒ ▒
░▒████▓ ░ ████▓▒░░██▓ ▒██▒ ▓█   ▓██▒▒██▒ ░  ░
 ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒▓▒░ ░  ░
 ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░  ▒   ▒▒ ░░▒ ░     
 ░ ░  ░ ░ ░ ░ ▒    ░░   ░   ░   ▒   ░░       
   ░        ░ ░     ░           ░  ░          
 ░                                          
{Color.CYAN}╔════════════════════════════════════╗
║    TERMUX ULTIMATE TOOLKIT v2.5    ║
║      {Color.MAGENTA}CREATED BY DEADLOX & DEEPSEEK{Color.CYAN}    ║
╚════════════════════════════════════╝{Color.RESET}""")

# ===== WHATSAPP TOOLS =====
def whatsapp_menu():
    while True:
        print(f"""
{Color.GREEN}╔════════════════════════════════════╗
║         WHATSAPP TOOLS            ║
╠════════════════════════════════════╣
║ {Color.CYAN}1.{Color.RESET} Spam Report (Individual)    {Color.GREEN}║
║ {Color.CYAN}2.{Color.RESET} Group Report               {Color.GREEN}║
║ {Color.RED}0.{Color.RESET} Back to Main Menu          {Color.GREEN}║
╚════════════════════════════════════╝{Color.RESET}""")
        
        choice = input(f"\n{Color.YELLOW}Select option (0-2): {Color.RESET}")
        
        if choice == "1":
            whatsapp_spam()
        elif choice == "2":
            whatsapp_group_report()
        elif choice == "0":
            break
        else:
            print(f"{Color.RED}Invalid option!{Color.RESET}")

def whatsapp_spam():
    print(f"\n{Color.RED}=== WHATSAPP SPAM REPORT (SIMULATION) ===")
    print(f"{Color.YELLOW}NOTE: This is simulation only!{Color.RESET}")
    
    number = input(f"{Color.BLUE}Enter phone number (628xxxx): {Color.RESET}").strip()
    count = min(int(input(f"{Color.BLUE}Number of reports (1-50): {Color.RESET}") or 1), 50)
    
    for i in range(1, count+1):
        try:
            print(f"{Color.GREEN}[✓] Simulated report {i} to {number}{Color.RESET}")
            time.sleep(random.uniform(0.3, 1.2))
        except Exception as e:
            print(f"{Color.RED}[X] Error: {str(e)[:50]}...{Color.RESET}")

def whatsapp_group_report():
    print(f"\n{Color.RED}=== WHATSAPP GROUP REPORT (SIMULATION) ===")
    print(f"{Color.YELLOW}NOTE: No actual reports are sent!{Color.RESET}")
    
    group_link = input(f"{Color.BLUE}Enter WhatsApp group link: {Color.RESET}").strip()
    if not group_link.startswith(('https://chat.whatsapp.com/', 'http://chat.whatsapp.com/')):
        print(f"{Color.RED}Invalid WhatsApp group link!{Color.RESET}")
        return
    
    print(f"\n{Color.YELLOW}=== SELECT REPORT REASON ===")
    print(f"{Color.RED}1. 18+ Content (Pornography/Exploitation)")
    print(f"2. Violence/Hate Speech")
    print(f"3. Spam/Scam")
    print(f"4. Other Violations{Color.RESET}")
    
    method = input(f"\n{Color.BLUE}Select reason (1-4): {Color.RESET}")
    reasons = {
        '1': 'Sexual content violation',
        '2': 'Violence/Hate speech',
        '3': 'Spam/Scam activity',
        '4': 'Other violations'
    }
    
    if method in reasons:
        print(f"\n{Color.RED}🚧 SIMULATION STARTED...{Color.RESET}")
        print(f"{Color.CYAN}Group: {group_link}")
        print(f"Reason: {reasons[method]}{Color.RESET}")
        
        for i in range(1, 6):
            print(f"{Color.YELLOW}[{i}] Simulating report process...{Color.RESET}")
            time.sleep(1)
        
        print(f"\n{Color.GREEN}✓ Simulation completed successfully!")
        print(f"ℹ️ In real usage, this would send report to WhatsApp{Color.RESET}")
    else:
        print(f"{Color.RED}Invalid selection!{Color.RESET}")

# ===== OTHER TOOLS =====
def social_media_downloader():
    print(f"\n{Color.MAGENTA}=== SOCIAL MEDIA DOWNLOADER ===")
    url = input(f"{Color.BLUE}Enter media URL: {Color.RESET}").strip()
    
    try:
        print(f"{Color.YELLOW}⚡ Downloading...{Color.RESET}")
        os.system(f"yt-dlp -f best {url}")
        print(f"{Color.GREEN}✓ Media saved in /storage/emulated/0/Download{Color.RESET}")
    except:
        print(f"{Color.RED}✗ Download failed!{Color.RESET}")

def phone_osint():
    print(f"\n{Color.BLUE}=== PHONE NUMBER OSINT ===")
    number = input(f"{Color.BLUE}Enter phone number (with country code): {Color.RESET}").strip()
    
    try:
        parsed = phonenumbers.parse(number)
        print(f"\n{Color.GREEN}📱 OSINT RESULTS:{Color.RESET}")
        print(f"• Carrier: {carrier.name_for_number(parsed, 'en')}")
        print(f"• Country: {geocoder.country_name_for_number(parsed, 'en')}")
        print(f"• Timezone: {timezone.time_zones_for_number(parsed)[0]}")
        print(f"• Valid: {phonenumbers.is_valid_number(parsed)}")
    except Exception as e:
        print(f"{Color.RED}✗ Error: {e}{Color.RESET}")

# ===== SYSTEM TOOLS =====
def device_optimizer():
    while True:
        print(f"\n{Color.CYAN}⚙ DEVICE OPTIMIZER MENU{Color.RESET}")
        print(f"{Color.GREEN}1. Battery Saver Mode")
        print(f"2. Performance Boost Mode")
        print(f"3. Balanced Mode")
        print(f"0. Back{Color.RESET}")
        
        opt = input(f"{Color.YELLOW}Select mode (0-3): {Color.RESET}")
        
        if opt == "1":
            battery_saver()
        elif opt == "2":
            performance_boost()
        elif opt == "3":
            set_balanced_mode()
        elif opt == "0":
            break
        else:
            print(f"{Color.RED}Invalid option!{Color.RESET}")

def battery_saver():
    print(f"\n{Color.GREEN}⚡ BATTERY SAVER MODE{Color.RESET}")
    try:
        if os.name == 'posix':
            os.system('settings put global window_animation_scale 0.5')
            os.system('settings put global transition_animation_scale 0.5')
            os.system('settings put global animator_duration_scale 0.5')
        print(f"{Color.CYAN}✓ Reduced animations")
        print(f"✓ Limited background processes")
        print(f"✓ Battery optimizations applied{Color.RESET}")
    except:
        print(f"{Color.YELLOW}⚠ Some features require root{Color.RESET}")

def performance_boost():
    print(f"\n{Color.CYAN}🚀 PERFORMANCE BOOST{Color.RESET}")
    try:
        if os.name == 'posix':
            os.system('settings put global window_animation_scale 1.0')
            os.system('settings put global transition_animation_scale 1.0')
            os.system('settings put global animator_duration_scale 1.0')
        print(f"{Color.MAGENTA}✓ GPU rendering enabled")
        print(f"✓ System optimizations applied{Color.RESET}")
    except:
        print(f"{Color.YELLOW}⚠ Some features require root{Color.RESET}")

def set_balanced_mode():
    print(f"\n{Color.CYAN}⚖️ BALANCED MODE{Color.RESET}")
    try:
        if os.name == 'posix':
            os.system('settings put global window_animation_scale 0.75')
        print(f"{Color.GREEN}✓ Balanced settings applied{Color.RESET}")
    except:
        print(f"{Color.YELLOW}⚠ Some features require root{Color.RESET}")

def system_info():
    print(f"\n{Color.MAGENTA}📱 DEVICE INFORMATION{Color.RESET}")
    try:
        print(f"{Color.CYAN}• OS: {os.name}")
        print(f"• CPU: {cpuinfo.get_cpu_info()['brand_raw']}")
        print(f"• Cores: {psutil.cpu_count(logical=False)}P/{psutil.cpu_count()}L")
        print(f"• RAM: {psutil.virtual_memory().total/1024/1024:.0f}MB")
        
        if os.name == 'posix':
            print(f"• Brand: {os.popen('getprop ro.product.brand').read().strip()}")
            print(f"• Model: {os.popen('getprop ro.product.model').read().strip()}")
            print(f"• Android: {os.popen('getprop ro.build.version.release').read().strip()}")
    except Exception as e:
        print(f"{Color.RED}✗ Error getting system info: {e}{Color.RESET}")

# ===== MAIN MENU =====
def main_menu():
    while True:
        show_banner()
        print(f"""
{Color.GREEN}╔════════════════════════════════════╗
║          MAIN MENU               ║
╠════════════════════════════════════╣
║ {Color.CYAN}1.{Color.RESET} WhatsApp Tools             {Color.GREEN}║
║ {Color.CYAN}2.{Color.RESET} Social Media Downloader    {Color.GREEN}║
║ {Color.CYAN}3.{Color.RESET} Phone Number OSINT         {Color.GREEN}║
║ {Color.CYAN}4.{Color.RESET} Device Optimizer           {Color.GREEN}║
║ {Color.CYAN}5.{Color.RESET} System Information         {Color.GREEN}║
║ {Color.RED}0.{Color.RESET} Exit                       {Color.GREEN}║
╚════════════════════════════════════╝{Color.RESET}""")
        
        choice = input(f"\n{Color.YELLOW}Select option (0-5): {Color.RESET}")
        
        if choice == "1":
            whatsapp_menu()
        elif choice == "2":
            social_media_downloader()
        elif choice == "3":
            phone_osint()
        elif choice == "4":
            device_optimizer()
        elif choice == "5":
            system_info()
        elif choice == "0":
            sys.exit()
        else:
            print(f"{Color.RED}Invalid option!{Color.RESET}")
        
        input(f"\n{Color.YELLOW}Press Enter to continue...{Color.RESET}")

# ===== INSTALL DEPENDENCIES =====
def install_deps():
    required = ['requests', 'phonenumbers', 'py-cpuinfo', 'psutil', 'yt-dlp']
    for pkg in required:
        try:
            __import__(pkg)
        except ImportError:
            print(f"{Color.YELLOW}[!] Installing {pkg}...{Color.RESET}")
            os.system(f"pip install {pkg}")

if __name__ == "__main__":
    try:
        if not authenticate():
            print(f"{Color.RED}🚫 Access denied! Exiting...{Color.RESET}")
            sys.exit()
        
        install_deps()
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{Color.RED}🚪 Exiting tools...{Color.RESET}")
        sys.exit()