import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter-")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')
lst = list()
count = 0
for tag in tags:
    lst.append(tag.contents[0])
    count = count + 1
sum = 0
for i in range(len(lst)):
    sum = sum + int(lst[i])
print('The count is', count)
print('The sum is', sum)
