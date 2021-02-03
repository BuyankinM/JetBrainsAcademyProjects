def add_viewer(name, fans=None):
    if fans is None:
        fans = []
    fans.append(name)
    return fans