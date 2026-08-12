import os
import subprocess
import sys
import webbrowser
import time

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = r"""
===================================================================
     ███████╗███╗   ██╗ ██████╗       ███████╗██╗   ██╗ █████╗ ██████╗ 
     ██╔════╝████╗  ██║██╔════╝       ██╔════╝╚██╗ ██╔╝██╔══██╗██╔══██╗
     █████╗  ██╔██╗ ██║██║  ███╗█████╗█████╗   ╚████╔╝ ███████║██║  ██║
     ██╔══╝  ██║╚██╗██║██║   ██║╚════╝██╔══╝    ╚██╔╝  ██╔══██║██╔══██║
     ███████╗██║ ╚████║╚██████╔╝      ███████╗   ██║   ██║  ██║██████╔╝
     ╚══════╝╚═╝  ╚═══╝ ╚═════╝       ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝ 
===================================================================
                 Developed By: Eng.Eyad
===================================================================
"""
    print("\033[1;34m" + banner + "\033[0m")

def install_spotify_and_spotx():
    print("\n\033[1;36m[ Step 1/3 ] Downloading and installing official Spotify...\033[0m")
    temp_dir = os.environ.get('TEMP', 'C:\\Temp')
    installer_path = os.path.join(temp_dir, 'SpotifySetup.exe')
    
    # 1. تحميل وتثبيت سبوتيفاي
    print("\033[1;33m[~] Downloading Spotify from official servers...\033[0m")
    dl_command = f"powershell -Command \"Invoke-WebRequest -Uri 'https://download.scdn.co/SpotifySetup.exe' -OutFile '{installer_path}'\""
    
    download_process = subprocess.Popen(dl_command, shell=True)
    bar_length = 30
    while download_process.poll() is None:
        for i in range(bar_length + 1):
            if download_process.poll() is not None:
                break
            percent = float(i) / bar_length
            arrow = '=' * int(round(percent * bar_length) - 1) + '>'
            spaces = ' ' * (bar_length - len(arrow))
            sys.stdout.write(f"\rDownloading: [{arrow + spaces}] {int(percent * 100)}%")
            sys.stdout.flush()
            time.sleep(0.1)
    
    print("\n\033[1;32m[+] Download completed successfully.\033[0m")
    
    if os.path.exists(installer_path):
        print("\033[1;33m[~] Running Spotify silent installer (Please wait)...\033[0m")
        subprocess.run(f"\"{installer_path}\" /s", shell=True)
        print("\033[1;32m[+] Spotify installed successfully.\033[0m")
    else:
        print("\033[1;31m[!] Failed to download Spotify installer.\033[0m")
        return

    # 2. تشغيل سكريبت SpotX بالمعاملات الخاصة بك تلقائياً
    print("\n\033[1;36m[ Step 2/3 ] Applying SpotX patch and optimizations...\033[0m")
    
    # إعداد معاملات SpotX كما هي في ملف الـ bat بتاعك
    spotx_params = "-confirm_uninstall_ms_spoti -confirm_spoti_recomended_over -podcasts_off -block_update_on -start_spoti -new_theme -adsections_off -lyrics_stat spotify -no_pause"
    url1 = "https://raw.githubusercontent.com/SpotX-Official/SpotX/refs/heads/main/run.ps1"
    url2 = "https://spotx-official.github.io/SpotX/run.ps1"
    
    # بناء أمر الـ PowerShell تماماً مثل الملف المرفق
    ps_command = (
        "$tls = [Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12; "
        f"$p='{spotx_params}'; "
        f"& {{ $(try {{ iwr -useb '{url1}' }} catch {{ $p+= ' -m'; iwr -useb '{url2}' }}) }} $p | iex"
    )
    
    full_powershell_cmd = f"powershell -Command \"{ps_command}\""
    
    print("\033[1;33m[~] Running SpotX script (This may take a moment)...033[0m")
    subprocess.run(full_powershell_cmd, shell=True)
    print("\033[1;32m[+] SpotX patch applied successfully.\033[0m")

def run_spotx_only():
    print("\n\033[1;36m[ ~ ] Running SpotX patcher only...\033[0m")
    spotx_params = "-confirm_uninstall_ms_spoti -confirm_spoti_recomended_over -podcasts_off -block_update_on -start_spoti -new_theme -adsections_off -lyrics_stat spotify -no_pause"
    url1 = "https://raw.githubusercontent.com/SpotX-Official/SpotX/refs/heads/main/run.ps1"
    url2 = "https://spotx-official.github.io/SpotX/run.ps1"
    
    ps_command = (
        "$tls = [Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12; "
        f"$p='{spotx_params}'; "
        f"& {{ $(try {{ iwr -useb '{url1}' }} catch {{ $p+= ' -m'; iwr -useb '{url2}' }}) }} $p | iex"
    )
    subprocess.run(f"powershell -Command \"{ps_command}\"", shell=True)
    print("\033[1;32m[+] SpotX execution finished.\033[0m")

def open_github():
    print("\n\033[1;36m[ Step 3/3 ] Opening your GitHub profile...\033[0m")
    github_url = "https://github.com/ICX40"
    webbrowser.open(github_url)
    print("\033[1;32m[+] GitHub profile opened successfully!\033[0m")

def main():
    while True:
        try:
            print_banner()
            print("  [1] Install Spotify")
            print("  [2] Run Premium")
            print("  [3] Open Eng.Eyad GitHub Profile")
            print("  [4] Exit")
            print("==================================================================-\n")
            
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == '1':
                install_spotify_and_spotx()
                time.sleep(1)
                open_github()
                print("\n\033[1;32m===================================================\033[0m")
                print("\033[1;32m   All processes completed successfully, Engineer!\033[0m")
                print("\033[1;32m===================================================\033[0m")
                input("\nPress Enter to return to the main menu...")
            elif choice == '2':
                run_spotx_only()
                input("\nPress Enter to return to the main menu...")
            elif choice == '3':
                open_github()
                input("\nPress Enter to return to the main menu...")
            elif choice == '4':
                print("\nGoodbye, Engineer!")
                sys.exit(0)
            else:
                print("\n\033[1;31m[!] Invalid choice, please try again.\033[0m")
                time.sleep(2)
        except (EOFError, KeyboardInterrupt):
            break

if __name__ == "__main__":
    main()
