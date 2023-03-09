import pandas as pd
import numpy as np
import requests,openpyxl
from bs4 import BeautifulSoup

Products=[]
Price=[]
Features=[]
ProductLink=[]
Reviews=[]
newdataframe=pd.DataFrame()
flipkartAddress="https://www.flipkart.com/search?q="
flipkartBaseAddress="https://www.flipkart.com"
searchWord=input("Enter the search queries:")
result=flipkartAddress+searchWord.replace(" ","+")
#print(result)
if __name__ == '__main__':
        try:
            page_num=int(input("Enter the number of pages:"))
            for j in range(1,int(page_num)+1):
                source = requests.get(result+"&"+str(j))
                source.raise_for_status()
                soup = BeautifulSoup(source.content, 'html.parser')
                products = soup.findAll('div', class_='_4rR01T')
                features = soup.findAll('ul', class_="_1xgFaf")
                price = soup.findAll('div', class_='_30jeq3 _1_WHN1')
                link = soup.find_all('a', class_="_1fQZEK")
                ratings=soup.findAll('div',class_="_3LWZlK")
                #print("page "+str(j))
                for i in link:
                    productLinks = flipkartBaseAddress + i['href']
                    ProductLink.append(productLinks)
                for i in products:
                    Product = i.text
                    Products.append(Product)
                for i in ratings:
                    rates=i.text
                    Reviews.append(rates)
                for i in price:
                    price = i.text
                    Price.append(price)
                for i in features:
                    featu = i.text
                    Features.append(featu)
                #print(Rating)
            newdataframe['Product'] = Products
            newdataframe['Features'] = Features
            #print(len(Reviews))
            newdataframe['Price'] = Price
            newdataframe['Product Link'] = ProductLink
            newdataframe.to_excel("Product.xlsx", index=False)
            excelData = pd.read_excel('Product.xlsx')
            print(excelData)
        except Exception as e:
            print(e)





