import os
import time
import requests
import json
import argparse

# TIP Certificate Portal API
cert_url = "https://tipcertificates.keys.tip.build:16061/api/v1"

#
# Update the redirector for the the AP
#
def update_redirector(url, serial, redirector, token={}):
    print("Update Redirector Value...")
    header = {
    "X-API-KEY": os.environ['CERT_API_KEY'],
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = {
    "redirector": redirector
    }
    response = requests.put(url+"/certificate/"+serial, headers=header, data=json.dumps(payload))
    data = json.loads(response.text)
    print ("URL:", response.request.url, " ", response.status_code)
    if response.status_code == 200:
       return
    print ("URL:", response.request.url)
    print ("Headers:", response.request.headers)
    print ("Payload:", response.request.body)
    print ("Response Payload:", data)


parser = argparse.ArgumentParser()
parser.add_argument('-r', type=str, help='change the redirector of this AP') 
parser.add_argument('macaddr', metavar='N', type=str, help='mac address of the AP to operate on') 
args = parser.parse_args()

update_redirector(cert_url, args.macaddr, args.r)
