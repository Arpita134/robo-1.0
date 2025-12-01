import os
from gtts import gTTS
from playsound import playsound

print("welcome to robo speaker 1.0")

while True:
   x=input("enter what you want to pronounce:")
   if x.lower()=="quit":
      break

   lang=input("Enter language code(ex: en, hi, bn, ta ):")

   tts=gTTS(text=x, lang=lang)
   filename="voice.mp3"
   tts.save(filename)

   playsound(filename)
   os.remove(filename)