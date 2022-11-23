from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip, clips_array

import os
import tkinter as tk
from tkinter import ttk
from tkinter import *


def convert_BBB_video():
    os.system("ffmpeg -i BBB_30S.mp4 -vf scale=1280:720 BBB_720p.mp4") # Escalem el video a 720p i ho guardem com BBB_720p.mp4
    os.system("ffmpeg -i BBB_30S.mp4 -vf scale=852:480 BBB_480p.mp4") # Escalem el video a 480p i ho guardem com BBB_480p.mp4
    os.system("ffmpeg -i BBB_30S.mp4 -vf scale=360:240 BBB_360x240.mp4") # Escalem el video a 360x240 i ho guardem com BBB_360x240.mp4
    os.system("ffmpeg -i BBB_30S.mp4 -vf scale=160:120 BBB_160x120.mp4") # Escalem el video a 160x120 i ho guardem com BBB_160x120.mp4


convert_BBB_video() # S'executa la funció per convertir el video en els diferents outputs mencionats anteriorment


#TRIKINER

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Page1, Page2, Page3, Page4):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# Pàgina inicial
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Select a file to convert", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="BBB_720p.mp4",
                           command=lambda: controller.show_frame(Page1),
                           activeforeground="blue",
                           activebackground="pink",
                           pady=60,
                           padx = 200)
        button.pack()

        button2 = tk.Button(self, text="BBB_480p.mp4",
                            command=lambda: controller.show_frame(Page2),
                            activeforeground="blue",
                            activebackground="pink",
                            pady=60,
                            padx = 200)
        button2.pack()

        button3 = tk.Button(self, text="BBB_360x240.mp4",
                            command=lambda: controller.show_frame(Page3),
                            activeforeground="blue",
                            activebackground="pink", pady=60,
                            padx=200)
        button3.pack()
        button4 = tk.Button(self, text="BBB_160x120.mp4",
                            command=lambda: controller.show_frame(Page4),
                            activeforeground="blue",
                            activebackground="pink",
                            pady=60,
                            padx=200)
        button4.pack()


# Pàgina BBB_720p
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=" Select what extension do you want to convert the video to", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to initial page",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="VP8",
                            command= lambda: os.system("ffmpeg -i  BBB_720p.mp4 -c:v libvpx -b:v 1M -c:a libvorbis BBB_720p_VP8.webm"),
                            activeforeground="blue",
                            activebackground="pink",
                            pady=60,
                            padx=200)
        button2.pack()
        button3 = tk.Button(self, text="VP9",
                            command= lambda: os.system("ffmpeg -i  BBB_720p.mp4 -c:v libvpx -b:v 1M -c:a libvorbis BBB_720p_VP9.webm"),
                            activeforeground="blue",
                            activebackground="pink",
                            pady=60,
                            padx=200)
        button3.pack()
        button4 = tk.Button(self, text="h265",
                            command= lambda: os.system("ffmpeg -i BBB_720p.mp4 -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k BBB_720p_h265.mp4"),
                            activeforeground="blue",
                            activebackground="pink",
                            pady=60,
                            padx=200)
        button4.pack()
        button5 = tk.Button(self, text="Av1",
                            command= lambda: os.system("ffmpeg -i BBB_720p.mp4 -c:v libaom-av1 -crf 30 BBB_720p_Av1.mkv"),
                            activeforeground="blue",
                            activebackground="pink",
                            pady=60,
                            padx=200)
        button5.pack()

