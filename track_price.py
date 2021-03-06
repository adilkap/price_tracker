import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.com/any-product-here"

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, 'html.parser')
soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')


product_price = soup2.find(id= "priceblock_ourprice").get_text()
converted_price = float (product_price[1:5])
    
product_title = (soup2.find(id="productTitle").get_text().strip())

def track_price():

    if (converted_price < 10):
        send_mail()
    else: print ("The price of \n {0} \n has not dropped below the specified value :(".format(product_title))

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('emailaddress@gmail.com', 'google-app-password')

    subject = 'The price for {0} fell below your price, and is now only {1}!'.format(product_title, product_price)
    body = 'Click the link below to view the product on Amazon: \n https://www.amazon.com/any-product-here'
    msg =  "Subject: {0} \n\n\n {1}".format(subject, body)
   

    server.sendmail(
        'emailaddress@gmail.com', 
        'receiving email', 
        msg)
    
    print ("Email has successfuly been sent")

    server.quit()

while(True):
    track_price()
    time.sleep(86400)

