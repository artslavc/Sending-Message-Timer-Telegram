import time
from pyrogram import Client

API_ID = ""
API_HASH = ""
CHAT_IDS = ['chat_id1', 'chat_id2']
MESSAGE = "MESSAGE"

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH)

def send_message():
    with app:
        for chat_id in CHAT_IDS:
            app.send_message(chat_id, MESSAGE)
            print(f"Сообщение отправлено в чат: {chat_id}")

if __name__ == "__main__":
    while True:
        send_message()
        time.sleep(600)

