from concurrent.futures import process
import os
from psutil import pid_exists
from dotenv import load_dotenv, find_dotenv, set_key
import psutil

class Config:
    dotenv_file = find_dotenv()
    load_dotenv(dotenv_path=".env")
    
    @staticmethod
    def start():
        if os.getenv("PLAYERSTATUS") == "True":
            PID = int(os.getenv("PID"))

            if pid_exists(PID):
                proc, children = Config.get_children_processes_by_id(PID)
                for child in children:
                    child.terminate()
                proc.terminate()
            
        set_key(Config.dotenv_file, "PID", str(os.getpid()))
        set_key(Config.dotenv_file, "PLAYERSTATUS", str(True))

    
    @staticmethod
    def end():
        set_key(Config.dotenv_file, "PLAYERSTATUS", str(False))


    
    @staticmethod
    def get_path():
        return os.getenv("FOLDER_PATH")
    
        
    def set_song_name(name):
        set_key(Config.dotenv_file, "SONG_NAME", name)
    
    def set_song_index(index):
        set_key(Config.dotenv_file, "INDEX", str(index))
        
    def get_song_name():
        try:
            return os.getenv("SONG_NAME")
        except:
            return None
        
    def get_song_status():
        return os.getenv("PLAYERSTATUS") == "True"
    
    @staticmethod
    def get_children_processes_by_id(script_id):
        children = []
        process = None
        for proc in psutil.process_iter():
            try:
                if proc.pid==script_id:
                    process = proc
                    for child in proc.children():
                        children.append(child)
                    break

            except psutil.NoSuchProcess:
                continue
        return process, children
    
    @staticmethod
    def get_song_index():
        return int(os.getenv("INDEX"))
                
            

        
    