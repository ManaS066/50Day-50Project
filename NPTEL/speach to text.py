import speech_recognition as sr
AUDIO_FILE = "song.wav"
r= sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio =  r.record(source)
#read audio file
try:
    print("Audio file contain "+r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google speach recognition could not undersatnd ")
except sr.RequestError:
    print("could not get result")

