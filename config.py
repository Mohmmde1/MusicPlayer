import os
from pickle import NONE
import signal
import sys
from dotenv import load_dotenv, find_dotenv, set_key

class Config:
    dotenv_file = find_dotenv()
    load_dotenv(dotenv_path=".env")
    
    @staticmethod
    def start():
        if os.getenv("PLAYERSTATUS") == "True":

            try:
                os.kill(int(os.getenv("PID")), signal.SIGTERM)
                os.kill(int(os.getenv("SONG_PID")), signal.SIGTERM)
            except:
                Config.end()
            
        set_key(Config.dotenv_file, "PID", str(os.getpid()))
        set_key(Config.dotenv_file, "PLAYERSTATUS", str(True))

    
    @staticmethod
    def end():
        set_key(Config.dotenv_file, "PLAYERSTATUS", str(False))
        sys.exit()

    
    @staticmethod
    def get_path():
        return os.getenv("FOLDER_PATH")
    
    @staticmethod
    def set_song_pid(pid):
        set_key(Config.dotenv_file, "SONG_PID", str(pid))
        
    def set_song_name(name):
        set_key(Config.dotenv_file, "SONG_NAME", name)
        
    def get_song_name():
        try:
            return os.getenv("SONG_NAME")
        except:
            return None
    