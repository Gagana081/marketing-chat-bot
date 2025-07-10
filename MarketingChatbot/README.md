# Marketing Chatbot

This chatbot simulates real-time communication between a client and a merchant using command-line interfaces. Powered by Hugging Face Transformers.

## Features

- Separate scripts for client and merchant.
- Real-time file-based communication.
- Hugging Face-powered auto-reply fallback.

## Setup Instructions

### 1. Install Python 3.8+
### 2. Create a Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Chatbot

Open two terminal windows:

#### Terminal 1 (Merchant)
```bash
python merchant.py
```

#### Terminal 2 (Client)
```bash
python client.py
```

### 5. Chat!

Type messages in the client window, respond from the merchant side.

## Notes

- All messages are stored in `shared_messages.json`.
- Bot can generate responses if merchant leaves input blank.

## License

MIT