#! /usr/bin/python3

import nltk
from collections import defaultdict

#from nltk.tokenize import word_tokenize
#from nltk.tokenize import sent_tokenize
#from nltk import pos_tag
#from nltk import RegexpParser

# A variable 'text' is passed in nltk modules.
text = "But you gotta have turkey on Thanksgiving! I mean, Thanksgiving with no turkey is like-like Fourth of July with no apple pie! Or Friday with no two pizzas!"
print("Text:",text)

# Tokenization of words
tokens = nltk.tokenize.word_tokenize(text)
print("After word tokenize:",tokens)

# Tokenization of sentences
s_tokens = nltk.tokenize.sent_tokenize(text)
print("After sentence tokenize:",s_tokens)

# POS(Parts of Speech) Tagging
tokens_tag = nltk.pos_tag(tokens)
print("After POS tagging:",tokens_tag)

print(
r'''
Abbreviation	Meaning
CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective (large)
JJR	adjective, comparative (larger)
JJS	adjective, superlative (largest)
LS	list market
MD	modal (could, will)
NN	noun, singular (cat, tree)
NNS	noun plural (desks)
NNP	proper noun, singular (sarah)
NNPS	proper noun, plural (indians or americans)
PDT	predeterminer (all, both, half)
POS	possessive ending (parent\ 's)
PRP	personal pronoun (hers, herself, him,himself)
PRP$	possessive pronoun (her, his, mine, my, our )
RB	adverb (occasionally, swiftly)
RBR	adverb, comparative (greater)
RBS	adverb, superlative (biggest)
RP	particle (about)
TO	infinite marker (to)
UH	interjection (goodbye)
VB	verb (ask)
VBG	verb gerund (judging)
VBD	verb past tense (pleaded)
VBN	verb past participle (reunified)
VBP	verb, present tense not 3rd person singular(wrap)
VBZ	verb, present tense with 3rd person singular (bases)
WDT	wh-determiner (that, what)
WP	wh- pronoun (who)
WRB	wh- adverb (how)
'''
)


# Chuking
#patterns = "mychunk:{<NN.?>*<VBD.?>*<JJ.?>*<CC>?}"
patterns = "mychunk:{<NN.?>*<VB.?><JJ.?>*}"
chunker = nltk.RegexpParser(patterns)
print("After Regex:",chunker)
output = chunker.parse(tokens_tag)
print("After Chunking",output)

# Stemming, normalization for words to showup the root word
ps = nltk.stem.PorterStemmer()
#ps = nltk.stem.porter.PorterStemmer()
for w in tokens:
    rootWord = ps.stem(w)
    print('Stemming: {} >> {}'.format(w,rootWord))

# Lemmatization, the algorithmic process of finding the lemma of a word
wl = nltk.stem.WordNetLemmatizer()
for w in tokens:
    rootWord = wl.lemmatize(w)
    print('Lemma: {} >> {}'.format(w,rootWord))

# Lemmatization with wordnet dictionary
tag_map = defaultdict(lambda : nltk.corpus.wordnet.NOUN)
tag_map['J'] = nltk.corpus.wordnet.ADJ
tag_map['V'] = nltk.corpus.wordnet.VERB
tag_map['R'] = nltk.corpus.wordnet.ADV
for token, tag in tokens_tag:
    lemma = wl.lemmatize(token, tag_map[tag[0]])
    print('Lemma wit wordnet: {} >> {}'.format(token,lemma))




