import time
import hashlib
from urllib.request import urlopen, Request
import win32com.client
 
outlook = win32com.client.Dispatch('outlook.application')
url = Request('https://moshtix.co.nz/v2/event/rhythm-and-vines-2022-the-20th-anniversary/123507?skin=RVD22',
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
            print("New tickets up")
            mail = outlook.CreateItem(0)
            mail.To = 'lfo47@uclive.ac.nz'
            mail.Subject = 'New RNV Resale Tickets'
            mail.Body = "New tickets got added \n https://moshtix.co.nz/v2/event/rhythm-and-vines-2022-the-20th-anniversary/123507?skin=RVD22"
            mail.Send()
            
            mail = outlook.CreateItem(0)
            mail.To = 'evafgalvin@gmail.com'
            mail.Subject = 'New RNV Resale Tickets'
            mail.Body = "New tickets got added \n https://moshtix.co.nz/v2/event/rhythm-and-vines-2022-the-20th-anniversary/123507?skin=RVD22"
            mail.Send()
           
            response = urlopen(url).read()
            currentHash = hashlib.sha224(response).hexdigest()
            time.sleep(30)
            continue
    except Exception as e:
        print("we shit the bed")