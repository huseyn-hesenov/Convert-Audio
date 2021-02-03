import pyttsx3
#speech engine
engine=pyttsx3.init()
#metni cevir
text="i study national aviation academy in azerbaijan"
engine.say(text)
engine.runAndWait()
#voice
rate=engine.getProperty("rate")
print (rate)