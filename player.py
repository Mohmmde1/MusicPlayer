
from song import Song

import os
import os.path
from playsound import playsound
import sys
import select
from random import randint


class Player:
    def __init__(self, folder_path="/users/mohammedalnashrei/Desktop/Music/"):
        self.folderPath = folder_path
        self.music = self._list_music()
        self.next = 0
        self.path = None
        self.current_song = None
        self.current_index = None
        self.user = ''


    def _list_music(self):
        return list(filter(lambda a: True if a[-1] == 'v' else False, os.listdir(self.folderPath)))

    # def song_path(self):
    #     self.path = self.folderPath + self.music[self.next]

    def choose_song(self):
        # while True:
        self.display_songs()
            # try:
        self.next = int(input("Insert the number of the song\n>>>")) - 1
            # return
            # except:
                # print("Insert a value from 1-{}".format(len(self.music)))

    def change_path(self):
        self.path = os.path.join(self.folderPath,self.music[self.next])
        if self.current_song:
            self.current_song.set_path(self.path)

    def display_songs(self):
        for index, value in enumerate(self.music):
            print(value[:-4], " ", index+1)

    def play(self):
        self.choose_song()
        self.change_path()
        self.current_song = Song(self.path)
        self.current_song.start()
        # self.current_song.start()
        while True: 
            
            # if self.music[self.next][:-4] != self.current_index:
            #     print("\n", self.music[self.next][:-4], " is currently playing.....")
            #     self.current_index = self.music[self.next][:-4]
            if self.user == '':
                self.choose_song()
                self.change_path()
                self.current_song = Song(self.path)
                self.current_song.start()
                self.user = 'p'
                print("here assigning user to p")

            i, o, e = select.select([sys.stdin], [], [], 5)
            if(i):
                self.user = sys.stdin.readline().strip()

            # if not self.current_song.still_working() and stop != 's':
            #     self.user = self.status
            if self.user == 'q':
                self.current_song.end()
                break
            elif self.user == 'p' and not self.current_song.still_working():
                self.current_song.start()
                print("here the song should have been started..")
                # stop = ''
                # current_song.countdown(current_song.get_the_duratoin())

            elif self.user == 'n':
                self.next = 0 if self.next+1 > len(self.music)-1 else self.next + 1
                self.change_path()
                
            elif self.user == 'prev':
                self.next = self.next - 1 if self.next-1 > - \
                    len(self.music) else len(self.music)-1
                self.change_path()

            elif self.user == 's':
                self.current_song.end()
                # stop = 's'

            elif self.user == 'r':
                self.current_song.start()
                
            elif self.user == 'd':
                self.next = self.choose_song() 
                self.change_path()

            elif self.user == 'random':
                self.next = randint(0, len(self.music)-1)
                self.change_path()
            