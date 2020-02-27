'''
get category members on Wikipedia Japanese edition.

In this test case at the bottom of this script, 
the members are names of people born in 1999.

I used Wikipedia API.
Here is the detail.
API:Categorymembers - MediaWiki
https://www.mediawiki.org/wiki/API:Categorymembers 
'''

import requests
wikipedia_ja = "https://ja.wikipedia.org/w/api.php"

# return a list of strings of pagename in a category on Wikipedia
def get_category_members(category_name, url):
    s = requests.Session()
    params = {
        "cmdir": "ascending",
        "format": "json",
        "list": "categorymembers",
        "action": "query",
        "cmtitle": category_name,
        "cmsort": "sortkey",
        "cmlimit": 500,
    }

    pages = [] # list of dictionaries
    
    while(True):
        result = s.get(url = wikipedia_ja, params=params)
        data = result.json()
        pages += data["query"]["categorymembers"] # list + list = list
        
        # continue when more results are available
        if data.get('continue'):
            params['cmcontinue'] = data['continue']['cmcontinue']
            params['continue'] = data['continue']['continue']
        else: # finish when there are no more result 
            break
    
    names = [] # list of strings
    # print results    
    for page in pages:
        names.append(page['title'])
    
    return names


##############
# test
############## 
category_name = "Category:1999年生"
persons_born_in_1999 = get_category_members(category_name, wikipedia_ja)

# print people born in 1999
for person in persons_born_in_1999:
    print(person)

#category_name = "Category:日本の女優"
#japenese_actresses = get_category_members(category_name, wikipedia_ja)

# print names in both two categories above.
# It would take 10-20 seconds to print the result. Please be patient.
#for person1 in persons_born_in_1990:
#    for person2 in japenese_actresses:
#        if person1 == person2:
#            print(person1)

