#!/usr/bin/env python
# coding: utf-8

# In[1]:


##########noise removal#########
import re

headline_one = '<h1>Nation\'s Top Pseudoscientists Harness High-Energy Quartz Crystal Capable Of Reversing Effects Of Being Gemini</h1>'

tweet = '@fat_meats, veggies are better than you think.'


headline_no_tag=re.sub(r'<.?h1>','',headline_one)

tweet_no_at=re.sub('@','',tweet)



try:
    print(headline_no_tag)
except:
    print('No variable called `headline_no_tag`')
try:
    print(tweet_no_at)
except:
    print('No variable called `tweet_no_at`')


# In[4]:


##########tokenization#########
import nltk
nltk.download('punkt')
  
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
ecg_text = 'An electrocardiogram is used to record the electrical conduction through a person\'s heart. The readings can be used to diagnose cardiac arrhythmias.'

tokenized_by_sentence=sent_tokenize(ecg_text)
tokenized_by_word=word_tokenize(ecg_text)







try:
    print('Word Tokenization:')
    print(tokenized_by_word)
except:
    print('Expected a variable called `tokenized_by_word`')
try:
    print('Sentence Tokenization:')
    print(tokenized_by_sentence)
except:
    print('Expected a variable called `tokenized_by_sentence`')


# In[5]:


##########normalization-upper or lowercasting#########
brands = 'Salvation Army, YMCA, Boys & Girls Club of America'

brands_lower=brands.lower()
brands_upper=brands.upper()


try:
    print(f'Lowercased brands: {brands_lower}')
except:
    print('Expected a variable called `brands_lower`')
try:
    print(f'Uppercased brands: {brands_upper}')
except:
    print('Expected a variable called `brands_upper`')


# In[9]:


##########normalization-stopword removal#########
import nltk
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

survey_text = 'A YouGov study found that American\'s like Italian food more than any other country\'s cuisine.'
stop_words=set(stopwords.words('english'))

#tokenize survey_text
tokenized_survey=word_tokenize(survey_text)

#remove stop words
text_no_stops=[word for word in tokenized_survey if word not in stop_words]


try:
    print(f'Stopwords type: {type(stop_words)}')
except:
    print('Expected a variable called `stop_words`')
try:
    print(f'Words Tokenized: {tokenized_survey}')
except:
    print('Expected a variable called `tokenized_survey`')
try:
    print(f'Text without Stops: {text_no_stops}')
except:
    print('Expected a variable called `text_no_stops`')
  


# In[10]:


##########normalization-stemming(remove pre/suffixes)#########
from nltk.tokenize import word_tokenize, sent_tokenize

#import and initialize stemmer
from nltk.stem import PorterStemmer
stemmer=PorterStemmer()

#raw text
populated_island = 'Java is an Indonesian island in the Pacific Ocean. It is the most populated island in the world, with over 140 million people.'

#tokenize populated_island
island_tokenized=word_tokenize(populated_island)

#to stem tokenized text
stemmed=[stemmer.stem(token) for token in island_tokenized]







try:
    print('A stemmer exists:')
    print(stemmer)
except:
    print('Expected a variable called `stemmer`')
try:
    print('Words Tokenized:')
    print(island_tokenized)
except:
    print('Expected a variable called `island_tokenized`')
try:
    print('Stemmed Words:')
    print(stemmed)
except:
    print('Expected a variable called `stemmed`')
  


# In[ ]:




