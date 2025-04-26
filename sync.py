import os
import time
import socket
import json
from datetime import datetime

def save_sync_log():
    current_date = datetime.now()
    log_dir = "sync_logs"
    
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    filename = f"{log_dir}/{current_date.year}_{current_date.month:02d}.json"
    
    log_entry = {
        "date": current_date.strftime("%Y-%m-%d"),
        "time": current_date.strftime("%H:%M:%S"),
        "status": "success"
    }
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = []
    else:
        logs = []
    
    logs.append(log_entry)
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)
    
    print(f"{filename} ✨")

def check_network_connection():
    try:
        socket.create_connection(("www.github.com", 80), timeout=5)
        return True
    except socket.error:
        return False

def sync_repository():
    if check_network_connection():
        print("✨ Network connection established. Starting sync process... ✨")
        print("(◕‿◕) Waiting for 60 seconds before syncing...")
        time.sleep(60)

        # Certifique-se de que o credential helper está configurado
        os.system("git config --global credential.helper store")
        
        git_commands = [
            "git init",
            "git remote remove origin 2>/dev/null || true",
            "git remote add origin https://github.com/kx4x/sync.git",
            "git branch -M main",
            "git add .",
            f"git commit -m \"Sync: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} 🌟\"",
            "git push -u origin main"
        ]

        for command in git_commands:
            os.system(command)
            print(f"(づ｡◕‿‿◕｡)づ Executed: {command}")

        print("(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ Repository sync completed successfully! ✧ﾟ･: *ヽ(◕ヮ◕ヽ)")
        save_sync_log()
    else:
        print("(╯°□°）╯︵ ┻━┻ No network connection. Sync process aborted.")

if __name__ == "__main__":
    print("(｡♥‿♥｡) Starting the sync process...")
    sync_repository()
