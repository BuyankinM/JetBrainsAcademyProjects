def get_percentage(value, round_digits=None):
    percent = value * 100
    if round_digits is None:
        return f"{round(percent)}%"
    return f"{round(percent, round_digits)}%"
