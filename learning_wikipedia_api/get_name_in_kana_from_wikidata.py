# -*- coding: utf-8 -*-
"""
get name in kana and date of birth from https://www.wikidata.org
I used Wikidata API.

Wikibase/API - MediaWiki
https://www.mediawiki.org/wiki/Wikibase/API

Shinzō Abe - Wikidata
https://www.wikidata.org/wiki/Q132345


For example:
https://www.wikidata.org/w/api.php?action=wbgetentities&sites=jawiki&titles=安倍晋三&languages=ja
"""

import requests

s = requests.Session()
wikidata_api = "https://www.wikidata.org/w/api.php"
titles = '安倍晋三|野田佳彦|菅直人|鳩山由紀夫|麻生太郎'

params = {
    "action": "wbgetentities",
    "sites": "jawiki",
    "titles": titles,
    "languages": "ja",
    "format": "json"
}

result = s.get(url = wikidata_api, params=params)
data = result.json()

for id in data['entities'].keys():
    name = ""
    yomi = ""
    birth = ""
    
    kana_ID = "P1814" # https://www.wikidata.org/wiki/Property:P1814
    date_of_birth_ID = "P569" # https://www.wikidata.org/wiki/Property:P569

    try:
        name = data['entities'][id]["labels"]['ja']['value']
        yomi = data['entities'][id]["claims"][kana_ID][0]["mainsnak"]["datavalue"]["value"]
        birth = data['entities'][id]["claims"][date_of_birth_ID][0]["mainsnak"]["datavalue"]["value"]["time"]
        birth = birth[1:11] # yyyy-mm-dd
    except:
        pass
        
    print(name + "," + yomi + "," + birth)