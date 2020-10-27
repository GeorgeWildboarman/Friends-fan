# -*- coding: utf-8 -*-

import os
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

pw_dir = os.path.dirname(__file__)

# num_words: the maximum number of words to keep, based on word frequency. Only the most common `num_words-1` words will be kept.
num_words = 10000

# # Each input sequence contains seq_length words.
seq_length = 40

# Tokenized words are converted into numpy array below and saved into a file of np_file in a directory of np_dir.
np_file = 'np_input_data.npz'
np_dir = '.numpy_data'

# Search dir and list up txt-file paths. 
data_dir = '.txt_data'
startpath = os.getcwd()
dir_path = ''
path_list = []
for root, dirs, files in os.walk(startpath, topdown=True):
    if os.path.basename(root) == data_dir:
        path_list.extend(os.path.join(root,f)for f in files)
        print('txt-file dir path: {}'.format(root))
        break

# dir_path_for_txt = 'd:/gitsandbox/sentiment/.txt_data'
# filename = '913sings.txt'
# path = os.path.join(dir_path_for_txt,filename)

# Open and read text files
# path_list =[path]

# Read preprosecced text files.
print('Reading text files...')
sentences = []
for path in path_list:
    with open(path,mode='r',encoding='utf_8') as f:
        sentences.append(f.read())

# Using tensorflow tokenizer, you can label each word and provide a dictionary of the words being used in the sentences.
# We create an instance of tokenizer with assigning a hyperparameter num_words.
# The hyperparameter oov_token assigns certian value to words which are not seen in the corpus.

print('Tokenizing...')
tokenizer = Tokenizer(num_words=num_words, filters='!"#$%&()*+,-./:;=?@[\\]^_`{|}~\t\n', oov_token='<OOV>',lower=False)

# The fit_on_texts() method is used to encode the sentences.
tokenizer.fit_on_texts(sentences)
print(f'The number of given sentences: {tokenizer.document_count}')

# The word_index() method gives a dictionary of all key-value pairs where the key is the word in the sentence and the value is the label assigned to it.
word_index = tokenizer.word_index

# The full vocabulary size is given by the number of words in the dictionary plus one to pad the value of '0'.
vocab_size = len(word_index)+1
num_words = min([vocab_size,num_words])
print('Full vocabulary size: {}'.format(vocab_size))
print('Applied vocabulary size: {}'.format(num_words))

# Dictionary that is used to translate index into word is given by:
index_word = {v:k for k,v in word_index.items()}

# Convert the dictionary to numpy array
names = ['index','word']
formats = [np.int16,np.object]
dtype = dict(names=names,formats=formats)
np_index_word = np.array(list(index_word.items()),dtype=dtype)

# The texts_to_sequences() method gives labelled equivalent based on the corpus of the words. To pass senctences it returns the labels.
sequences = tokenizer.texts_to_sequences(sentences)

# Use pad_sequences() to pad sequences with variable length strings.
# If set the hyperparameter padding to be post, the padding is to be done after the sentence.  
# Padding is generally done with reference to longest sentence, however the hyperparameter maxlen can define the maxium length of the sentence.
# maxlen = 100
# padded_seq = pad_sequences(sequences, padding='post')
# padded_seq = pad_sequences(sequences, padding='post', maxlen=maxlen)

# The sequences provided by texts_to_sequence() are divided into input sequences.  
# Each input sequence contains seq_length words.

print('The lenght of input sequence: ',seq_length)
# For each input sequence, the corresponding targets contain one word shifted from the end of the sequence to the right
x = [] # input sequences
y = [] # targets
print('Creating input sequence and targets...')
for sq in sequences:
    for i,s in enumerate(sq[:-seq_length]):
        x.append(sq[i:seq_length+i])
        y.append(sq[seq_length+i])

print('The number of input sequences: ',len(x))

x = np.array(x, dtype=np.int16).reshape(len(x),seq_length)
y = np.array(y, dtype=np.int16).reshape(len(y),1)
print('shape of x: ',x.shape)
print('shape of y: ',y.shape)

# Saving input sequences, targets, and dict as numpy
print('Saving input sequences, targets, and dict as numpy...')

# Make dir to store numpy data.
np_path = os.path.join(pw_dir,np_dir)
if not os.path.isdir(np_path):
    print('Created new directory for numpy data: ',np_path)
    os.makedirs(np_path, exist_ok=True)
else:
    print('Directory of \"{}\" already exits.'.format(np_path))

file_path = os.path.join(np_path,np_file)
np.savez(file_path,x,y,np_index_word)

