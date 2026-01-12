from filters import check_filters
from x_hype import check_x_hype

def scan_new_coins():
    coin = {
        "name": "AI_TEST",
        "liquidity": 6000,
        "dev_hold": 3,
        "top10": 20,
        "holders": 120,
        "score": 80,
        # TEST IMAGE (abhi)
        "image": "https://cryptologos.cc/logos/solana-sol-logo.png"
    }

    if check_filters(coin) and check_x_hype(coin["name"]):
        return [coin]
    return []
