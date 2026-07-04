TURN_THRESHOLD = 20

def should_summarize(turn_count):
    return turn_count >= TURN_THRESHOLD
