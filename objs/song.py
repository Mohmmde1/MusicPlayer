from multiprocessing import Process 
from playsound import playsound
from config.config import Config
import wave
import contextlib
import time


class Song:
    
    __slots__ = ('path', 'process', 'duration', )
    def __init__(self, path):
        self.path = path
        
        # self.duratoin = self._cal_the_duration()
        self.process = None
        self.duration = None


    # def start(self):
        # if self.process:
        #     self.end()
        # process = Process(target=playsound, args=(self.path, ))
       
        # self.process = process
      
    def __eq__(self, __o: object) -> bool:
        if object.__class__ is self.__class__:
            return object.path == self.path
        raise NotImplementedError
    
    def __ne__(self, __o: object) -> bool:
        if object.__class__ == self.__class__:
            return object.path != self.path
        raise NotImplementedError
    
    def end(self):
        if self.process:     
            self.process.terminate()
        
    
    def start(self):
        if self.process:
            self.end()
        self.process = Process(target=playsound, args=(self.path, ))
        self.process.start()
        Config.set_song_pid(self.process.pid)

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
