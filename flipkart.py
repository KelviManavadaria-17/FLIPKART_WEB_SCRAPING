from sqlalchemy import create_engine

from bs4 import BeautifulSoup 

import requests 




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
product=soup.find('div',attrs={'class':'_4rR01T'})

# print(product.text)
for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):
  name=a.find('div',attrs={'class':'_4rR01T'})

  price=a.find('div',attrs={'class':'_30jeq3 _1_WHN1'})

  rating=a.find('div',attrs={'class':'_3LWZlK'})
  links.append(a.get('href'))
  products.append(name.text)

  prices.append(price.text)

  ratings.append(rating.text)


df = pd.DataFrame({'NAME':products,'PRICE':prices,'RATINGS':ratings,'LINK':links})
print(df)
df.head()
df.to_csv('product.csv')


server = '127.0.0.1' 
database = 'flipkart' 
username = 'root' 
password = '' 


my_conn=create_engine("mysql+mysqldb://root:@localhost/flipkart")
df.to_sql(con=my_conn,name='products',if_exists='append',index=False)