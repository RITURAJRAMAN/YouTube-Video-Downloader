from tkinter import *
from pytube import YouTube

window = Tk()
window.title("Future Keys")
window.geometry('500x400')
window.configure(bg='black')
Label(window, text="YouTube Video Downloader", font="algerian 22 bold", bg='OrangeRed1').place(x=30, y=20)
Msg = StringVar()
Label(window, text="Enter URL", font='arial 15 bold', fg='white', bg='black').place(x=50, y=100)
entry = Entry(window, textvariable=Msg, font='arial 16')
entry.place(x=50, y=140, width=420, height=35)


def download():
    url = entry.get()
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    stream.download(output_path='D:\Rituraj\Videos')


Button(window, text='Start Download', font='arial 12 bold', width='15', bg='lightgreen', command=download).place(x=150,
                                                                                                                 y=250)
Button(window, text='Exit', font='arial 12 bold', width='15', bg='red', command=window.destroy).place(x=150, y=300)
window.mainloop()
