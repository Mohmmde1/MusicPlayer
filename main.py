


from song import Song

import os
import os.path
from playsound import playsound
import sys, select
from random import randint

def display_songs(music):
    for index, value in enumerate(music):
        print(value[:-4], " ", index+1)

def choose_song():
    while True:
        display_songs(music)
        try:
            return int(input("Insert the number of the song\n>>>"))
        except:
            print("Insert a value from 1-{}".format(len(music)))

        if 0 < next <= len(music):
            break

def change_path(index):
    path =  folderPath + "/" + music[index]  
    current_song.set_path(path)

if __name__ == '__main__': 
    folderPath = "/Users/mohammedalnashrei/Desktop/Music/"
    music = list(filter(lambda a: True if a[-1]=='v' else False, os.listdir(folderPath)))
    next = choose_song() - 1
    path = '/Users/mohammedalnashrei/Desktop/Music/' + music[next]
    current_song = Song(path)
    current_index = ''
    status = 'n'
    if current_song:
        current_song.start()
    stop = ''
    while True:
        user = ''
        if music[next][:-4]!= current_index:
            print("\n", music[next][:-4], " is currently playing.....")
            current_index = music[next][:-4]
        
        i, o, e = select.select([sys.stdin], [], [], 5)
        if(i):
            user = sys.stdin.readline().strip()
        

        if not current_song.still_working() and stop !='s':
            user = status

        if user == 'q': 
            current_song.end()
            sys.exit()

        elif user == 'p':
            current_song.start()
            stop = ''
            # current_song.countdown(current_song.get_the_duratoin())
           
        elif user == 'n':
            next = 0 if next+1 > len(music)-1 else next + 1
            change_path(next)

        elif user == 'prev':
            next = next - 1 if next-1 > -len(music) else len(music)-1
            change_path(next)
        
        elif user == 's':
            current_song.end()
            stop ='s'
            
        elif user == 'r':
            current_song.start()

        elif user == 'd':
            display_songs(music)

        elif user =='random':
            next = randint(0, len(music)-1)
            change_path(next)


       
        
       
            
            