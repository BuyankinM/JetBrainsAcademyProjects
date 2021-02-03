def check_email(string: str):
    if " " in string or "@" not in string:
        return False
    pos = string.find("@")
    pos_dot = string.find(".", pos)
    return pos_dot > pos + 1
