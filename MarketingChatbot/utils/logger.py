import json
import os

LOG_FILE = "chat_history.json"

def log_message(sender, message):
    entry = {
        "sender": sender,
        "message": message
    }
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r+") as file:
            data = json.load(file)
            data.append(entry)
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
    else:
        with open(LOG_FILE, "w") as file:
            json.dump([entry], file, indent=4)
