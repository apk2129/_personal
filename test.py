# import nltk
# nltk.download('punkt')

from nltk.tokenize import word_tokenize, sent_tokenize

line = "Natural Language Processing is the task we give computers to read and understand (process) written text (natural language). By far, the most popular toolkit or API to do natural language processing is the Natural Language Toolkit for the Python programming language. "

print(sent_tokenize(line))
