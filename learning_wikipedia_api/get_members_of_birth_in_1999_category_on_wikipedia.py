'''
get members of birth in 1999 Category on Wikipedia.
In this case, the members are names of people born in 1999.

I used wikipedia API.
Here is the detail.

API:Categorymembers - MediaWiki
https://www.mediawiki.org/wiki/API:Categorymembers 

'''

import requests

s = requests.Session()
wikipedia_ja = "https://ja.wikipedia.org/w/api.php"

params = {
    "cmdir": "ascending",
    "format": "json",
    "list": "categorymembers",
    "action": "query",
    "cmtitle": "Category:1999年生",
    "cmsort": "sortkey",
    "cmlimit": 500,
}

pages = [] # list of dictionaries

while(True):
    result = s.get(url = wikipedia_ja, params=params)
    data = result.json()
    pages += data["query"]["categorymembers"]
    
    # continue when more results are available
    if data.get('continue'):
        params['cmcontinue'] = data['continue']['cmcontinue']
        params['continue'] = data['continue']['continue']
    else: # finish when there are no more result 
        break
        
# print results    
for page in pages:
    print(page['title'], end=", ")
print()
    