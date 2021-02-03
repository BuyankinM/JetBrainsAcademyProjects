from nltk.tokenize import regexp_tokenize


tokens = regexp_tokenize(input(), r"[A-Za-z]+")
print(tokens[int(input())])
