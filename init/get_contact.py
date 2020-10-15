import os
def get_contact():
    s = open("logs/online.log","r")
    while True:
        serialno = s.readline().strip()
        if not serialno:
            break
        os.system("adb -s "+serialno+" shell 'content query --uri content://contacts/phones/ --projection display_name:number_key'")
    s.close()

get_contact()
