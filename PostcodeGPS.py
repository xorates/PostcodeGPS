#PostcodeGPS v1.0 (c) Xorates (https://github.com/xorates) 2017 All rights reserved - Created 18/10/2017

import requests;

r=requests.post("http://wheredoivote.co.uk/api/beta/postcode/"+str(input("Enter postcode here: ")).replace(" ","")+".json").json();

lat,long=r["postcode_location"]["geometry"]["coordinates"];
print("{0}{1},{2}".format("https://www.google.com/maps/search/?api=1&query=",long,lat));

input();
