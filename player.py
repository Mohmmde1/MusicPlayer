
from song import Song

import os
import os.path
from playsound import playsound
import sys
import select
from random import randint


class Player:
    def __init__(self, folder_path="/users/mohammedalnashrei/Desktop/Music/"):
        self.folderPath = folder_path       # where the muisc files are
        self.music = self._list_music()     # list contains the songs' names
        self.next = 0                       # the index
        self.path = None                    # the path of the current song
        self.current_song = None            # song object
        self.current_index = None           # name of the current song
        self.user = ' '                      # what action to take
        self.pause = False                  # flag to stop the song
        self.PLAYERSTATUS = False           # flag to control the player
        self.status = False                 # in case there is a song playing

    def _list_music(self):
        return list(filter(lambda a: True if a[-1] == 'v' else False, os.listdir(self.folderPath)))

    def choose_song(self):
        # while True:
        self.display_songs()
        # try:
        self.next = int(input("Insert the number of the song\n>>>")) - 1
        # return
        # except:
        # print("Insert a value from 1-{}".format(len(self.music)))

    def change_path(self):
        self.path = os.path.join(self.folderPath, self.music[self.next])
        if self.current_song:
            self.current_song.set_path(self.path)

    def display_songs(self):
        for index, value in enumerate(self.music):
            print(value[:-4], " ", index+1)

    def display_status(self):
        if self.pause and self.current_index != "\nStopped ...\n":
            print("\nStoped ...\n")
            self.current_index = "\nStopped ...\n"
            
        elif self.music[self.next][:-4] != self.current_index and not self.pause:
            print("\n", self.music[self.next][:-4], " is currently playing.....")
            self.current_index = self.music[self.next][:-4]

    def play(self):
        self.PLAYERSTATUS = True
        while self.PLAYERSTATUS:
            if self.user == ' ':  # choose first song and play
                self.choose_song()
                self.change_path()
                self.current_song = Song(self.path)
                self.current_song.start()
                self.user = 'p'

            # check if there is a song working
            self.status = self.current_song.still_working()
            self.display_status()                              # display the current song

            # wait for an input for 5 secs
            i, o, e = select.select([sys.stdin], [], [], 5)
            if(i):
                self.user = sys.stdin.readline().strip()

            if not self.status and not self.pause:      # to play next song after
                self.user = 'n'                         # the first has finished
            
            self.action()

    def action(self):
        # to check @self.user
        if self.user == 'q':  # to end the program
            self.current_song.end()
            self.PLAYERSTATUS = False

        elif self.user == 'n':
            self.next = 0 if self.next + 1 > len(self.music)-1 else self.next + 1
            self.change_path()
            self.user = ''
            self.pause = False

        elif self.user == 'prev':
            self.next = self.next - 1 if self.next-1 > - \
                len(self.music) else len(self.music)-1
            self.change_path()
            self.user = ''

        elif self.user == 's':  # to pause the song
            self.current_song.end()
            self.pause = True
            self.user = ''

        elif self.user == 'r':
            self.current_song.start()
            self.user = ''

        elif self.user == 'd':
            self.choose_song()
            self.change_path()
            self.user = ''

        elif self.user == 'random' and not self.status:
            self.next = randint(0, len(self.music)-1)
            self.change_path()
