# PrimeAlgo Chat Terminal (Offline/Simulation Mode with Basic UI)
# Console-based UI with colored output to make it visually better.

# ---------- Setup Instructions ----------
# 1. Ensure Python 3.10+ is installed.
# 2. Install required packages:
#    pip install pandas colorama
# 3. Run this script using:
#    python primealgo_console_ui_terminal.py

from datetime import datetime
import time
import pandas as pd
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# ---------- Configuration ----------
SENDER_NAME = "Trader"  # Predefined sender name

# ---------- Local Message Store ----------
messages_store = []

def print_message(msg):
    print(Fore.CYAN + f"[{msg['timestamp']}] " + Fore.GREEN + f"{msg['sender']}: " + Style.RESET_ALL + f"{msg['text']}")

print(Fore.MAGENTA + "\n--- PrimeAlgo Chat Terminal (Simulation Mode) ---")
print(Fore.YELLOW + f"Sender: {SENDER_NAME}\n")

# Example messages to simulate sending
messages_to_send = [
    "Hello, this is a test message.",
    "Checking the chat terminal functionality.",
    "Final automated message."
]

# Send messages automatically
for message_text in messages_to_send:
    msg = {
        'id': str(datetime.now().timestamp()),
        'timestamp': datetime.now().isoformat(),
        'sender': SENDER_NAME,
        'text': message_text
    }
    messages_store.append(msg)
    print(Fore.GREEN + f"Sent: {message_text}")
    time.sleep(1)  # Simulate delay

# Display last 20 messages
print(Fore.MAGENTA + "\n--- Last 20 Messages ---")
for msg in messages_store[-20:]:
    print_message(msg)

# Optional: store messages in a CSV for later analysis
df = pd.DataFrame(messages_store)
df.to_csv("simulated_chat_log.csv", index=False)

print(Fore.MAGENTA + "\nPrimeAlgo Chat Terminal simulation run completed. Messages saved to simulated_chat_log.csv.")
