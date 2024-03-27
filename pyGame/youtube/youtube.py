from pytube import YouTube


link = input("enter the link ")
yt = YouTube(link)


# print(yt.title)
# print(yt.views)

yd = yt.streams.get_highest_resolution()

yd.download("D:/Downloads")
