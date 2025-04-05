import os
import re
import time

# Color codes
green = '\033[92m'
reset = '\033[0m'
cyan = '\033[96m'
yellow = '\033[93m'

def banner():
    os.system("clear" if os.name == 'posix' else 'cls')
    print(cyan + r"""
     
   _____ __________  _________   _____      _____   
  /  _  \\______   \/   _____/  /  _  \    /     \  
 /  /_\  \|       _/\_____  \  /  /_\  \  /  \ /  \ 
/    |    \    |   \/        \/    |    \/    Y    \
\____|__  /____|_  /_______  /\____|__  /\____|__  /
        \/       \/        \/         \/         \/ 

    """ + reset)
    print("="*50)
    print(f"  {yellow}>>> ARSAM TEXT CLEANER TOOL <<<{reset}")
    print("="*50)
    print(f"  Owner   : {green}Arsam Sheikh{reset}")
    print(f"  Github  : {cyan}https://github.com/Arsam-Dev404{reset}")
    print(f"  Version : 2.0 (Premium)")
    print("="*50 + "\n")

def is_valid(line):
    return bool(re.match(r'^[0-9]{10,}\|[a-zA-Z\s]+$', line.strip()))

def clean_file():
    input_path = input("Enter input file path (e.g. /sdcard/file.txt): ")
    output_path = input("Enter output file path (e.g. /sdcard/cleaned.txt): ")
    
    try:
        with open(input_path, 'r', encoding='latin-1') as infile:
            lines = infile.readlines()
    except Exception as e:
        print(f"\n{red}Error reading file:{reset}", e)
        return

    cleaned = [line for line in lines if is_valid(line)]
    removed = len(lines) - len(cleaned)

    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write(''.join(cleaned))

    print(f"\n{green}[✓] SUCCESS!{reset}")
    print(f"  Original lines: {len(lines)}")
    print(f"  Cleaned lines: {len(cleaned)}")
    print(f"  Removed lines: {removed}")
    print(f"\n{yellow}File saved to:{reset} {output_path}\n")

# ==== MAIN ====
if __name__ == "__main__":
    while True:
        banner()
        print(f" {cyan}[1]{reset} Clean Corrupted File")
        print(f" {cyan}[2]{reset} Exit\n")
        choice = input(f" {yellow}[?]{reset} Enter your choice: ")

        if choice == '1':
            clean_file()
            input("\nPress Enter to return to menu...")
        elif choice == '2':
            print(f"\n{yellow}Thank you for using Arsam Text Cleaner!{reset}")
            break
        else:
            print(f"\n{red}Invalid choice!{reset}")
            time.sleep(1)
