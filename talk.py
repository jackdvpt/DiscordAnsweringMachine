from gtts import gTTS
from playsound import playsound
import os
import time
from time import gmtime, strftime

def play(string, who):
    name = strftime("%Y%m%d%H%M%S", gmtime())
    talk = who+" says " + string
    tts = gTTS(talk, 'en-au')
    tts.save(name+".mp3")
    playsound("ring.wav")
    playsound(name+".mp3")
    time.sleep(3)
    os.remove(name+".mp3")

if __name__ == '__main__':
    play("hello World")
