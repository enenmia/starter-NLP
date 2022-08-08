#!/usr/bin/env python
# coding: utf-8

# In[2]:


########nomalization-lemmatization(basic)########
import nltk
nltk.download('wordnet')

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer=WordNetLemmatizer()

populated_island = 'Indonesia was founded in 1945. It contains the most populated island in the world, Java, with over 140 million people.'

tokenized_string=word_tokenize(populated_island) 

#for every item in populated_island, named it as token, and do lemmarizer.lemmatize() for token
lemmatized_words=[lemmatizer.lemmatize(token) for token in tokenized_string]







try:
    print(f'A lemmatizer exists: {lemmatizer}')
except:
    print('Expected a variable called `lemmatizer`')
try:
    print(f'Words Tokenized: {tokenized_string}')
except:
    print('Expected a variable called `tokenized_string`')
try:
    print(f'Lemmatized Words: {lemmatized_words}')
except:
    print('Expected a variable called `lemmatized_words`')
  


# In[4]:


########nomalization-lemmatization(advanced, with part-of-speech tagging词性标注)########
####define get_part_of_speech####

import nltk
from nltk.corpus import wordnet
from collections import Counter

#get a set of synonyms for the word
def get_part_of_speech(word):
    probable_part_of_speech = wordnet.synsets(word)

#use synonyms to determine the most likely part of speech 
    pos_counts = Counter()

    pos_counts["n"] = len(  [ item for item in probable_part_of_speech if item.pos()=="n"]  )
    pos_counts["v"] = len(  [ item for item in probable_part_of_speech if item.pos()=="v"]  )
    pos_counts["a"] = len(  [ item for item in probable_part_of_speech if item.pos()=="a"]  )
    pos_counts["r"] = len(  [ item for item in probable_part_of_speech if item.pos()=="r"]  )

 #return the most common part of speech 
    most_likely_part_of_speech = pos_counts.most_common(1)[0][0]

#we've found the most probable part of speech for a given word.Pass this to lemmatizer when we find the root for each word...

    return most_likely_part_of_speech


# In[6]:


########nomalization-lemmatization(advanced, with part-of-speech tagging词性标注)########
####apply get_part_of_speech to lemmatization####

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
#from part_of_speech import get_part_of_speech

lemmatizer = WordNetLemmatizer()

populated_island = 'Indonesia was founded in 1945. It contains the most populated island in the world, Java, with over 140 million people.'

tokenized_string = word_tokenize(populated_island)


#we've found the most probable part of speech for a given word.Pass this to lemmatizer when we find the root for each word...
lemmatized_pos=[lemmatizer.lemmatize(token,get_part_of_speech(token)) for token in tokenized_string]


try:
    print(f'The lemmatized words are: {lemmatized_pos}')
except:
    print('Expected a variable called `lemmatized_pos`')


# In[ ]:




