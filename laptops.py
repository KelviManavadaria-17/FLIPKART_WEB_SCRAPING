from sqlalchemy import create_engine

from bs4 import BeautifulSoup 

import requests 

import find_number


import pandas as pd

url="https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=01f467b5-a95c-48de-a7e8-7862607e782a&as-backfill=on&sort=popularity"


response = requests.get(url)


htmlcontent = response.content

soup = BeautifulSoup(htmlcontent,"html.parser")

# print(soup.prettify)
products=[]

prices=[]
ratings=[]
links = []


total_products = soup.find('span',attrs={'class':'_10Ermr'})


res = [int(i) for i in total_products.text.split() if i.isdigit()]


no_of_products_in_one_page = res[1]
total_products_pages = find_number.find(total_products.text)
page_num = int(total_products_pages/no_of_products_in_one_page)
print(page_num)
for i in range(1,page_num +1):
    url1 = "https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=01f467b5-a95c-48de-a7e8-7862607e782a&as-backfill=on&sort=popularity&page=" + str(i)
    response = requests.get(url1)
    htmlcontent = response.content
    soup = BeautifulSoup(htmlcontent,"html.parser")
    product=soup.find('div',attrs={'class':'_4rR01T'})
    print(url1)
    for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):
        
        name=a.find('div',attrs={'class':'_4rR01T'})
        price=a.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
        rating=a.find('div',attrs={'class':'_3LWZlK'})
        links.append(a.get('href'))
        products.append(name.text)
        prices.append(price.text)
        if(rating != None):
            ratings.append(rating.text)
        else:
            ratings.append("None")








df = pd.DataFrame({'NAME':products,'PRICE':prices,'RATINGS':ratings,'LINK':links})
print(df)
df.head()
df.to_csv('product.csv')


server = '127.0.0.1' 
database = 'flipkart' 
username = 'root' 
password = '' 


my_conn=create_engine("mysql+mysqldb://root:@localhost/flipkart")
df.to_sql(con=my_conn,name='laptop',if_exists='append',index=False)