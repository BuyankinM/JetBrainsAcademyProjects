def sort_names(names):
    """Sort names by length in descending order."""
    for i in range(len(names) - 1):
        index = i
        for j in range(i + 1, len(names)):
            if len(names[j]) > len(names[index]):
                index = j
        if index != i:
            names[index], names[i] = names[i], names[index]

    return names
