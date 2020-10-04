#!/usr/bin/env python
# coding: utf-8

# In[4]:


from gtts import gTTS
eng = "Hello, I welcome you to my birthday celebration. We all will enjoy the day.Thank you."
obj = gTTS(text = eng, slow = False, lang = 'en')
obj.save('English.mp3')


Hindi = "हैलो, मैं आप सभी को मेरे जन्मदिन के जश्न में स्वागत करता हूं। हम सभी दिन का आनंद लेंगे। धन्यवाद।"
obj = gTTS(text = Hindi, slow = False, lang = 'hi')
obj.save('Hindi.mp3')


# In[ ]:





# In[ ]:




