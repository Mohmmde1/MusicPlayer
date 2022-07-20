import os
import sys
from dotenv import load_dotenv, find_dotenv, set_key

class Config:
    dotenv_file = find_dotenv()
    load_dotenv(dotenv_path=".env")
    
    @staticmethod
    def start():
        # check if the player is on that means i should stop close first teh last script
        if os.getenv("PLAYERSTATUS") == "True":
            os.system("kill -9 " + os.getenv("PID"))
            
        set_key(Config.dotenv_file, "PID", str(os.getpid()))
        set_key(Config.dotenv_file, "PLAYERSTATUS", str(True))

    
    @staticmethod
    def end():
        set_key(Config.dotenv_file, "PLAYERSTATUS", str(False))
        sys.exit()

    
    @staticmethod
    def get_path():
        return os.getenv("FOLDER_PATH")
        
    