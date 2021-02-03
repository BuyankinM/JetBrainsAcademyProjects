from nltk.stem import SnowballStemmer


# the following line reads a text from the input and converts it into a list
sent = input().split()
SS = SnowballStemmer("german")
print("\n".join([SS.stem(word) for word in sent]))
