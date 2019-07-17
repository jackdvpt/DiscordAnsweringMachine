from gtts import gTTS
from playsound import playsound
import os
import time
from time import gmtime, strftime

def play(string):
    name = strftime("%Y%m%d%H%M%S", gmtime())
    tts = gTTS(string, 'en-au')
    tts.save(name+".mp3")
    playsound(name+".mp3")
    time.sleep(1)
    os.remove(name+".mp3")

if __name__ == '__main__':
    play("hello World")
