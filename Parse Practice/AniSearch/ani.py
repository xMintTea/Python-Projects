import requests, eel
import ctypes, subprocess


subprocess.SW_HIDE

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

eel.init("web")


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
    
@eel.expose
def getYouTube(limit=6,offset=0):
    api = f"https://api.anilibria.tv/v2/getYouTube?limit={limit}&filter=image,youtube_id,title"
    data = requests.get(api).json()

    videos = []
    for i in range(len(data)):
        title = data[i]['title']
        image = data[i]['image']
        link = data[i]["youtube_id"]
        videos.append([image,link,title])
    return videos[offset:]




eel.start("main.html",cmdline_args=['--start-fullscreen'])

