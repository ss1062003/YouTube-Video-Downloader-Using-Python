from pytube import YouTube

link="https://www.youtube.com/watch?v=hwNWx1GTSKo"
youtube_1 = YouTube(link)

videos = youtube_1.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
strm = int(input("enter:"))
videos[strm].download()
print("SUCCESSFULLY")