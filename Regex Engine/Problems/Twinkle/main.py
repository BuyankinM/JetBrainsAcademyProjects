import nltk


poem = ['Twinkle', ',', 'twinkle', ',', 'little', 'star', ',',
        'How', 'I', 'wonder', 'what', 'you', 'are', '.',
        'Up', 'above', 'the', 'world', 'so', 'high', ',',
        'Like', 'a', 'diamond', 'in', 'the', 'sky', '.']

print("\n".join(word for word, tag in nltk.pos_tag(poem) if tag == "NN"))