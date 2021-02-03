def check_word(word):
    if "0" in word:
        raise NotWordError(word)
    return word

def error_handling(word):
    try:
        res = check_word(word)
    except NotWordError as err:
        print(err)
    else:
        print(res)