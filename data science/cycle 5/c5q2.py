import requests
from bs4 import BeautifulSoup

print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
def getdata(url):
    r=requests.get(url)
    return r.content

htmldata=getdata("https://sjcetpalai.ac.in/")
soup=BeautifulSoup(htmldata,'html.parser')

links=soup.find_all("a")
print("links: ",len(links))
for link in links:
    if link.get("href") != "":
        print("Link: ",link.get("href"),"Text: ",link.string)