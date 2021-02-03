def object_with_beautiful_identity():
    for i in range(10_000):
        id_str = str(id(i))
        if id_str.endswith("888"):
            return i