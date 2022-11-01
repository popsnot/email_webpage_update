import time
import hashlib
from urllib.request import urlopen, Request
import win32com.client
 
outlook = win32com.client.Dispatch('outlook.application')
url = Request('your webpage here',
              headers={'User-Agent': 'Mozilla/5.0'})
 
response = urlopen(url).read()
 
currentHash = hashlib.sha224(response).hexdigest()
print("running")
 
time.sleep(10)
while True:
    try:
        response = urlopen(url).read()
        currentHash = hashlib.sha224(response).hexdigest()
        time.sleep(30)
        response = urlopen(url).read()
        newHash = hashlib.sha224(response).hexdigest()
        if newHash == currentHash:
            continue
        else:
            print("page updated")
            mail = outlook.CreateItem(0)
            mail.To = '***insert your email here***'
            mail.Subject = '***'
            mail.Body = "***"
            mail.Send()
           
            response = urlopen(url).read()
            currentHash = hashlib.sha224(response).hexdigest()
            time.sleep(30)
            continue
    except Exception as e:
        print("error")
