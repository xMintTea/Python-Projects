from base64 import decode
import requests, eel, json
import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0)+100, user32.GetSystemMetrics(1)+100

@eel.expose
def getTitle(name):
    data = requests.get(f"https://api.anilibria.tv/v2/searchTitles?search={name}&filter=names,description,status,posters,type").json()
    


    info = []
    for i in range(len(data)):
        poster = "https://static-libria.iss.bond"+data[i]["posters"]["small"]["url"]
        name = data[i]["names"]["ru"]
        status = data[i]["status"]["string"]
        description = data[i]["description"]
        type_ = data[i]["type"]["full_string"]
        info.append([name,description,status,poster,type_])
    return info
    


eel.init("web")
eel.start("index.html",cmdline_args=['--start-fullscreen'])

