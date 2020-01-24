import requests
from bs4 import BeautifulSoup


URL= 'https://www.amazon.com/EarFun-Bluetooth-Waterproof-Earpclehones-Headphones/dp/B07R5MKX3K'

headers ={"User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

page= requests.get(URL,headers=headers)


soup1=BeautifulSoup(page.content, "html.parser")
soup2=BeautifulSoup(soup1.prettify(), "html.parser")

print soup2

