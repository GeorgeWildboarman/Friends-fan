# -*- coding: utf-8 -*-

import re,string,os
from bs4 import BeautifulSoup
import chardet

def read_content(path):
    '''
    Read file downloaded from the wave site.
    path : file path
    '''
    # Read html file as binary data.
    with open(path,'rb') as f:
        raw_data = f.read()
    # Detect charactor code.
    # encode_dict.detect gives a dict of coding data including char code.
    # The key for char code is 'encoding'.
    encode_dict = chardet.detect(raw_data)
    # print(encode_dict['encoding'])
    # Decode to text data.
    content = raw_data.decode(encoding=encode_dict['encoding'])
    return content

def retrieve_text(content):
    '''
    Analys wiht BeautifulSoup.
    And retriev necessay text from html-content.
    I need text about lines for the convasation.
    content : content with html tags
    '''

    # Remove tags that interfere with an analysis of BeauttifulSoup.
    # Some of the html-contents downloaded here are defective.
    # For instans </b> tags don't have the corresponding tab in some cases.
    content = content.replace('<b>','').replace('</b>','')
    content = content.replace('<i>','').replace('</i>','')
    content = content.replace('<o:p>','').replace('</o:p>','')

    # BeautifulSoup Analysis of html-content
    soup = BeautifulSoup(content,'html.parser')
    
    ptags = soup.find_all('p')
    
    text = '' # Text Retrieved from html-content
    for ptag in ptags:
        for x in ptag.contents:
            if getattr(x,'string')!=None:
                result = re.sub(r'\n+?',r' ',x.string)
                text += result
            if getattr(x,'name')=='br':
                text += '\n'
        text += '\n'

    return text

def pre_process_raw_text(rawtext):
    '''
    Pre-process the raw text.
    The text contains numbers, special characters, and others noise.
    In this process I remove charactors that can interfere with text analysis.
    '''
    text = ''
    # Remove excess lines and new line charactors
    pattern = r'.+\s*:' #ex. "Rachel:"
    for i,t in enumerate(rawtext.split('\n')[6:-6]):
        if re.search(pattern,t) and i!=0:
            text += '\n'+t
        else:
            text += t

    oldtext = text

    # Convert to lowercase
    text = text.lower()

    # Remove parenthesized and bracketed
    # Pattern for sentences enclosed in parentheses and curly bracket.
    # pattern = r'(\(|\{|\[).+?(\)|\}|\])'
    pattern = r'\(.+?\)|\{.+?\}|\[.+?\]'
    text = re.sub(pattern,'',text)

    # Remove or substitude characters that can interfere with text analysis.
    pattern = r'(—|-|…|\.{3,})+?'
    # pattern = r'(—|-|…)+?'
    text = re.sub(pattern,' ',text) # replace whit singl space
    pattern = r'(“|”|»)+?'
    text = re.sub(pattern,'',text) # remove

    # Remove 'xxxxxxx:'
    # Exp.
    # "Chandler: That's what our friends call us." into " That's what our friends call us."
    # pattern = r'\S+\s*:'
    pattern = r'.*:'
    text = re.sub(pattern,'',text)

    ### Process for converting contraction into full form ###
    text = text.replace(r"'",r"’")
    # Read contraction list
    filename='list_of_contractions.txt'
    path = os.path.join(os.path.dirname(__file__),filename)
    # path = os.path.join('d:/gitsandbox/friends-fan',filename)
    with open(path,mode='r',encoding='utf_8') as f:
        contra_list = [l.strip().split(',') for l in f.readlines()]
    # Make dict of contraction
    contra_dict = dict(contra_list)
    # Convert contraction into full form
    for k, v in contra_dict.items():
        pattern = re.compile(re.escape(k),re.IGNORECASE)
        text = pattern.sub(v,text)

    ### Process for removing punctuation ###

    # Panctuation characters defined in string module is:
    # string.punctuation
    # String of ASCII characters which are considered punctuation characters:
    # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.
    
    # The string methode of str.maketrans() returns a translation table usable for str.translate().
    # The third argument is a string, whose characters will be mapped to None in the result.
    punct_table = str.maketrans('','',string.punctuation)
    # The result is the same as below:
    # punct_table = dict((ord(c),None) for c in string.punctuation)
    
    # str.translate() returns a copy of the str in which each charactors are mapped through the given translation table.
    text = text.translate(punct_table) 
   
    # Substitute multiple spaces with singl space.
    pattern = r'\ +'
    text = re.sub(pattern,' ',text)

    # Remove excess new line charactor
    pattern = r'((\n|\r|\n\r)+\s*)'
    # pattern = r'(\n+)'
    text = re.sub(pattern,r'\n',text)

    return text


# Get list of content paths. 
content_dir = '.scripts'
startpath = os.getcwd()
dir_path = ''
path_list = []
for root, dirs, files in os.walk(startpath, topdown=True):
    if os.path.basename(root) == content_dir:
        path_list.extend(os.path.join(root,f)for f in files)
        print('HTML content dir path: {}'.format(root))
        break

# Make dir to store text data in it.
dir_name_for_txt = '.txt_data'
dir_path_for_txt = os.path.join(os.path.dirname(__file__),dir_name_for_txt)
if not os.path.isdir(dir_path_for_txt):
    print('Created new directory: ',dir_path_for_txt)
    os.makedirs(dir_path_for_txt, exist_ok=True)
else:
    print('Directory of \"{}\" already exits.'.format(dir_path_for_txt))

for path in path_list:
    print(f'Now open the file: {path}')

    # Read html-content for Morphological Analysis.
    content = read_content(path)

    # # Retrieve text from html-content.
    text = retrieve_text(content)

    # # Pre-processing raw text for normalize.
    text = pre_process_raw_text(text)

    filename = os.path.splitext(os.path.basename(path))[0]+'.txt'
    path_for_txt = os.path.join(dir_path_for_txt,filename)
    print(f'Write to the file: {path_for_txt}')
    with open(path_for_txt,mode='w',encoding='utf_8') as f:
        f.write(text)


print('Good Job!!!')
