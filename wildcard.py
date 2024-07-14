from requests.auth import HTTPBasicAuth
import requests
import html
import time

j  = 1 # counter to limit requests - 30 Reqs per mins~
apikey = '2a55c7f5-e807-11ed-9a5f-0242ac110002'

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



while 1:
    requestIn = input('Enter a search word like OSCP or type exit to quit: ')
    url = 'http://assignment-code-warriors.unimelb.life/api/store.php?name='+requestIn
    cookies = {'PHPSESSID': s.cookies['PHPSESSID'], 'CSRF_token' : s.cookies['CSRF_token']}
    headers = {'Accept': 'application/json', 'apikey':apikey}
    r = requests.get(url, cookies=cookies, headers=headers)
    res = r.content
    decodeRes= html.unescape(res.decode('UTF-8'))
    if(requestIn=="exit"):
        break
    print("_______ Results________\n")
    print(decodeRes)

