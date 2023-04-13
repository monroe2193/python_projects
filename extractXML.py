import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url:")
print('Retrieving:', url)
fhandle = urllib.request.urlopen(url, context=ctx).read()
print('Retrieving:', len(fhandle))
count = re.findall("\>([0-9]+)\<",str(fhandle))
#option 1
lst = list()
for num in count:
    number = int(num)
    lst.append(number)

sum = 0
for i in lst:
    sum = sum + i
print('The count is', len(lst))
print('The sum is', sum)

#Option 2
tree = ET.fromstring(fhandle)
list = tree.findall('comments/comment')
count = 0
total = 0
for tag in list:
    count = count + 1
    num = tag.find('count').text
    total = total + float(num)
print('The count is', count)
print('The sum is', total)

