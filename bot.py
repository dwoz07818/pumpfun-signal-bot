from telegram import Bot
from scanner import scan_new_coins
from config import TELEGRAM_TOKEN, CHAT_ID
import time

bot = Bot(token=TELEGRAM_TOKEN)

def send(msg):
    bot.send_message(chat_id=CHAT_ID, text=msg)

while True:
    signals = scan_new_coins()
    for s in signals:
        send(s)
    time.sleep(60)
