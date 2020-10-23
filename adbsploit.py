# -*- coding: utf-8 -*-
'''
Authors: Iqbalmh18
Project: Adbspooit
Version: 1.0
'''
from init.__init__ import *

def listener():
    exploit.session()
    while True:
        try:
            dog = input.prompt(input_listener, auto_suggest=AutoSuggestFromHistory(), style=style_listener, completer=WordExp)
            if dog == "exit" or dog == "back":
                main()
            elif dog == "?" or dog == "help":
                exploit.help(0)
            elif dog == "clear":
                os.system("clear")
            elif "sysinfo" in dog:
                exploit.sys_info()
            elif "shell" in dog:
                exploit.shell()
            elif "screencap" in dog:
                exploit.screencap()
            elif "screenrec" in dog:
                exploit.screenrec()
            elif "root" in dog:
                exploit.root()
            elif "downloads" in dog:
                load = dog.split()
                if len(load) == 5:
                    if load[1] == "-f" or load[1] == "--file" and load[3] == "-o" or load[3] == "--output":
                        file = load[2]
                        out = load[4]
                        exploit.download("file",file,out)
                    elif load[1] == "-d" or load[1] == "--dir" and load[3] == "-o" or load[3] == "--output":
                        path = load[2]
                        out = load[4]
                        exploit.download("file",path,out)
                    else:
                        exploit.help(3)
                else:
                    exploit.help(3)
            elif "app" in dog:
                apkf = dog.split()
                if len(apkf) == 3:
                    if apkf[1] == "-i" or apkf[1] == "--install":
                        apk = apkf[2]
                        if os.path.isfile(apk):
                            exploit.app_install("install",apk)
                        else:
                            print(r+"[!]"+w+" file not found")
                    elif apkf[1] == "-u" or apkf[1] == "--uninstall":
                        apk = apkf[2]
                        exploit.app_uninstall(apk)
                    elif apkf[1] == "-r" or apkf[1] == "--run":
                        apk = apkf[2]
                        exploit.app_run(apk)
                    elif apkf[1] == "-p" or apkf[1] == "--path":
                        apk = apkf[2]
                        exploit.app_path(apk)
                    elif apkf[1] == "--hide":
                        apk = apkf[2]
                        exploit.app_hide(apk)
                    elif apkf[1] == "--unhide":
                        apk = apkf[2]
                        exploit.app_unhide(apk)
                    else:
                        exploit.help(1)
                elif len(apkf) == 2:
                    if apkf[1] == "-l" or apkf[1] == "--list":
                        exploit.app_list()
                    else:
                        exploit.help(1)
                else:
                    exploit.help(1)
            elif "usekey" in dog:
                key = dog.split()
                if len(key) == 2:
                    if key[1] == "-l" or key[1] == "--list":
                        i = -1
                        print(w+"-"*32)
                        for i in range(0,86):
                            print(w+str(i)+r+")"+w+" remote code for: "+KeyList[i] )
                        print(w+"-"*32)
                    else:
                        exploit.help(2)
                elif len(key) == 3:
                    if key[1] == "-e" or key[1] == "--exec" and key[2] < 86:
                        key = int(key[2])
                        exploit.key(key)
                    else:
                        exploit.help(2)
                else:
                    exploit.help(2)
            elif "logcat" in dog:
                log = dog.split()
                if len(log) == 2:
                    if log[1] == "--start":
                        exploit.logcat()
                    else:
                        exploit.help(5)
                else:
                    exploit.help(5)
            elif "reboot" in dog:
                boot = dog.split()
                if len(boot) == 2:
                    if boot[1] == "-r" or boot[1] == "--recovery":
                        exploit.reboot(1)
                    elif boot[1] == "-b" or boot[1] == "--bootloader":
                        exploit.reboot(2)
                    else:
                        exploit.help(4)
                else:
                    exploit.help(4)
            else:
                listener()
        except KeyboardInterrupt:
            adb.stop()
            exit(r+"[!]"+w+" Aborted ...")

def main():
    os.system("clear")
    print(logo)
    print(y+"**AdbSploit**"+w+" is an exploit tool for android debug bridge")
    print(w+"type "+y+"help"+w+" or "+y+"?"+w+" if u need help.")
    print(w)
    while True:
        try:
            bal = input.prompt(input_main, auto_suggest=AutoSuggestFromHistory(), style=style_main, completer=WordAdb)
            if bal == "exit":
                exit()
            elif bal == "?" or bal == "help":
                adb.help(0)
            elif bal == "clear":
                os.system("clear")
            elif bal == "update":
                os.system("git reset --hard && git pull")
                exit(g+"[*]"+w+" source code updated")
            elif bal == "show apikey":
                apikey = open("logs/api.log","r")
                print(b+"[*]"+w+" shodan api: "+apikey.readline().strip())
            elif "shodan init" in bal:
                api = bal.split()
                if len(api) == 3:
                    adb.shodan_init(api[2])
                else:
                    adb.help(1)
            elif "shodan search" in bal:
                src = bal.split()
                if len(src) == 3:
                    if src[2].isnumeric():
                        adb.shodan_search(src[2])
                    else:
                        adb.help(2)
                else:
                    adb.help(2)
            elif "connect" in bal:
                con = bal.split()
                if len(con) == 3:
                    if con[1] == "-s" or con[1] == "--serialno":
                        adb.connect(con[2])
                    elif con[1] == "-f" or con[1] == "--fromfile":
                        adb.connect_all(con[2],debug=True)
                    else:
                        adb.help(5)
                else:
                    adb.help(5)
            elif "disconnect" in bal:
                adb.disconnect()
            elif "tcpip" in bal:
                tcp = bal.split()
                if len(tcp) == 4:
                    if tcp[1] == "-e" or tcp[1] == "--emulator" and tcp[3] == "-p" or tcp[3] == "--port":
                        dvc = tcp[2]
                        port = tcp[4]
                        adb.tcpip(dvc,port)
                    else:
                        adb.help(7)
                else:
                    adb.help(7)
            elif "show devices" in bal:
                os.system("adb devices | sed -e 's/List of devices attached/\--------------------------------/g;s/device/online/g;' | awk '!NF{$0="+'"--------------------------------"'+"}1'")
            elif "exploit" in bal:
                exp = bal.split()
                if len(exp) == 3:
                    if exp[1] == "-s" or exp[1] == "--serialno":
                        exploit.devices(exp[2])
                        listener()
                    elif exp[1] == "-a" or exp[1] == "--all" and exp[2] == "get_contact":
                        adb.get_contact_all()
                    else:
                        adb.help(6)
                else:
                    adb.help(6)
            else:
                pass
        except FileNotFoundError:
            print(r+"[!]"+w+" file not found")
        except KeyboardInterrupt:
            adb.stop()
            exit(r+"[!]"+w+" Aborted ...")

if "__main__" == __name__:
    adb.start()
    os.system("clear;rm -rf adb.json.gz logs/online.log logs/offline.log logs/cache.log logs/get_contact_all.log logs/get_contact_all.txt logs/address.log logs/session.log")
    main()