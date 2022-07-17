
# import sys


# # import pygame
# path = "/Users/mohammedalnashrei/Desktop/Music/Sean Paul - Temperature (Official Video).wav"
# # import multiprocessing
# from playsound import playsound
# # if __name__ == '__main__':
# #     p = multiprocessing.Process(target=playsound, args=(path,))
# #     p.start()
# #     print("HI")
# #     sys.exit()
# #You First Need To Do This In Your Python Terminal: "pip install pydub"
# # from pydub import AudioSegment
# from pydub.playback import play
import threading

# # sound = AudioSegment.from_wav(path)
# t = threading.Thread(target=playsound, args=(path,))
# t.start()
# quit()
# print("I like this line to be executed simoultinously with the audio playing")
import os
import pafy
import vlc
import time
import random
import re
import requests
import subprocess
import urllib.parse
import urllib.request


def play(name, n):
    query_string = urllib.parse.urlencode({"search_query": name})
    formatUrl = urllib.request.urlopen(
        "https://www.youtube.com/results?" + query_string)
    search_results = re.findall(
        r"watch\?v=(\S{11})", formatUrl.read().decode())
    clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
    video = pafy.new(clip2)
    if n == 1:
        videolink = video.getbest()
        print("video is playing")
    else:
        videolink = video.getbestaudio()
        print("audio is playing")
    media = vlc.MediaPlayer(videolink.url)
    # t = threading.Thread(target=playsound, args=(videolink.url,))
    # t.start()
    media.play()
    time.sleep(30)
    media.stop()


while n != 0:
    print("Enter 1 for video and 2 for only audio")
    n = int(input())
    print("Enter play name:")
    play(input(), n)
