import requests
from bs4 import BeautifulSoup
import smtplib



URL='https://www.amazon.in/All-New-Kindle-Paperwhite-10th-Built/dp/B077454Z99?pf_rd_p=bee4a676-f79b-4489-bcf3-0d8873a9db7f&pd_rd_wg=ctjxm&pf_rd_r=FF5H8J8TW3BSDKSA2BRX&ref_=pd_gw_bia_d0&pd_rd_w=u4Z32&pd_rd_r=d45cc95c-74cb-40cd-a4e0-df74c7061fe0'
headers ={"User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

page= requests.get(URL,headers=headers)


soup1=BeautifulSoup(page.content, "html.parser")
soup2=BeautifulSoup(soup1.prettify(), "html.parser")

price = soup2.find(id="priceblock_ourprice").get_text()

price1=price.strip()[1:4] 

# print price1
price2 = price.strip()[6:8]
# print price2

fprice=float( price1+price2 )

if(fprice < 12000):
    send_mail()



def send_mail():
    server= smtplib('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()


    #add your email id and password
    server.login('email id','pwd')

    subject="Price went down"
    body= "The price for this product https://www.amazon.in/All-New-Kindle-Paperwhite-10th-Built/dp/B077454Z99?pf_rd_p=bee4a676-f79b-4489-bcf3-0d8873a9db7f&pd_rd_wg=ctjxm&pf_rd_r=FF5H8J8TW3BSDKSA2BRX&ref_=pd_gw_bia_d0&pd_rd_w=u4Z32&pd_rd_r=d45cc95c-74cb-40cd-a4e0-df74c7061fe0 fell down"
    msg=f"Subject:{subject}\n\n{body}"

    server.sendmail(
        'add-your-email',
        'add-your-email or the email where you want to recieve the mail',
        msg

    )

    print("hey email has been sent")


    server.quit()


