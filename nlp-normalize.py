#! /usr/bin/python3

import re,string,os
from bs4 import BeautifulSoup
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.stem import WordNetLemmatizer

# Path of  an example of html content for Morphological Analysis.
filename = '.scripts/809rumor.htm'
path = os.path.join(os.path.dirname(__file__),filename)

def read_content(path):
    with open(path,'r',encoding='utf_8') as f:
        content = f.read()
    return content

def retrieve_text(content):
    '''
    Retriev text from html-content.
    content : content in html
    '''
    # BeautifulSoup Analysis of html-content
    soup = BeautifulSoup(content,'html.parser')
    ptags = soup.find_all('p')

    text = '' # Text Retrieved from html-content
    for ptag in ptags:
        btag = ptag.b
        if btag != None:
            #print('[ Original Text ]\n',ptag.text)
            btag.clear() # remove b-tags
            result = re.sub(r'\n+?',r' ',ptag.text) # remove newline code
            #print('[ After remove b-tags and newline code ]\n',result,'\n')
            text += result +'\n'
    return text

def remove_noise(text,pattern,newcar=''):
    '''
    Remove noise from text with RegExp.
    Return a new text of result from remove.
    Arguments
    text : text to be removed
    pattern : noise pattern in RegExp
    newcar : replacement of removed noise in string
    '''
    return re.sub(pattern,newcar,text)


def pre_process_raw_text(text):
    oldtext = text
    
    # Pattern for sentences enclosed in parentheses and curly bracket.
    pattern = '(\(|\{)(.*?\s*?)*?(\)|\})'
    # Remove parenthesized and bracketed
    text = re.sub(pattern,'',text)
    
    #text = remove_noise(text,pattern)
    #paren = re.compile(pattern)
    #text = paren.sub('',text)
    
    # Remove characters that can interfere with text analysis.
    pattern = r'(—|-|…)+?'
    text = re.sub(pattern,' ',text)

    #text = text.lower() # convert to lowercase

    # Remove punctuation.
    # remove_punct_dict = dict((ord(punct),None) for punct in string.punctuation)
    remove_punct_dict = str.maketrans('','',string.punctuation+'’')

    # pnct = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    # remove_punct_dict = dict((ord(punct),None) for punct in pnct)
    # remove_punct_dict = str.maketrans('','',pnct+'’')
    
    #text = text.translate(remove_punct_dict) # remove punctuation

    #for i in range(len(text.split('\n'))):
    #    print('[ Before processing raw text ]\n',oldtext.split('\n')[i])
    #    print('[ After processing ]\n',text.split('\n')[i],'\n')
 
    return text



# Read html-content for Morphological Analysis.
content = read_content(path)

# Retrieve text from html-content.
text = retrieve_text(content)

# Pre-processing raw text for normalize.
text = pre_process_raw_text(text)

# temp_file = os.path.join(os.path.dirname(__file__),'chk_temp_text.txt')
# with open(temp_file,mode='w',encoding='utf_8') as fw:
#     fw.write(text)

# Tokenization of the text.
tokens = word_tokenize(text) # convert to list of words

# # Normalize tokens by Lemmatization
lemmatizer = WordNetLemmatizer()
lemma = [lemmatizer.lemmatize(token) for token in tokens]
for i in range(len(tokens)):
    print(tokens[i],' => ', lemma[i])


# ----------
# Tokenization
# ---------
# sent_tokens = sent_tokenize(text) # convert to list of sentences
#for s in sent_tokens: print('[ After tokenization for sentence ]\n',s,'\n')


'''
for sent in sent_tokens:
    sent_rm_punct = sent.translate(remove_punct_dict)
    lemma = [lemmatizer.lemmatize(token) for token in word_tokenize(sent_rm_punct)]
    print(sent)
    print(lemma)

'''
print('Good Job!!!')

# Variable of 'text' is used for Morphological Analysis.
