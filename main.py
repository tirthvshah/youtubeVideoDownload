import pytube
url="https://www.youtube.com/watch?v=xgXnDnf0cHY"

video = pytube.YouTube(url)
youtube = video.streams.first()
youtube.download(r'C:\Users\admin\Downloads')