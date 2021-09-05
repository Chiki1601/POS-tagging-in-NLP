#implementation of POS tagging in NLP
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words(&#39;english&#39;))

# Dummy text
txt = &quot;Sukanya, Rajib and Naba are my good friends. &quot; \
&quot;Sukanya is getting married next year. &quot; \
&quot;Marriage is a big step in one’s life.&quot; \
&quot;It is both exciting and frightening. &quot; \
&quot;But friendship is a sacred bond between people.&quot; \
&quot;It is a special kind of love between us. &quot; \
&quot;Many of you must have tried searching for a friend &quot;\
&quot;but never found the right one.&quot;

# sent_tokenize is one of instances of
# PunktSentenceTokenizer from the nltk.tokenize.punkt module
tokenized = sent_tokenize(txt)
for i in tokenized:
# Word tokenizers is used to find the words
# and punctuation in a string
wordsList = nltk.word_tokenize(i)
# removing stop words from wordList
wordsList = [w for w in wordsList if not w instop_words]
# Using a Tagger. Which is part-of-speech
# tagger or POS-tagger.
tagged = nltk.pos_tag(wordsList)
print(tagged)
