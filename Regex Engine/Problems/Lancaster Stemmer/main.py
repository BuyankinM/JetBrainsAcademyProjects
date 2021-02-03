from nltk.stem import LancasterStemmer


sent = input().split()
lcs = LancasterStemmer()
print("\n".join([lcs.stem(word) for word in sent]))
