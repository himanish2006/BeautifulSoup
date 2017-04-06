
# coding: utf-8

# In[18]:

#Using Beautiful soup
from bs4 import BeautifulSoup
from urllib.request import urlopen


# In[19]:

quote_page = 'http://www.bloomberg.com/quote/SPX:IND'  


# In[23]:

page = urllib.request.urlopen(quote_page)  


# In[24]:

soup = BeautifulSoup(page, 'html.parser')  


# In[25]:

soup

