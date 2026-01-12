from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from scanner import scan_new_coins
from filters import check_filters
from config import *
import time

bot = Bot(token=TELEGRAM_TOKEN)

def send_signal(coin):
    pumpfun = f"https://pump.fun/{coin['mint']}"
    bullx   = f"https://bullx.io/terminal?chain=solana&address={coin['mint']}"
    axiom   = f"https://axiom.trade/token/{coin['mint']}"

    keyboard = [
        [InlineKeyboardButton("🚀 Buy on Pump.fun", url=pumpfun)],
        [
            InlineKeyboardButton("📈 BullX", url=bullx),
            InlineKeyboardButton("⚡ Axiom", url=axiom)
        ],
        [InlineKeyboardButton("🔥 X Hype", url=coin["twitter"])]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    caption = f"""
🪙 *{coin['name']}*
💰 MC: {coin['marketcap']}
👥 Holders: {coin['holders']}
🧠 Risk: {coin['risk']}
"""

    bot.send_photo(
        chat_id=CHAT_ID,
        photo=coin["image"],
        caption=caption,
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

while True:
    coins = scan_new_coins()
    for coin in coins:
        if check_filters(coin):
            send_signal(coin)
    time.sleep(60)
