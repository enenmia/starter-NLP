#!/usr/bin/env python
# coding: utf-8

# In[3]:


#noise removal#
import re
text='<head>Full stack developers must also often have enough configuration and administration skills to operate their application, for example, in the cloud.The courses will introduce you to modern JavaScript-based web development and you will learn to use various tools.</head> '
text_no_noise=re.sub(r'<.?head>','',text)#r is outside ''
text_no_noise


# In[7]:


#lowercasting
text_lower=text_no_noise.lower()
text_lower


# In[8]:


#tokenization#
import nltk
from nltk.tokenize import word_tokenize

tokenized_by_word=word_tokenize(text_lower)
tokenized_by_word


# In[15]:


#stop word
from nltk.corpus import stopwords
stop_words=set(stopwords.words('english'))
text_no_stopwords=[word for word in tokenized_by_word if word not in stop_words]
text_no_stopwords


# In[16]:


#choice1:stemming
from nltk.stem import PorterStemmer
stemmer=PorterStemmer()

stemmed_text=[stemmer.stem(token) for token in text_no_stopwords]
stemmed_text


# In[21]:


#choice2:lemmatization(with get-part-of-speech)
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from collections import Counter

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

lemmatizer=WordNetLemmatizer()
lemmatized_pos=[lemmatizer.lemmatize(token,get_part_of_speech(token))for token in text_no_stopwords]
lemmatized_pos

