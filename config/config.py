from concurrent.futures import process
import os
import signal
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
            # SONG_PID = int(os.getenv("SONG_PID"))
            
            # safe guard to check if the song and the player are running
            # if pid_exists(SONG_PID):
            #     os.kill(SONG_PID, signal.SIGTERM)
            if pid_exists(PID):
                proc, children = Config.get_script_children_processes_by_id(PID)
                for child in children:
                    child.kill()
                proc.kill()
                
            # to update the player status into False
            # if not pid_exists(PID):
            #     Config.end()
            
        set_key(Config.dotenv_file, "PID", str(os.getpid()))
        set_key(Config.dotenv_file, "PLAYERSTATUS", str(True))

    
    @staticmethod
    def end():
        set_key(Config.dotenv_file, "PLAYERSTATUS", str(False))


    
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
        
    def get_song_status():
        return os.getenv("PLAYERSTATUS") == "True"
    @staticmethod
    def get_script_children_processes_by_id(script_id):

        children = []
        process = None
        for proc in psutil.process_iter():
            try:
                if proc.pid==script_id:
                    process = proc
                    for child in proc.children():
                        children.append(child)

            except psutil.NoSuchProcess:
                continue
            
        return proc, children
                
            

        
    