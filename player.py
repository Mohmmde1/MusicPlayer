
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
        self.current_song = None            # song object
        self.current_index = None           # name of the current song
        self.path = None                    # the path of the current song
        self.PLAYERSTATUS = False           # flag to control the player
        self.pause = False                  # flag to stop the song
        self.status = False                 # in case there is a song playing
        self.repeat = False                 # either keep the current song running or not
        self.user = ''                      # what action to take
        self.control = 'u'                  # either repaeat song, sequential, or random

    def _list_music(self):
        return list(filter(lambda a: True if a[-1] == 'v' else False, os.listdir(self.folderPath)))

    def choose_song(self):
        # while True:
        self.display_songs()
        # try:
        self.next = int(input("Insert the number of the song\n>>> ")) - 1
        # return
        # except:
        # print("Insert a value from 1-{}".format(len(self.music)))

    def change_path(self):
        self.path = os.path.join(self.folderPath, self.music[self.next])
        if self.current_song:
            self.current_song.set_path(self.path)

    def display_songs(self):
        for index, value in enumerate(self.music):
            print(value[:-4], index+1, sep=" ")

    def display_status(self):
        if self.pause and self.current_index != "Stopped":
            print("\nStopped ...\n")
            self.current_index = "Stopped"
            self._display_controllers()

        elif self.music[self.next][:-4] != self.current_index and not self.pause:
            print("\n", self.music[self.next][:-4],
                  " is currently playing.....\n")
            self.current_index = self.music[self.next][:-4]
            self._display_controllers()
    
    def _display_controllers(self):
        print("Press\
            \nq to quit\
            \nn to go to next song\
            \np to go back to previous song\
            \ns to stop current song\
            \nr to restart the current song\
            \nd to display and choose the song\
            \nb to make the status random\
            \nk to keep the current song\
            \nu to make a sequential mode\
            \n>>> ", end='')

    def _first_song(self):
        self.choose_song()
        self.change_path()
        self.current_song = Song(self.path)
        self.current_song.start()

    def _control_mode(self):
        # Here player mange the mode when the song is finihsed 
        # and not stopped:
        # 1. k for keeping the next song 
        # 2. b to pick random song
        # 3. u to make it sequential mode (default)       
        if not self.status and not self.pause:
            if self.control == 'k':
                self.user = 'r'
            elif self.control == 'b': 
                self.user = 'random'      
            elif self.control == 'u':
                self.user = 'n'       

    def _input(self):
        i, o, e = select.select([sys.stdin], [], [], 1)      
        if i: # keyboard prssed detected
            self.pause = False
            self.user = sys.stdin.readline().strip().lower() 
        else:
            self.user = ''
            
    def play(self):
        self.PLAYERSTATUS = True
        self._first_song()  # choose first song and play
        while self.PLAYERSTATUS:
            self.status = self.current_song.still_working()                 # check if there is a song working
            self.display_status()                                           # display the current song
            self._input()                                                   # wait for an input for 5 secs
            self._control_mode()                                            # to control the mode
            
            # to get control
            self.control = self.user if self.user in "ubk" and self.user != '' else self.control

            # make an action based on the input user
            self.action()

    def action(self):
        # to check @self.user
        if self.user == 'q':  # to end the program
            self.current_song.end()
            self.PLAYERSTATUS = False

        elif self.user == 'n':
            self.next = 0 if self.next + \
                1 > len(self.music)-1 else self.next + 1
            self.change_path()

        elif self.user == 'p':
            self.next = self.next - 1 if self.next-1 > - \
                len(self.music) else len(self.music)-1
            self.change_path()

        elif self.user == 's':  
            self.current_song.end()
            self.pause = True

        elif self.user == 'r':
            self.current_song.start()

        elif self.user == 'd':
            self.choose_song()
            self.change_path()

        elif self.user == 'random':
            self.next = randint(0, len(self.music)-1)
            self.change_path()
