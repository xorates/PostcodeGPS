#PostcodeGPS v1.0 (c) Xorates (https://github.com/xorates) 2017 All rights reserved - Created 18/10/2017 - Documented 11/09/2018

import requests; #requests is a much simpler HTTP request module

postcode=str(input("Enter postcode here: ")).replace(" ",""); #Prompts user to input their postcode. .replace(" ","") removes whitepace in inputted string
request_URL="http://wheredoivote.co.uk/api/beta/postcode/"+postcode+".json" #Inserts scrubbed postcode into URL
request_data=requests.post(request_URL).json(); #HTTP request then sent to URL location in respective string. Reply stored in varable and is JSONified.
lat,long=request_data["postcode_location"]["geometry"]["coordinates"]; #["coordinates"] is two values, which are sotred in respective variables.
print("{0}{1},{2}".format("https://www.google.com/maps/search/?api=1&query=",long,lat)); #Prints Google Maps URL for the coordinated extracted, using replacement fields string formatting for neatness.

input(); #prevents programme from closing after result is returned.

#
#
#
#
#Shortened version, without comments
import requests;

r=requests.post("http://wheredoivote.co.uk/api/beta/postcode/"+str(input("Enter postcode here: ")).replace(" ","")+".json").json();

lat,long=r["postcode_location"]["geometry"]["coordinates"];
print("{0}{1},{2}".format("https://www.google.com/maps/search/?api=1&query=",long,lat));

input();
