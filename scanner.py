from filters import check_filters
from x_hype import check_x_hype

def scan_new_coins():
    # TEST coin (abhi real data nahi)
    coin = {
        "name": "AI_TEST",
        "liquidity": 6000,
        "dev_hold": 3,
        "top10": 20,
        "holders": 120,
        "score": 80
    }

    if check_filters(coin) and check_x_hype(coin["name"]):
        return [format_signal(coin)]
    return []

def format_signal(c):
    return f"""
🚀 EARLY SIGNAL (TEST)

Name: {c['name']}
Liquidity: ${c['liquidity']}
Dev Hold: {c['dev_hold']}%
Top10: {c['top10']}%
Holders: {c['holders']}
Score: {c['score']}
"""
