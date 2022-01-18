import os, shutil
from bs4 import BeautifulSoup
import requests, csv
from datetime import datetime
from progress.bar import Bar 
import datetime as dt

def getSoup(link):
    if requests.get(link).status_code == 200:
        All_Banners_Response = requests.get(link)
        return BeautifulSoup(All_Banners_Response.content, "html.parser")

start_time = datetime.now()

link = "https://genshin-info.ru/bannery/"



soup = getSoup(link)

links = []
things = []
banners = []

banners_characters = []

for a in soup.find_all("a"):
        if "bannery" in a.get("href") and len(a.get("href")) >9:
            banner_link = a.get("href")
            banner_link = banner_link[9:]
            if banner_link == "zhazhda-stranstviy/" or banner_link == "molitva-novichka/":
                continue
            else:
                links.append(link+banner_link)


getChar = Bar("Получение банеров", max=len(links),fill="+")
for getCharacters in range(len(links)):
    Character_Soup = getSoup(links[getCharacters])
    for i in Character_Soup.find_all(id="up"):
        da = i.find_all("div", attrs= {"class" : "itemcard__imgName"})
        for i in da:
            character_name = str(i)
            character_name = character_name[character_name.index(">")+1:len(character_name)-6]
            things.append(character_name)
        banners.append(things)
        getChar.next()
        things = []

getChar.finish()

sortBanners = Bar("Сортировка банеров", max=len(banners),fill="+")

for i in banners:
    if len(i) >= 6:
        sortBanners.next()
    else:
        banners_characters.append(i)
        sortBanners.next()
sortBanners.finish()



with open("banners.csv", 'w', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    for sublist in banners_characters:
        writer.writerow(sublist)

shutil.move("banners.csv","C:/Users/Mint Tea/Desktop/baneners/")
end_time = dt.now()

print(end_time-start_time)
print("Compilation is end")
