import sys
from objs.song import Song
from random import randint
from config.config import Config

import click
import os

class Player():
    next = 0                       # the index of the current song 
    FolderPath =  Config.get_path()     # where the muisc files are
    music = list(filter(lambda a: True if a[-1] == 'v' else False, os.listdir(FolderPath)))     # list contains the songs' names
    current_song = None            # song object
    path = None                    # the path of the current song
    is_playing = False             # in case there is a song playing

    @staticmethod
    def choose_song():
        length = len(Player.music)
        Player.display_songs()
        while True:
            try:
                Player.next = int(input("Insert the number of the song\n>>> ")) - 1
                if Player.next >= length or Player.next < 0:
                    raise Exception()
                return
            except:
                print("\nInsert a value from 1-{}".format(length))

    @staticmethod
    def change_path():
        Player.path = os.path.join(Player.FolderPath, Player.music[Player.next])
        if Player.current_song:
            Player.current_song.set_path(Player.path)

    @staticmethod
    def display_songs():
        for index, value in enumerate(Player.music):
            print(value[:-4], index+1, sep=" ")
    
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
    @click.command()
    def status():
        if Config.get_song_status():
            print(Config.get_song_name()[:-3] + " is currently playing ....")
        else:
            print("No song is playing")
    
    @click.command()
    @click.option('-cs', '--choose-song', is_flag=True)   
    @click.option('-q', '--quit' ,is_flag=True)
    @click.option('-r', '--random' ,is_flag=True) 
    @click.option('-s', '--sequential' ,is_flag=True)
    @click.option('-f', '--frequent', is_flag=True)
    def play(choose_song, quit, random, sequential, frequent): 
        Config.start()
        while True:
            if not Player.is_playing:
                if choose_song:
                    Player.choose_song()

                elif quit:
                    Config.end()
                    sys.exit()

                elif sequential:
                    Player.next = 0 if Player.next + \
                        1 > len(Player.music)-1 else Player.next + 1

                elif frequent:
                    Player.next = Player.next
                    
                elif random:
                    Player.next = randint(0, len(Player.music)-1)
                    
                Player.change_path()
                Player.current_song = Song(Player.path)
                Player.current_song.start()
                Config.set_song_name(Player.music[Player.next])
                
            Player.is_playing = Player.current_song.still_working()           # check if there is a song working
            
            