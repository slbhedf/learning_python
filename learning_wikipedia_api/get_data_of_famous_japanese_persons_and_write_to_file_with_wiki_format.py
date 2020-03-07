# -*- coding: utf-8 -*-
'''
get data of famous japanese persons using wikidata API,
politicians, actors, athletes, and so on.
and write them into a file with wiki table format.

For exmple, this is data of 5 japanese prime miniters
https://www.wikidata.org/w/api.php?action=wbgetentities&sites=jawiki&titles=安倍晋三|野田佳彦|菅直人|鳩山由紀夫|麻生太郎&languages=ja

action=wbgetentities
https://www.wikidata.org/w/api.php?action=help&modules=wbgetentities
titles: Maximum number of values is 50 (500 for clients allowed higher limits).

'''

import requests

input_file = 'famous_persons.txt' # titles separated by '\n'
output_file = 'data_of_famous_persons.txt' # write the result to this file
fin = open(input_file, 'r', encoding='utf-8')
fout = open(output_file, 'w', encoding='utf-8')

line_list = fin.readlines() # list of strings
lines = "".join(line_list) # string
title_list = lines.split('\n') # ['a','b','c',...]

# titles_list: list of titles
titles_list = [] # ["a|b|c|d|e|f|g|h|i|j", "k|l|m|n|o|p|q|r|s|t", ...]
temp_list = [] # list of 10 titles
for title in title_list:
    if not title == '':
        temp_list.append(title)
    if len(temp_list) >= 10:
        titles = "|".join(temp_list) # titles string separated by |, like "a|b|c|d|e|f|g|h|i|j"
        titles_list.append(titles) # add titles to titles_list 
        temp_list.clear()
if(len(temp_list) > 0):
    titles = "|".join(temp_list)
    titles_list.append(titles)
    temp_list.clear()


wikipedia_ja = "https://ja.wikipedia.org/w/api.php"
wikidata_api = "https://www.wikidata.org/w/api.php"

kana_ID = "P1814" # https://www.wikidata.org/wiki/Property:P1814
date_of_birth_ID = "P569" # https://www.wikidata.org/wiki/Property:P569

s = requests.Session()

fout.write('{| class="sortable wikitable"\n')
fout.write('! name !! name in kana !! date of birth !! wikidata\n')
    
# get infomation on wikidata.org
for titles in titles_list:
    params = {
    "action": "wbgetentities",
    "sites": "jawiki",
    "titles": titles,
    "languages": "ja",
    "format": "json"
    }

    result = s.get(url=wikidata_api, params=params)
    data = result.json()
    
    for id in data['entities'].keys():
        title = ""
        yomi = ""
        birth = ""
        wikidata_url = "https://www.wikidata.org/wiki/" + id
        
        # title
        try:
            title = data['entities'][id]["sitelinks"]["jawiki"]['title']
        except:
            print(id + ": title is not found")
            print(wikidata_url + "\n")
            continue
        
        # name in kana
        try:
            yomi = data['entities'][id]["claims"][kana_ID][0]["mainsnak"]["datavalue"]["value"]
        except:
            print(title + ": name in kana is not defined")
            print(wikidata_url + "\n")
        
        # date of birth
        try:    
            birth = data['entities'][id]["claims"][date_of_birth_ID][0]["mainsnak"]["datavalue"]["value"]["time"]
            birth = birth[1:11] # yyyy-mm-dd
            if birth.endswith('01-01'):
                print(title + ": date of birth might be incorret")
                print(wikidata_url + "\n")
                birth = birth[:5] + "??-??"
            if birth.endswith('00-00'):
                print(title + ": date of birth is incorret")
                print(wikidata_url + "\n")
                birth = birth[:5] + "??-??"
        except:
            print(title + ": date of birth is not defined")
            print(wikidata_url + "\n")
            
        # xxxx (xxx) -> xxxx (xxx)|  
        if title.endswith(')') or title.endswith('）'):
            title += "|"
        
        line = "|-\n|[[" + title + "]]||" + yomi + "||" + birth + "||[" + wikidata_url + "]\n"
        fout.write(line)

fout.write('|}')
fout.close()

print("")
print("wrote to " + output_file)
    
