from config import *

def check_filters(c):
    return (
        c["liquidity"] >= MIN_LIQUIDITY and
        c["dev_hold"] <= MAX_DEV_HOLD and
        c["top10"] <= MAX_TOP10 and
        c["holders"] >= MIN_HOLDERS and
        c["score"] >= MIN_SCORE
    )
