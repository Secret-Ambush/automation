#! /usr/bin/env python3

import os
import requests

dir = "/data/feedback/"
for file in os.listdir(dir): 

    format = ["title","name","date","feedback"]
    content = {}
    
    with open('{}/{}'.format(dir,file), 'r') as txtfile:
        counter = 0
        for line in txtfile:
            line = line.replace("\n", "")
            content[format[counter]] = line.strip('\n')
            counter += 1
    '''
    Use the Python requests module to post the dictionary to the company's website. 
    Use the request.post() method to make a POST request to http://<corpweb-external-IP>/feedback. 
    Replace <corpweb-external-IP> with corpweb's external IP address.
    '''
    response = requests.post("http://35.225.95.53/feedback/",json = content)

    if not response.ok:
        raise Exception("POST failed! | Status code: {} | File: {}".format(response.status_code, file))
    print("Feedback added!")
