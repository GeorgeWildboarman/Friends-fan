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

## 1.4. Conclusion


Bye,bye!
