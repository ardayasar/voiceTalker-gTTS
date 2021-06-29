# voiceTalker-gTTS
A voice talker with manual input. gTTS used to make this python file.

### How to Use
Firstly we need to install important modules which is gTTS. You can simply install the module with `pip install gTTS`.
After starting the python (`./voiceTalker.py`) you can type the words you want to.

### !Important!
If your language is not English and you want your language to work, change the code inside `tts = gTTS(text=data, lang='en')` where `en` with your language.
!If you get any error, you can see it from error.log!

### How it works
Code | Explanation
------------ | -------------
`data = input("What should I say?: ")` | Gets the input from terminal.
`tts = gTTS(text=data, lang='en')` | Creates the voice from input.
`tts.save(data[0]+".mp3")` | Creates the .mp3 file with first letter of sentence.
`os.system("start " + data[0]+".mp3")` | Starts the mp3 file to talk.
`time.sleep(1)` | Stops the program for a second so it waits until finishing.
