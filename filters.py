from config import *

def check_filters(coin):
    score = 0

    if coin["holders"] >= MIN_HOLDERS:
        score += 25

    if coin["dev_hold"] <= MAX_DEV_HOLD:
        score += 25

    if coin["top10"] <= MAX_TOP10:
        score += 25

    if score >= MIN_SCORE:
        coin["risk"] = "🟢 SAFE"
        return True

    coin["risk"] = "🔴 RISKY"
    return False
