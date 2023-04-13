#Retriveing web pages
#urllib is a library that does the socket work for us
#requesting encoding sending, recieving, decoding, and opening a page using python
import ssl
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

#using this url open you can handle data on the internet like you have
#been doing on txt files in previous assignments, handle them just like an open() statement

import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    #decode takes the bytes string and turns it into a unicode character string
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

#spidering the web or crawling the web
#SCRAPING
#Why?
# to pull data, specifically social data
#get data back out of a sytem that has no export capabilities
#moniter a site for new informationi
#spider the web to make a database for a search engine
#beautiful soup library

import re
from bs4 import BeautifulSoup
import ssl
#ignore
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#context=ctx
url = input("Enter-")
#read() puts the whole document into one big string
html = urllib.request.urlopen(url).read()
#then tell beautiful soup to parse it
# takes the whole file html and uses html.parser, to clean it up and organize
soup = BeautifulSoup(html, 'html.parser')
#now we can ask questions of beautiful soup
#retrieve all the anchor tags
tags = soup('span')
lst = list()
print(tags)
count = 0
for tag in tags:
    lst.append(tag.contents[0])
    count = count + 1
print(lst)
sum = sum(lst)
print('The count', count)
Print('The average', sum/count)
#for tag in tags:
 #   tag.get('href', None)
  #  # tag.get() #is like a dictionary and tallys the anchor tags in a list

#lst =
#for i in range(len(tags)):
 #      lst[i] = re.findall("[0-9]+", 'tags[i]')

#print(lst)


