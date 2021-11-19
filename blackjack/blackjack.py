def card_score(cards):
    # catch errors in input
    if not isinstance(cards, str):
        raise ValueError(f"The `cards` param must be string, got: {type(cards)}")
    if len(cards) < 2:
        raise ValueError(f"The `cards` param needs to be < 2, got: {cards}")
    numbers = [c for c in cards if c in "23456789"]
    faces = [c for c in cards if c in "JQK"]
    n_aces = sum([1 for c in cards if c == "A"])
    score = sum([int(i) for i in numbers]) + len(faces) * 10
    while n_aces > 0:
        score += 1 if score + 11 > 21 else 11
        n_aces -= 1
    return score if score <= 21 else 0
