import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_American_football_stadiums_by_capacity"

page = urllib.request.urlopen(url)

soup = BeautifulSoup(page, "lxml")

right_table = soup.find_all('table', class_="wikitable sortable plainrowheaders")
# print(right_table[0])

# Capacity
A=[]
#Capacity after new line removed
AA=[]

#City
B=[]


#State/Province
C=[]

#Home teams
D=[]

# Stadium Name
E=[]


for row in right_table[0].findAll('tr'):
    cells=row.findAll('td')
    headers=row.findAll('th')
    if len(cells)==6:
        A.append(cells[1].find(text=True))
        B.append(cells[2].find(text=True))
        C.append(cells[3].find(text=True))
        D.append(cells[4].find(text=True))
        E.append(headers[0].find(text=True))

#take off new line character from html
for i in A:
	num = i[:-1]
	AA.append(num)




df=pd.DataFrame(E,columns=['Stadium Name'])
df['Capacity']=AA
df['City']=B
df['State/Province']=C
df['Home Teams']=D

print(df)

df.to_csv('American_Football_Stadiums_Capacity.csv')




             




