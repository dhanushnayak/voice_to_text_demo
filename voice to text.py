import speech_recognition as sr  
import pyttsx3 as pt
engine = pt.init()
engine.setProperty('rate', 125)     
# get audio from the microphone                                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source,timeout=10)   

engine.say('Recorded')
engine.runAndWait()
try:
    print("You said " + r.recognize_google(audio))
    a= r.recognize_google(audio)
    engine.say("You said "+a)
    engine.runAndWait()
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))


engine.stop()