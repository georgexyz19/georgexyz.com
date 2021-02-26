title: Python Code To Check If A Product Is In Stock
slug: check-product-in-stock
date: 2021-02-26 10:35
modified: 2021-02-26 10:35
tags: python
note: chapter 12 of Al Sweigart' book
no: 68

I am reading 
[Chapter 13](https://automatetheboringstuff.com/2e/chapter13/) of Al Sweigart's 
*Automate The Boring Stuff With Python 2nd ed* book for some spreadsheet work. 
The [Chapter 12](https://automatetheboringstuff.com/2e/chapter12/) *Web Scraping* 
is also very interesting. 

The first example in *Web Scraping* Chapter is to search Pypi website for 
python packages and open the search results on new browser tabs.  It is 
easy to revise the program a little to check if a product is *in stock* or 
*out of stock*.  

Here is a python script modified from the example.  The script will check 
if a Ryobi Sander is in stock on *direct tools outlet* website. 

```
#!python3

#ryobiSander.py - Opens ryobi sander page on directtoolsoutlet page

import requests, webbrowser, bs4

print('Searching...')
url = 'https://www.directtoolsoutlet.com/Products/' + 
      'Power-Tools/Finishing-Tools/Sanders/' + 
      'RYOBI-ONE%2B-18-Volt-5-In-Random-Orbit-Sander/p/P411'
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
buttonElem = soup.select('.js-add-to-cart')
if buttonElem[0].get('disabled') == 'disabled':
    print('The button is disabled')
else:
    print('Opening ', url)
    webbrowser.open(url)

```

I have some other ideas to add to this program:

- Add code to run the check every 1 hour or other time interval. 
- Find a way to click the *Add To Cart* button if it is enabled
- Send an email or text message to remind that it is in stock

The code does not look complicated.  The program shapes up to 
be a ticket scalping tool, and I stop the post right here. 