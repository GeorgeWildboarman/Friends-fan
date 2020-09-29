# Build ChatBot to talk with 'Friends'


## Introduction 


Hello!!!


I just started learning Python by myself, so I'm still a beginner.


Now I'm trying to build a chatbot with Python3 to have a fun. 
It will help to improve my skills, although it will take me a very long time to complete.


Give it a try!


My goal is to make a simple chatbot that talks as if it were one of 'Friends'. 
Because I am a fan of 'Friends', popular American television sitcom.


All the resources of the scripts of 'Friends' are provided by Crazy For Friends.

Resource website URL: http://www.livesinabox.com/friends/scripts.shtml


## 1. Crawl and Scrape

[grab-webcontents.py](grab-webcontents.py)
- Get the contents of the scripts from [the resource site](http://www.livesinabox.com/friends/scripts.shtml). 
- Store them in a local directory assigned by an argument.
 

Usage: python3 grab-webcontents.py [dir_path=.scripts] 
dir_path is direcory path and default is '.scripts'.


```bash
python3 grab-webcontents.py .scripts
```



## 2. Natural Language Processing with Tensorflow

### Installation of Tensorflow from Anaconda
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

 



## Conclusion


Bye,bye!
