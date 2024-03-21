#!/usr/bin/env python
# coding: utf-8

# In[60]:


#Task is to find which tokens from the sentence has higher score
#Tokens belong to which POS?


# In[1]:


import pandas as pd


# In[4]:


df=pd.read_csv("974_sentences.csv")


# In[5]:


df.head(4)


# In[7]:


df=df[['explicit_sentence_with_no_stopwords','scores']]


# In[8]:


df.head()


# In[12]:


def combine_words_and_scores(row):
    words = row['explicit_sentence_with_no_stopwords'].split()
    scores = row['scores'].split()
    combined = list(zip(words, scores))
    return combined

df['combined'] = df.apply(combine_words_and_scores, axis=1)


# In[13]:


df


# In[14]:


for index, row in df.iterrows():
    print(row['combined'])


# In[17]:


df=pd.read_csv("974_sentences.csv")


# In[18]:


df


# In[19]:


import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")

def pos_tagging(sentence):
    doc = nlp(sentence)
    pos_tags = [(token.text, token.pos_) for token in doc]
    return pos_tags

df['POS_tags_spaCy'] = df['explicit_sentence_with_no_stopwords'].apply(pos_tagging)


# In[20]:


df


# In[27]:


def combine_words_and_scores(row):
    words = row['POS_tags_spaCy']
    scores = row['scores'].split()
    combined = list(zip(words, scores))
    return combined

df['combined'] = df.apply(combine_words_and_scores, axis=1)


# In[25]:


df


# In[33]:


df['combined'][0:5]


# In[30]:


#df.to_csv("exp_sen_pos_impscores.csv", header=True)


# In[34]:


df['combined'][0]


# In[38]:


import pandas as pd


# In[61]:


#Edited the sheet in excel to maintain everything all rows are in one single format


# In[44]:


df=pd.read_csv("exp_sen_pos_impscores.csv")


# In[45]:


df


# In[54]:


df['combined_list'][0]


# In[51]:


combined_list = ast.literal_eval(df['combined_list'][0])

max_score = -float('inf')
max_tuple = None
for item in combined_list:
    score = float(item[1].rstrip(','))
    if score > max_score:
        max_score = score
        max_tuple = item[0]

print("Tuple with the highest score:", max_tuple)


# In[52]:


max_scores = [-float('inf'), -float('inf')]
max_tuples = [None, None]

for item in combined_list:
    score = float(item[1].rstrip(','))
    if score > max_scores[0]:
        max_scores = [score, max_scores[0]]
        max_tuples = [item[0], max_tuples[0]]
    elif score > max_scores[1]:
        max_scores[1] = score
        max_tuples[1] = item[0]

print("Top two tuples with the highest scores:")
for i in range(2):
    print("Tuple:", max_tuples[i], "Score:", max_scores[i])


# In[55]:


import ast

top_two_max_scores = []
top_two_max_tuples = []

for index, row in df.iterrows():
    try:
        combined_list = ast.literal_eval(row['combined_list'])
        
        max_scores = [-float('inf'), -float('inf')]
        max_tuples = [None, None]
        
        for item in combined_list:
            score = float(item[1].rstrip(','))
            if score > max_scores[0]:
                max_scores = [score, max_scores[0]]
                max_tuples = [item[0], max_tuples[0]]
            elif score > max_scores[1]:
                max_scores[1] = score
                max_tuples[1] = item[0]
        
        top_two_max_scores.append(max_scores)
        top_two_max_tuples.append(max_tuples)
    except (SyntaxError, ValueError):
        top_two_max_scores.append([None, None])
        top_two_max_tuples.append([None, None])

df['top_two_max_scores'] = top_two_max_scores
df['top_two_max_tuples'] = top_two_max_tuples


# In[56]:


df


# In[59]:


df.to_csv("max_scores_max_pos_exp_sen.csv", header= True)


# In[ ]:




