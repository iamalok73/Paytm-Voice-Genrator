import pygame as py
from gtts import gTTS
py.init()

def Paytm(amount):
    txt  = f" Paytm per {amount}rs Prapt huye, Thank you.."
    msg = gTTS(txt)
    msg.save("audio.mp3")
    gana = py.mixer.Sound("audio.mp3")
    gana.play()
    
    
    
print(Paytm(100))