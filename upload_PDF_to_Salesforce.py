import requests
import os
from ftplib import FTP
import json
import base64

###LOGIN AND GET A SESSION ID
data = {
                'grant_type': 'password',
                'client_id': '<INSERT_HERE>',
                'client_secret': '<INSERT_HERE>',
                'username': '<INSERT_HERE>',
                'password': '<INSERT_HERE_USERNAME_AND_TOKEN>'
        }

r = requests.post('https://test.salesforce.com/services/oauth2/token', data=data)
response = r.json()
sessionId = response['access_token']
instance = response['instance_url']

##print ('sessionId: ' + sessionId)
##print ('instance: ' + instance)

###CREATE AN ACCOUNT
data2 = {
            'Name': 'test integration'
        }

hdr = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + sessionId
    }

payload = json.dumps(data2)

r2 = requests.post(instance + '/services/data/v43.0/sobjects/Account', headers = hdr, data=payload)
##print(r2.text)

response2 = r2.json()

##print(response2)

accountId = response2['id']

print(accountId)

####OPEN A FILE, CONVERT TO BASE 64 and UPLOAD

f = open('Output.PDF', 'rb')
file_content = f.read()
b64 = base64.b64encode(file_content).decode("utf-8")


print(file_content)

print(b64)

data3 = {
                'ParentId': accountId,
                'Name': 'test.pdf',
                'body': b64
        }

payload2 = json.dumps(data3)



r3 = requests.post(instance + '/services/data/v43.0/sobjects/Attachment', headers = hdr, data=payload2)
print(r3.text)
