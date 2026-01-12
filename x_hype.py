def check_x_hype(name):
    # TEST logic: keyword based (X hype compulsory later)
    keywords = ["AI", "MEME", "COIN"]
    return any(k.lower() in name.lower() for k in keywords)
