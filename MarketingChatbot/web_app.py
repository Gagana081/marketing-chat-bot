from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os
import time

app = Flask(__name__)
SHARED_FILE = "shared_messages.json"

def init_messages_file():
    if not os.path.exists(SHARED_FILE):
        with open(SHARED_FILE, "w") as f:
            json.dump({"messages": []}, f)

def read_messages():
    with open(SHARED_FILE, "r") as f:
        return json.load(f)

def write_messages(data):
    with open(SHARED_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/")
def home():
    return redirect(url_for("client_chat"))

@app.route("/client", methods=["GET", "POST"])
def client_chat():
    init_messages_file()
    data = read_messages()

    if request.method == "POST":
        msg = request.form["message"]
        data["messages"].append({
            "sender": "Client",
            "text": msg,
            "timestamp": time.time()
        })
        write_messages(data)
        return redirect(url_for("client_chat"))

    messages = sorted(data["messages"], key=lambda x: x["timestamp"])
    return render_template("chat.html", role="Client", messages=messages)

@app.route("/merchant", methods=["GET", "POST"])
def merchant_chat():
    init_messages_file()
    data = read_messages()

    if request.method == "POST":
        msg = request.form["message"]
        data["messages"].append({
            "sender": "Merchant",
            "text": msg,
            "timestamp": time.time()
        })
        write_messages(data)
        return redirect(url_for("merchant_chat"))

    messages = sorted(data["messages"], key=lambda x: x["timestamp"])
    return render_template("chat.html", role="Merchant", messages=messages)

# ✅ JSON API for real-time updates
@app.route("/messages")
def get_messages():
    data = read_messages()
    messages = sorted(data["messages"], key=lambda x: x["timestamp"])
    return jsonify(messages)

if __name__ == "__main__":
    app.run(debug=True)
