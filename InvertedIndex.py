#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=open("myfile.txt","w")
a.write("he problem of document storage and retrieval has always been a major issue in Computer Science. One of the most popular techniques of information retrieval has been the use of inverted indices, the method used by most commercial indexing software companies")
a.close()


# In[5]:


from pprint import pprint as pp
from glob import glob
try: reduce
except: from functools import reduce
try:    raw_input
except: raw_input = input
 
 
def texts(fileglob='myfile.txt'):
    texts, words = {}, set()
    for txtfile in glob(fileglob):
        with open(txtfile, 'r') as f:
            txt = f.read().split()
            words |= set(txt)
            texts[txtfile.split('\\')[-1]] = txt
    return texts, words
 
def search(terms): 
    return reduce(set.intersection,
                  (invindex[term] for term in terms),
                  set(texts.keys()))
 
texts, words = texts()
print('\nTexts')
pp(texts)
print('\nWords')
pp(sorted(words))
 
invindex = {word:set(txt
                        for txt, wrds in texts.items() if word in wrds)
            for word in words}
print('\nInverted Index')
pp({k:sorted(v) for k,v in invindex.items()})
 
terms = ["retrieval","used","storage"]
print('\nTerm Search for: ' + repr(terms))
pp(sorted(search(terms)))


# In[ ]:




