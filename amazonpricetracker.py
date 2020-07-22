import requests
from bs4 import BeautifulSoup
import time
import smtplib

URL = "https://www.amazon.in/Apple-iPhone-Pro-Max-256GB/dp/B07XVMDRZW/ref=sr_1_3?dchild=1&keywords=iphone&qid=1595356917&sr=8-3"

def sendemail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('your email here','your password here')

    subject = "Your Product Price Has Dropped"
    body = "Your Product Price Has Dropped please ckeck out" + URL

    message = f"Subject: {subject} \n\n {body}"

    server.sendmail(
        'sender email here',
        'receiver email here',
        message
    )
    print("email sent")
    server.quit()

def pricecheck():
    headers = {'User-Agent': 'search google for your user agent'}
    time.sleep(5)
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    # title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    new_price = float(price[1:].replace(",",""))

    if new_price < 13190.0:
        sendemail()
    print(new_price)

while True:
    pricecheck() 
    time.sleep(10000)      

