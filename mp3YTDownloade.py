from pytube import YouTube
import os

print("")
print("Made By Decryption")
print("")
yt = YouTube(input("Enter URL to Downlaod\n>> "))

video = yt.streams.filter(only_audio=True).first()

destination = "Audio/"

out_file = video.download(output_path=destination)

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

print(yt.title + " successfully downlaoded.")
