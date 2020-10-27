# 1. Build ChatBot to talk with 'Friends'


## 1.1. Introduction 


Hello!!!


I just started learning Python by myself, so I'm still a beginner.


Now I'm trying to build a chatbot with Python3 to have a fun. 
It will help to improve my skills, although it will take me a very long time to complete.


Give it a try!


My goal is to make a simple chatbot that talks as if it were one of 'Friends'. 
Because I am a fan of 'Friends', popular American television sitcom.


All the resources of the scripts of 'Friends' are provided by Crazy For Friends.

Resource website URL: http://www.livesinabox.com/friends/scripts.shtml


## 1.2. Crawl and Scrape

[grab-webcontents.py](grab-webcontents.py)
- Get the contents of the scripts from [the resource site](http://www.livesinabox.com/friends/scripts.shtml). 
- Store them in a local directory assigned by an argument.
 

Usage: python3 grab-webcontents.py [dir_path=.scripts] 
dir_path is direcory path and default is '.scripts'.


```bash
python3 grab-webcontents.py .scripts
```



## 1.3. Natural Language Processing with Tensorflow


### 1.3.1. Pre-process the raw text.
Raw text retrieved from wave site contains numbers, special characters, and others noise. In this process I remove characters that can interfere with text analysis.

[preprocess_of_raw_data.py](preprocess_of_raw_data.py)

- Process for removing punctuation

string.punctuation is string of panctuation characters defined in string module.
The String of ASCII characters which are considered punctuation is shown by:
      
```python
import string
print('Punctuation Characters   : {}'.format( string.punctuation ))
# Punctuation Characters   : !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```


  But Characters of period, quesion mark, and exclamation mark are needed to be remain, and later traslated into <EOS>.

```python
my_punctuation = '"#$%&\'()*+,-/:;<=>@[\]^_`{|}~'
print('My Punctuation Characters: {}'.format( my_punctuation ))
# My Punctuation Characters: !"#$%&'()*+,-/:;<=>?@[\]^_`{|}~
```


  The string methode of str.maketrans() returns a translation table usable for str.translate().
  The third argument is a string, whose characters will be mapped to None in the result.

```python
punct_table = str.maketrans('','',string.punctuation)
```


  The result is the same as below:

```python
punct_table = dict((ord(c),None) for c in string.punctuation)
```
  str.translate() returns a copy of the text in which each charactors are mapped through the given translation table.

```python
text = text.translate(punct_table)
```

  **e.g.**

  Given the text:

  Two thousand dollars!? What do you think I am? I soap opera star!? Yeah... That's right I am!
  
  Translated into:

  Two thousand dollars What do you think I am I soap opera star Yeah Thats right I am


```python
import string
text = "Two thousand dollars!? What do you think I am? I soap opera star!? Yeah... That\'s right I am!"
punct_table = str.maketrans('','',string.punctuation)
text_translated = text.translate(punct_table)
```





### 1.3.2. Installation of Tensorflow from Anaconda
  - Create virtual environment for Tensorflow with Python3.6 or Python3.7
  - Open Anaconda Powershell

```bash
conda activate <virtual evironment name>
conda upgrade -y --all
conda clean -y --packages
```
        
for CPU
```bash
conda install -y tensorflow tensorflow-datasets
```
        
for GPU
```bash
conda install -y tensorflow-gpu tensorflow-datasets
```
        
Check Tensorflow version
```bash
python -c "import tensorflow as tf; print(tf.__version__)"
```

### 1.3.3 Tokenize with TensorFlow

After pre-process of raw text you have to tokenize and vectorize the words in the text to use for machine learning models.

Here we use a tokenizer from tensorflow utility for tokenize and vectorize.

```python
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
```

This class allows to vectorize a text corpus, by turning each text into either a sequence of integers (each integer being the index of a token in a dictionary) or into a vector where the coefficient for each token could be binary, based on word count, based on tf-idf..

[tokenize_and_convert_into_numpy_array.py](tokenize_and_convert_into_numpy_array.py)

Create a instance of Tokenizer with arguments:
num_words: the maximum number of words to keep, based on word frequency. Only the most common `num_words-1` words will be kept.
filters: a string where each element is a character that will be filtered from the texts. The default is all punctuation, plus tabs and line breaks, minus the `'` character.
lower: boolean. Whether to convert the texts to lowercase.
split: str. Separator for word splitting.
char_level: if True, every character will be treated as a token.
oov_token: if given, it will be added to word_index and used to replace out-of-vocabulary words during text_to_sequence calls


```python
# Using tensorflow tokenizer, you can label each word and provide a dictionary of the words being used in the sentences.
# We create an instance of tokenizer with assigning a hyperparameter num_words.
# The hyperparameter oov_token assigns certian value to words which are not seen in the corpus.

tokenizer = Tokenizer(num_words=num_words, filters='!"#$%&()*+,-./:;=?@[\\]^_`{|}~\t\n', oov_token='<OOV>',lower=False)

# The fit_on_texts() method is used to encode the words in sentences of text.
tokenizer.fit_on_texts(sentences)

# The word_index() method gives a dictionary of all key-value pairs where the key is the word in the sentence and the value is the label assigned to it.
word_index = tokenizer.word_index

# The full vocabulary size is given by the number of words in the dictionary plus one, which is the value of '0' and used to pad out of words in sequence.
vocab_size = len(word_index)+1

```

We need another dictionary that is used to convert index into a word from prediction result.
```python
# Dictionary that is used to translate index into word is given by:
index_word = {v:k for k,v in word_index.items()}
```



## 1.4. Conclusion


Bye,bye!
