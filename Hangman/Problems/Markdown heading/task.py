def heading(sym, num=1):
    num = max(num, 1)
    num = min(num, 6)
    return f"{'#' * num} {sym}"