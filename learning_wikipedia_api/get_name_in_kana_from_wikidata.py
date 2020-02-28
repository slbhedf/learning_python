# -*- coding: utf-8 -*-
"""
get name in kana, and date of birth from https://www.wikidata.org

I used Wikidata API.

Wikibase/API - MediaWiki
https://www.mediawiki.org/wiki/Wikibase/API

For example:
https://www.wikidata.org/w/api.php?action=wbgetentities&sites=jawiki&titles=久間田琳加&languages=ja

"""

import requests

s = requests.Session()
wikidata_api = "https://www.wikidata.org/w/api.php"
titles = '久間田琳加|田鍋梨々花'

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
    
    try:
        name = data['entities'][id]["labels"]['ja']['value']
        yomi = data['entities'][id]["claims"]["P1814"][0]["mainsnak"]["datavalue"]["value"]
        birth = data['entities'][id]["claims"]["P569"][0]["mainsnak"]["datavalue"]["value"]["time"]
        birth = birth[1:11] # yyyy-mm-dd
    except:
        pass
        
    print(name + "," + yomi + "," + birth)

