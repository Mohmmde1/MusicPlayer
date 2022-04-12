from multiprocessing import Process 
from playsound import playsound
import wave
import contextlib
import time


class Song:
    def __init__(self, path):
        self.path = path
        
        # self.duratoin = self._cal_the_duration()
        self.process = Process(target=playsound, args=(self.path, ))
        self.duration = None

    # def start(self):
        # if self.process:
        #     self.end()
        # process = Process(target=playsound, args=(self.path, ))
       
        # self.process = process
      
    def end(self):
        self.process.terminate()
        
    
    def start(self):
        self.process = Process(target=playsound, args=(self.path, ))
        self.process.start()

    def set_path(self, path):
        self.end()
        self.path = path
        self.start()

    def _cal_the_duration(self):
        with contextlib.closing(wave.open(self.path,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            return frames / float(rate)

    def get_the_duratoin(self):
        return self.duratoin
    
    def countdown(self, t):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
    def still_working(self):
        if self.process:
            return self.process.is_alive() 
        return -1
