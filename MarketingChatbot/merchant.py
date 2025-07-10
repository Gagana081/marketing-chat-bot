import json
import time
from transformers import pipeline
from utils.logger import log_message

SHARED_FILE = 'shared_messages.json'

# Use correct Hugging Face pipeline
def load_bot():
    return pipeline("text2text-generation", model="facebook/blenderbot-400M-distill")

def read_messages(last_index):
    with open(SHARED_FILE, 'r') as file:
        data = json.load(file)
        msgs = data['client_to_merchant']
        if len(msgs) > last_index:
            return msgs[last_index:], len(msgs)
        return [], last_index

def send_reply(reply):
    with open(SHARED_FILE, 'r+') as file:
        data = json.load(file)
        data['merchant_to_client'].append(reply)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()

def main():
    print("Merchant chatbot started. Waiting for client messages...")
    last_msg_index = 0
    bot = load_bot()

    while True:
        msgs, last_msg_index = read_messages(last_msg_index)
        if msgs:
            for msg in msgs:
                print(f"\nClient: {msg}")
                response = input("You (Merchant): ")

                # Generate response using BlenderBot if input is empty
                if not response.strip():
                    response = bot(msg, max_length=100)[0]['generated_text']

                log_message("Merchant", response)  # ✅ log only the final response
                send_reply(response)
        time.sleep(1)


if __name__ == "__main__":
    main()
