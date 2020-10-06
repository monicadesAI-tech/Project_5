#!/usr/bin/env python
# coding: utf-8

# In[4]:



eng = "Hello, I welcome you to my birthday celebration. We all will enjoy the day.Thank you."



import win32com.client as wincl
speak = wincl.Dispatch('SAPI.SpVoice')
speak.Speak(eng)


# In[ ]:





# In[ ]:




