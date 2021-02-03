from nltk.stem import SnowballStemmer


sent = input().split()
snowball = SnowballStemmer('english')

for word in sent:
    print(snowball.stem(word))