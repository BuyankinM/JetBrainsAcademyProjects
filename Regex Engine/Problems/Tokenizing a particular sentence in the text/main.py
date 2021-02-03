from nltk.tokenize import sent_tokenize, regexp_tokenize


sentences = sent_tokenize(input())
my_sent = sentences[int(input())]
print(regexp_tokenize(my_sent, "[A-z']+"))