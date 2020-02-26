# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26, using Spyder (Python IDE)

This is a very rough web-scraping script. 

gather names of famous japanese actresses from pages on wikipedia like xxxx年の日本#誕生(in Japanese).
make a csv file whose each row consists of a birthday and name. 

### here is an exmple.
2000年1月1日, ○○○○
......

"""

from bs4 import BeautifulSoup
import urllib.request
import re

# ????年の日本(???? in Japan)
def year_in_japan_URL(year):
    return "https://ja.wikipedia.org/wiki/" + str(year) + "%E5%B9%B4%E3%81%AE%E6%97%A5%E6%9C%AC"

def get_births_section(html):
    lines = html.split("\n") # list of strings
    births_html = "" # str
    in_birth_section = False # when in birth section, turn it True
    for line in lines:
        if 'id="誕生"' in line: # 誕生(births)
            in_birth_section = True
        elif 'id="死去"' in line : # 死去(deaths)
            in_birth_section = False
            break
        elif 'id="崩御・死去"' in line: # 崩御・死去 (deaths including emperors')
            in_birth_section = False
            break
        if in_birth_section:
            births_html += line
    return births_html 

mmdd_regex = re.compile('^\d+月\d+日')
year_from = 1990
year_until = 2000
filename = 'famous_japanese_actress_born_in_'+ str(year_from) + '-' + str(year_until-1) + '.csv'
f = open(filename, 'w', encoding='UTF-8') # set encoding for UTF-8 to avoid UnicodeEncodeError

for year in range(year_from, year_until):
    url = year_in_japan_URL(year)
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read().decode() # html source: str
    html = get_births_section(html) # html source in the birth section: str
    soup = BeautifulSoup(html, "lxml")
    
    ul_list = soup.find_all('ul')
    for ul in ul_list:
        li_list = ul('li')
        for li in li_list:
            if re.match(mmdd_regex, li.text ) and "、女優" in li.text: # li.text is a HTMLtag-removed text
                row = re.sub(r'^', str(year)+"年" , li.text)
                row = re.sub(r'、.*', "", row)
                row = re.sub(r'\s*(\-|‐)\s*', ",", row)
                f.write(row + "\n")
                print(row)
f.close()



