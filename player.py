
from song import Song
from dotenv import load_dotenv
from random import randint

import click
import os
import sys
import select



load_dotenv()



class Player():
    next = 0                       # the index
    folderPath =  os.getenv('folder_path')    # where the muisc files are
    music = list(filter(lambda a: True if a[-1] == 'v' else False, os.listdir(folderPath)))     # list contains the songs' names
    current_song = None            # song object
    current_index = None           # name of the current song
    path = None                    # the path of the current song
    PLAYERSTATUS = os.getenv("PLAYERSTATUS") == "True" # flag to control the player
    pause = os.getenv("PAUSE") == "True"                  # flag to stop the song
    is_playing = False             # in case there is a song playing
    repeat = False                 # either keep the current song running or not
    user = ''                      # what action to take
    control = 'u'                  # either repaeat song, sequential, or random


 
    @staticmethod
    # @click.command()
    def choose_song():

        # while True:
        Player.display_songs()
        # try:
        Player.next = int(input("Insert the number of the song\n>>> ")) - 1

        # return
        # except:
        print("Insert a value from 1-{}".format(len(Player.music)))

    @staticmethod
    def change_path():

        Player.path = os.path.join(Player.folderPath, Player.music[Player.next])
        if Player.current_song:
            Player.current_song.set_path(Player.path)

    @staticmethod
    def display_songs():
        for index, value in enumerate(Player.music):
            print(value[:-4], index+1, sep=" ")

    @staticmethod
    # @click.command()
    def display_status():
        if Player.pause and Player.current_index != "Stopped":
            print("\nStopped ...\n")
            Player.current_index = "Stopped"
            Player._display_controllers()

        elif Player.music[Player.next][:-4] != Player.current_index and not Player.pause:
            print("\n", Player.music[Player.next][:-4], " is currently playing.....\n")
            Player.current_index = Player.music[Player.next][:-4]
            Player._display_controllers()
    
    @staticmethod
    # @click.command()
    def _display_controllers():
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

    @staticmethod
    def _first_song():

        Player.choose_song()
        Player.change_path()
        Player.current_song = Song(Player.path)
        Player.current_song.start()

    @staticmethod
    # @click.command()
    def _control_mode():
        # Here player mange the mode when the song is finihsed 
        # and not stopped:
        # 1. k for keeping the next song 
        # 2. b to pick random song
        # 3. u to make it sequential mode (default)       
        if not Player.is_playing and not Player.pause:
            if Player.control == 'k':
                Player.user = 'r'
            elif Player.control == 'b': 
                Player.user = 'random'      
            elif Player.control == 'u':
                Player.user = 'n'       

    @staticmethod
    # @click.command()
    def _input():
        i, o, e = select.select([sys.stdin], [], [], 1)      
        if i: # keyboard prssed detected
            Player.user = sys.stdin.readline().strip().lower() 
            if Player.user in set("qnpr"):
                Player.pause = False
        else:
            Player.user = ''
    
    @staticmethod
    @click.command()    
    def play():
        os.environ["PLAYERSTATUS"] = "True"

        Player._first_song()  # choose first song and play
        while Player.PLAYERSTATUS:
            Player.is_playing = Player.current_song.still_working()           # check if there is a song working
            Player.display_status()                                           # display the current song
            Player._input()                                                   # wait for an input for 5 secs
            Player._control_mode()                                            # to control the mode and must be called after _input 
            
            # to get control
            Player.control = Player.user if Player.user in set("ubk") else Player.control
            
            # make an action based on the input user
            Player.action()


    @staticmethod
    def action():
        # to check @user
        if Player.user == 'q':  # to end the program
            Player.current_song.end()
            Player.PLAYERSTATUS = False

        elif Player.user == 'random':
            Player.next = randint(0, len(Player.music)-1)
            Player.change_path()
        
        elif Player.user == 'n':
            Player.next = 0 if Player.next + \
                1 > len(Player.music)-1 else Player.next + 1
            Player.change_path()

        elif Player.user == 'p':
            Player.next = Player.next - 1 if Player.next-1 > - \
                len(Player.music) else len(Player.music)-1
            Player.change_path()

        elif Player.user == 's':  
            Player.current_song.end()
            Player.pause = True

        elif Player.user == 'r':
            Player.current_song.start()

        elif Player.user == 'd':
            Player.choose_song()
            Player.change_path()

