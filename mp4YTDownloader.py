import pytube

#put you're link here
link = ""
yt = pytube.YouTube(link)
yt.streams.get_highest_resolution().download()
print("downloaded", link)
