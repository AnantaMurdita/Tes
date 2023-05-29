import requests,json,os,time
from requests import post
from requests import get

#system
time.sleep (1)
os.system ("clear")
banner = """\t_______________________________________
\t dP"Yb  88 8888b.    .d   dP"Yb  .dP"o. 
\tdP   Yb 88 8I   Yb .d88  dP   Yb `8b.d' 
\tYb   dP 88 8I   dY   88  Yb   dP d'`Y8b 
\t YbodP  88 8888Y"    88   YbodP  `bodP' 
\t_______________________________________
\t       Spam WhatsApp No Brutall
\t======================================="""
print (banner)
time.sleep (1)
banner = """==================================================
[+] Author  : OID108 / Mr.DOY108               [+]
[+] Team    : DOY X-PUNTEN                     [+]
[+]           Solo Timur Cyber Team            [+]
[+] Youtube : OID108                           [+]
[+] Github  : https://github.com/oranginisiald [+]
=================================================="""
print (banner)
time.sleep (2)

nomer = input("Nomer :")
jumlah = int(input("Jumlah :"))

#ini headers
headers = {

}

#Ini Data
data_segari = json.dumps({Input Your Data Website})

#ini Perintah

for k in range(jumlah):

  pos = requests.post("Input your url website",headers=header,data=data).text

  if "Send successfully" in pos:

    print("Spam WhatsApp Berhasil")

  else:

    print("Spam WhatsApp Berhasil")
