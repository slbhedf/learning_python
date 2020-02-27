# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 20:44:00 2020

if you have not installed pywikibot, please install it.

$ pip install pywikibot

Manual:Pywikibot - MediaWiki
https://www.mediawiki.org/wiki/Manual:Pywikibot

Put user-config.py in the same directory.

### my user-confing.py
family = 'wikipedia'
mylang = 'ja'
usernames['wikipedia']['ja'] = u'YOUR USERNAME'

"""

import pywikibot

site = pywikibot.Site()
page = pywikibot.Page(site, u"2020年")
text = page.text
print(text) # source (wiki format text)
