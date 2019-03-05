# ./src/timings.py
def has_cooldown(current_time, last_action, cooldown):
    return not current_time - last_action >= cooldown