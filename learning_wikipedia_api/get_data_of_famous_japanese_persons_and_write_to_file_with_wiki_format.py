# -*- coding: utf-8 -*-
'''
get data of famous japanese persons using wikidata API,
politicians, actors, athletes, and so on.
and write them into a file with wiki table format.
'''

import requests

input_file = 'famous_persons.txt' # titles separated by '\n'
output_file = 'data_of_famous_persons.txt' # write the result to this file
fin = open(input_file, 'r', encoding='utf-8')
fout = open(output_file, 'w', encoding='utf-8')

titles_list = [] # [["a","b","c","d","e","f","g","h","i","j"], ["k","l","m","n","o","p","q","r","s","t"], ...]

line_list = fin.readlines() # list of strings
lines = "".join(line_list) # string
title_list = lines.split('\n') # ['a','b','c',...]

# titles_list: list of list of 10 strings
temp_list = [] # list of some titles
for title in title_list:
    if not title == '':
        temp_list.append(title)
    if len(temp_list) >= 10:
        titles_list.append(temp_list.copy()) # add list of 10 titles to titles_list 
        temp_list.clear()
if(len(temp_list) > 0):
    titles_list.append(temp_list.copy())


wikipedia_ja = "https://ja.wikipedia.org/w/api.php"
wikidata_api = "https://www.wikidata.org/w/api.php"

kana_ID = "P1814" # https://www.wikidata.org/wiki/Property:P1814
date_of_birth_ID = "P569" # https://www.wikidata.org/wiki/Property:P569

s = requests.Session()

fout.write('{| class="sortable wikitable"\n')
fout.write('! name !! name in kana !! date of birth !! wikidata\n')
    
# get infomation on wikidata.org
for temp_list in titles_list:
    titles = "|".join(temp_list) # 10-titles string like "a|b|c|d|e|f|g|h|i|j"
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
    
