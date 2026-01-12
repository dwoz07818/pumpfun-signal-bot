from telegram import Bot
from scanner import scan_new_coins
from config import TELEGRAM_TOKEN, CHAT_ID
import time

bot = Bot(token=TELEGRAM_TOKEN)

def send_signal(coin):
    msg = f"""
🚀 EARLY SIGNAL

Name: {coin['name']}
Liquidity: ${coin['liquidity']}
Dev Hold: {coin['dev_hold']}%
Top10: {coin['top10']}%
Holders: {coin['holders']}
Score: {coin['score']}
"""

    if "image" in coin and coin["image"]:
        bot.send_photo(
            chat_id=CHAT_ID,
            photo=coin["image"],
            caption=msg
        )
    else:
        bot.send_message(chat_id=CHAT_ID, text=msg)

while True:
    coins = scan_new_coins()
    for c in coins:
        send_signal(c)
    time.sleep(60)
