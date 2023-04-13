#JSON
import json
data = '''{
   "name" : "Chuck",
   "phone" : {
      "type" : "intl",
      "number" : "+1 361 585 9305"
      },
   "email" : {
      "hide" : "yes"
      }
}'''
info = json.loads(data)
print('Name:', info["name"]) # info is a dictionary
print('Hide:', info["email"]["hide"]) #find email in the info dictionary,
# and then info[email] is also a dictionary so find hide
print('Number', info["phone"]['number'])

#list of dictionaries
input_ = '''[
   {  "id" : "007",
      "x" : "7",
      "name" : "Jorden"
   } , 
   {  "id" : "001",
      "x" : "6",
      "name" : "Danely"
   } 
]'''
info_ = json.loads(input_) # the list that contains 2 dictionaries
print('User Count:', len(info_))
for dic in info_:
    print("Id:", dic["id"])
    print("X:", dic["x"])
    print("Name:", dic["name"])

#JSON represents data as nested lists and dictionaries

#service oriented approach to data sharing
#sharing data between applications is a well established principle
#
#APPLICANTION PROGRaMMING INTERFACES (API)
#specification for the url patterns and the specifications of the data were going to get back
#producer of api defines api exports data
#consumer reads documentation of api creates code follows the rules of the api
#more common to be the consumer
#Geoprogramming -

import urllib.parse, urllib.request, urllib.error
import json


service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter Location:')
    if len(address)<1:
        break

    addy = {'address':address }
    url = service_url + urllib.parse.urlencode(addy)
    print('Retrieving', url)

    fhandle = urllib.request.urlopen(url)
    data = fhandle.read().decode()
    print('Received', len(data), 'characters')

    try:
        js = jason.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print("===Failure to retrieve===", data)
        continue
    print(json.dumps(js, indent=4))



    results = tree.findall('result')
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['resuls'][0]['geometry']['location']['lng']

    print('lat', lat, 'lng', lng)
    print(location)

#API requests