#Pàgina BBB_480p
class Page2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Select what extension do you want to convert the video to", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to initial page",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="VP8",
                            command=lambda: os.system(
                                "ffmpeg -i  BBB_480p.mp4 -c:v libvpx -b:v 1M -c:a libvorbis BBB_480p_VP8.webm"),
                            activeforeground="blue",
                            activebackground="pink",
                            pady=60,
                            padx=200)
        button2.pack()
        button3 = tk.Button(self, text="VP9",
                            command=lambda: os.system(
                                "ffmpeg -i  BBB_480p.mp4 -c:v libvpx -b:v 1M -c:a libvorbis BBB_480p_VP9.webm"),
                            activeforeground="blue",
                            activebackground="pink",
                            pady=60,
                            padx=200)
        button3.pack()
        button4 = tk.Button(self, text="h265",
                            command=lambda: os.system(
                                "ffmpeg -i BBB_480p.mp4 -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k BBB_480p_h265.mp4"),
                            activeforeground="blue",
                            activebackground="pink",
                            pady=60,
                            padx=200)
        button4.pack()
        button5 = tk.Button(self, text="Av1",
                            command=lambda: os.system("ffmpeg -i BBB_480p.mp4 -c:v libaom-av1 -crf 30 BBB_480p_Av1.mkv"),
                            activeforeground="blue",
                            activebackground="pink",
                            pady=60,
                            padx=200)
        button5.pack()
#Pàgina BBB_360x240
class Page3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Select what extension do you want to convert the video to", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to initial page",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="VP8",
                            command=lambda: os.system(
                                "ffmpeg -i  BBB_360x240.mp4 -c:v libvpx -b:v 1M -c:a libvorbis BBB_360x240_VP8.webm"),
                            activeforeground="blue",
                            activebackground="pink",
                            pady=60,
                            padx=200)
        button2.pack()
        button3 = tk.Button(self, text="VP9",
                            command=lambda: os.system(
                                "ffmpeg -i  BBB_360x240.mp4 -c:v libvpx -b:v 1M -c:a libvorbis BBB_360x240_VP9.webm"),
                            activeforeground="blue",
                            activebackground="pink",
                            pady=60,
                            padx=200)
        button3.pack()
        button4 = tk.Button(self, text="h265",
                            command=lambda: os.system(
                                "ffmpeg -i BBB_360x240.mp4 -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k BBB_360x240_h265.mp4"),
                            activeforeground="blue",
                            activebackground="pink",
                            pady=60,
                            padx=200)
        button4.pack()
        button5 = tk.Button(self, text="Av1",
                            command=lambda: os.system("ffmpeg -i BBB_360x240.mp4 -c:v libaom-av1 -crf 30 BBB_360x240_Av1.mkv"),
                            activeforeground="blue",
                            activebackground="pink",
                            pady=60,
                            padx=200)
        button5.pack()

#Pàgina BBB_160x120
class Page4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Select what extension do you want to convert the video to", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to initial page",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="VP8",
                            command= lambda: os.system("ffmpeg -i  BBB_160x120.mp4 -c:v libvpx -b:v 1M -c:a libvorbis BBB_160x120_VP8.webm"),
                            activeforeground="blue",
                            activebackground="pink",
                            pady=60,
                            padx=200)
        button2.pack()
        button3 = tk.Button(self, text="VP9",
                            command= lambda: os.system("ffmpeg -i  BBB_160x120.mp4 -c:v libvpx -b:v 1M -c:a libvorbis BBB_160x120_VP9.webm"),
                            activeforeground="blue",
                            activebackground="pink",
                            pady=60,
                            padx=200)
        button3.pack()
        button4 = tk.Button(self, text="h265",
                            command= lambda: os.system("ffmpeg -i BBB_160x120.mp4 -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k BBB_160x120_h265.mp4"),
                            activeforeground="blue",
                            activebackground="pink",
                            pady=60,
                            padx=200)
        button4.pack()
        button5 = tk.Button(self, text="Av1",
                            command= lambda: os.system("ffmpeg -i BBB_160x120.mp4 -c:v libaom-av1 -crf 30 BBB_160x120_Av1.mkv"),
                            activeforeground="blue",
                            activebackground="pink",
                            pady=60,
                            padx=200)
        button5.pack()
app = SeaofBTCapp()
app.mainloop()