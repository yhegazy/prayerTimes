#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import re
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('headless')
options.add_argument('--no-sandbox')

browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
browser.get('https://www.islamicfinder.org/world/united-states/5150529/cleveland-prayer-times/')

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

master_data = []
prayerTable = soup.find_all("table", {"class" : "table table-pt"})

for prayer in prayerTable:
    data_dict = {}
    tBody = prayer.find('tbody')
        
    trActive = tBody.find("tr", {"class": "tr-active"})
    data_dict['rows'] = trActive.text 
    data_dict['header'] = prayer.find('').text.strip()
        
    master_data.append(data_dict)

df = pd.DataFrame(master_data)
df.to_json('dailyPrayerTimes.json')


# In[ ]:




