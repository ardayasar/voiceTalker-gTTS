import time
from gtts import gTTS
import os
error_log = os.getcwd() + "\error.log"


while True:
    try:
        data = input("What should I say?: ")
        tts = gTTS(text=data, lang='tr')
        tts.save(data[0]+".mp3")
        os.system("start " + data[0]+".mp3")
        time.sleep(1)
    except ValueError:
        open("error.log", "a").write(ValueError + "\n")
        print(f'Problem written in the file: "{error_log}"')
