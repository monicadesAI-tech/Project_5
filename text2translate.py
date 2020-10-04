#!/usr/bin/env python
# coding: utf-8

# In[4]:


from googletrans import Translator,LANGUAGES
sample_text ="This is my house"
for language in LANGUAGES:
    t = Translator().translate(sample_text,dest=language)
    print(LANGUAGES[language] + ': ' + t.text)


# In[ ]:





# In[ ]:




