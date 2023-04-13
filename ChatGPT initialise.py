#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install openai


# In[ ]:


#source : geeksforgeeks.org ( How to Use ChatGPT API in Python ?)
https://www.geeksforgeeks.org/how-to-use-chatgpt-api-in-python/


# In[1]:


import openai
openai.api_key = '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'
messages = [ {"role": "system", "content":
			"You are a intelligent assistant."} ]
while True:
	message = input("User : ")
	if message:
		messages.append(
			{"role": "user", "content": message},
		)
		chat = openai.ChatCompletion.create(
			model="gpt-3.5-turbo", messages=messages
		)
	reply = chat.choices[0].message.content
	print(f"ChatGPT: {reply}")
	messages.append({"role": "assistant", "content": reply})
    print(/n)


# In[ ]:


print(/n)


# In[ ]:




