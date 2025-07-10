import json
import time
from transformers import pipeline
from utils.logger import log_message


SHARED_FILE = 'shared_messages.json'

def send_message(msg):
    with open(SHARED_FILE, 'r+') as file:
        data = json.load(file)
        data['client_to_merchant'].append(msg)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()

def check_for_reply(last_index):
    with open(SHARED_FILE, 'r') as file:
        data = json.load(file)
        replies = data['merchant_to_client']
        if len(replies) > last_index:
            return replies[last_index:], len(replies)
        return [], last_index

def main():
    print("Client chatbot started. Type your message and wait for a response (type 'exit' to quit).")
    last_reply_index = 0

    while True:
        msg = input("You (Client): ")
        log_message("Client", msg)
        if msg.lower() == 'exit':
            break

        send_message(msg)

        print("Waiting for merchant reply...", end="", flush=True)
        while True:
            replies, last_reply_index = check_for_reply(last_reply_index)
            if replies:
                for r in replies:
                    print(f"\nMerchant: {r}")
                break
            print(".", end="", flush=True)
            time.sleep(1)

if __name__ == "__main__":
    main()