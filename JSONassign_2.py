import urllib.error, urllib.request, urllib.parse
import ssl
import json

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parameters = dict()
    parameters['address'] = address
    parameters['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parameters)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    print(f'Place ID: {js["results"][0]["place_id"]}')
    another = input('Do you want to do another? Enter Y for yes or X for no. :')
    if another == 'Y': continue
    if another == 'N': print("Have a good day...")
    break

    #print(json.dumps(js, indent=4))


