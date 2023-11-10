from pytube import YouTube
from sys import argv


if len(argv) != 2:
    print("Usage: python script.py <YouTube video URL>")
    exit()

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)

# Get the stream with the highest resolution
yd = yt.streams.get_highest_resolution()

# Downloading the video into this folder
download_path = r'C:\Users\viet\desktop\Own Projects\YTDownloads'

# Download the video
yd.download(download_path)

print("Download complete.")
