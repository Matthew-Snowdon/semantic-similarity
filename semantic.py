# importing libraries, requires install
import spacy

# The main difference when loading 'en_core_web_sm' is this model doesn't have
# word vectors, so the comparisons made aren't as accurate.
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# cat and monkey have a 59% similarity and monkey and banana have a 40%
# similarity, both are animals and monkeys like bananas but cats don't like
# bananas - you can see how to values are derived, it's definitely interesting.
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# I don't know how monkey and tiger have a higher similarity at 64% than cat
# and tiger at 56% but there you go, the model values similarity in the animal
# species over the fact that a tiger is a cat...but a cat isn't always a tiger.
tokens = nlp('cat tiger monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
