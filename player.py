
from email.policy import default
from song import Song
from dotenv import load_dotenv, find_dotenv, set_key
from random import randint

import click
import os
import sys
import select


dotenv_file = find_dotenv()
load_dotenv(dotenv_path=".env")



class Player():
    # REPEAT = False                  #  either the current song running or not
    # SEQUENTIAL = False              #  flag to track sequential mode
    # RANDOM = False                  #  flag to track random mode
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
    control = 'u'                  # either repaeat song, sequential, or random


 
    @staticmethod
    def choose_song():
        length = len(Player.music)
        while True:
            Player.display_songs()
            try:
                Player.next = int(input("Insert the number of the song\n>>> ")) - 1
                if Player.next >= length or Player.next < 0:
                    raise Exception()
                return
            except:
                print("Insert a value from 1-{}".format(length))

    @staticmethod
    def change_path():

        Player.path = os.path.join(Player.folderPath, Player.music[Player.next])
        if Player.current_song:
            print(type(Player.current_song))
            Player.current_song.set_path(Player.path)

    @staticmethod
    def display_songs():
        for index, value in enumerate(Player.music):
            print(value[:-4], index+1, sep=" ")

    @staticmethod
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
    def play_random_song():
        Player.next = randint(0, len(Player.music)-1)
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
    @click.command()
    def current_song_status():
        pass
    
    @click.command()
    @click.option('-chs', '--choose-song', is_flag=True)   
    @click.option('-q', '--quit' ,is_flag=True)
    @click.option('-r', '--random' ,is_flag=True) 
    @click.option('-s', '--sequential' ,is_flag=True)
    @click.option('-f', '--frequent', is_flag=True)
    def play(choose_song, quit, random, sequential, frequent):
        if choose_song:
            Player.choose_song()
            return
        elif quit:
            pass
        elif random:
            pass
        elif sequential:
            pass
        elif frequent:
            pass
        
        set_key(dotenv_file, "PLAYERSTATUS", "True")
        Player.play_random_song()  
        while Player.PLAYERSTATUS:
            Player.is_playing = Player.current_song.still_working()           # check if there is a song working
            Player._control_mode()                                            # to control the mode and must be called after _input 
            if not Player.is_playing:
                Player.play_random_song()
            



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

