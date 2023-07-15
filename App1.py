#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pyautogui as pg


# In[8]:


mat_list = ["183358","83715","1997","1996"]
f = open(r"F:\gui\test_mat.txt", "r")
text_file = (f.read())


# In[9]:


text_file_replaced = text_file.replace(';',' ')


# In[10]:


text_file_split = text_file_replaced.split(" ")


# In[11]:


keys = []
for i in mat_list:
    for j in text_file_split:
        if(i==j):
            keys.append(i)
        else:
            pass


# In[12]:


keys


# In[13]:


pg.keyDown('win')
pg.keyDown('r')
pg.PAUSE = 2
pg.keyUp('r')
pg.keyUp('win')
pg.PAUSE = 2
pg.hotkey('enter')
pg.PAUSE = 2
pg.hotkey('enter')
pg.PAUSE = 2
pg.hotkey('enter')
pg.PAUSE = 2
for i in keys:
    insert_point = pg.locateCenterOnScreen('view_button.png')
    pg.click(x=insert_point[0], y=insert_point[1], clicks=1, interval=0, button='left')
    pg.PAUSE = 1
    pic_point = pg.locateCenterOnScreen('pic_button.png')
    pg.click(x=pic_point[0], y=pic_point[1], clicks=1, interval=0, button='left')
    pg.PAUSE = 2
    pg.typewrite(i)
    pg.PAUSE = 2
    pg.hotkey('enter')


# In[ ]:




