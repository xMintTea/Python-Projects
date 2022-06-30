from pyparsing import col
import requests

week = ["Понедельник",'Вторник','Среда','Четверг','Пятница',"Суббота","Воскресенье"]




def getSchedule():
    schedule = []
    link = "https://api.anilibria.tv/v2/getSchedule"
    data = requests.get(link).json()
    for i in range(0,7):
        print(week[i])
        for j in range(len(data[i]["list"])):
            name = data[i]["list"][j]["names"]["ru"]
            print("     "+name)
        print("\n")

