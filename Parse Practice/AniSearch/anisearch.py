# https://github.com/anilibria/docs/blob/master/api_v2.md

import requests, json, time,os

class Anime:
    

    def getTitle(name):
        name = name.strip().replace(" ","-")
        api = f"https://api.anilibria.tv/v2/getTitle?code={name}"
        data = requests.get(api)
        if data.status_code == 200:
            data = data.json()
            print(data["names"]["ru"]) #Название
            print(data["status"]["string"]) #Статус
            for i in data["genres"]: #Жанры
                print(f"{i}",end="")
            print(data["player"]["series"]["string"]) #Количество серий
            print(data["description"]) #Описание
        else:
            print(data.status_code)

    def getGenres():
        api = f"https://api.anilibria.tv/v2/getGenres"
        data = requests.get(api)
        print(data.content.decode("utf-8"))

    def search(name):
        try:
            api = f"https://api.anilibria.tv/v2/searchTitles?search={name}"
            data = requests.get(api)
            if data.status_code == 200:
                data = json.loads(data.content)
                print(data[0]["names"]["ru"],"|",data[0]["names"]["en"])
                print(data[0]["type"]["full_string"])
                print(data[0]["status"]["string"], data[0]["season"]["year"])
                
                print("\nЖанры:")
                for i in data[0]["genres"]:
                    print(i+" ", end="")
                print("\n\nОписание:")
                desc = data[0]["description"].split(".")
                for i in desc:
                    print(i.strip())
                code = data[0]["code"]
                link = f"https://ww.anilibria.cf/release/{code}.html"
                print("\nСсылка на сайт:", link)
                input("\nНажмите на любую клавишу, чтобы продолжить")
                os.system("cls")
        except:
            print("Что-то пошло не так...")
            time.sleep(3)
            os.system("cls")

while 1:
    print("0. Закрыть\n1. Найти аниме")
    answer = int(input("Ввод: "))
    if answer == 0:
        break
    elif answer == 1:
        name = input("Введи название аниме: ")
        os.system("cls")
        Anime.search(name)


