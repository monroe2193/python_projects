import json
import urllib.request,urllib.parse, urllib.error

url = input("Enter address:")
handle = urllib.request.urlopen(url)
print('Retrieving', url)
stringdata = handle.read().decode()
print('Retrieved:', len(stringdata), 'characters')
info = json.loads(stringdata)

sum = 0
count = 0
for num in info['comments']:
    sum = sum + float(num['count'])
    count = count + 1

print(f'Count: {count}')
print(f'The sum {sum}')
