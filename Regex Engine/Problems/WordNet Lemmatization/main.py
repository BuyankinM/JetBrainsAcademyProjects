from nltk.stem import WordNetLemmatizer
from nltk.corpus.reader.wordnet import VERB, ADJ


word = input()
WNL = WordNetLemmatizer()

print(WNL.lemmatize(word))
print(WNL.lemmatize(word, pos=ADJ))
print(WNL.lemmatize(word, pos=VERB))