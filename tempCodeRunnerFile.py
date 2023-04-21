import pyttsx3
engine = pyttsx3.init()
answer = input("what u what to convert to speech?");
engine.say(answer)
engine.runAndWait()