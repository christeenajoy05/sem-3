import requests
from bs4 import BeautifulSoup

def getdata(url):
    r=requests.get(url)
    return r.content

print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
htmldata=getdata("https://www.w3schools.com/html/html_entities.asp")
soup=BeautifulSoup(htmldata,'html.parser')
data=''
pr=len(soup.find_all('p'))
print("P tag: ",pr)
for data in soup.find_all('p'):
    print(data.get_text())