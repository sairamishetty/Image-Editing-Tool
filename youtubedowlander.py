from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title:", yt.title)

yd = yt.streams.get_lowest_resolution()
yd.download('/Users/saira/OneDrive/Documents/School/projects/PYTHON AUTOMATION/DowlandVideo')
