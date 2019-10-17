from gtts import gTTS
import pygame
import tessOCR
import glob
import os
pygame.mixer.init()

def OcrTTS():
    tts_list=[]
    try:
        file='audio.mp3'
        seperator=','
        txt=tessOCR.Detect()
        txt=seperator.join(txt)
        print(txt)
        tts=gTTS(txt,lang='en')
        tts.save(file)
        print('file saved')
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            pass
        print('over')
        print('New session')
        
        
    except:
        print('No text found')
        pygame.mixer.music.load('fail.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            pass
        print('New session')
        pass



##OcrTTS()
