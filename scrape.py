import pandas as pd
import numpy as np
import requests,openpyxl
from bs4 import BeautifulSoup

PhoneName=[]
Price=[]
Features=[]
newdataframe=pd.DataFrame()

try:
    source = requests.get("https://www.flipkart.com/search?q=mobile+phone+5g&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobile+phone+5g%7CMobiles&requestId=61c49f0b-72f7-46bd-bc25-43d98824df52&as-searchtext=moblie%20phones")
    source.raise_for_status() #it throws the error if the link is not

    soup=BeautifulSoup(source.text,'html.parser')
    phones=soup.findAll('div',class_='_4rR01T')
    features=soup.findAll('li',class_='rgWa7D')
    price=soup.findAll('div',class_='_30jeq3 _1_WHN1')
    for i in phones:
        phone=i.text
        PhoneName.append(phone)
    for i in price:
        price = i.text
        Price.append(price)
    for i in features:
        featu = i.text
        Features.append(featu)
    newdataframe['Phone']=PhoneName
    newdataframe['Price'] = Price
    newdataframe.to_excel("exceldata.xlsx",index=False)
    excelData=pd.read_excel('exceldata.xlsx')
    print(excelData)

except Exception as e:
    print(e)
