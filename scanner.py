import requests

def scan_new_coins():
    coins = []

    # Example dummy data (replace with real API later)
    coin = {
        "name": "TESTINU",
        "mint": "So11111111111111111111111111111111111111112",
        "marketcap": "$45k",
        "holders": 320,
        "dev_hold": 2,
        "top10": 18,
        "image": "https://pump.fun/logo.png",
        "twitter": "https://twitter.com/search?q=TESTINU"
    }

    coins.append(coin)
    return coins
