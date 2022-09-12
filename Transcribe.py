import speech_recognition as sr
from os import path
from pydub import AudioSegment

AudioSegment.from_file("C:\Users\Manish\Downloads\Video\test.mp4").export("output.mp3", format="mp3")
sound = AudioSegment.from_mp3("output.mp3")
audio_file = "transcript.wav"
sound.export(audio_file, format='wav')
r = sr.Recognizer()
with sr.AudioFile(audio_file) as source:
    audio = r.record(source)
text = r.recognize_google(audio)
print(text)
with open("transcript.txt", "w") as F:
    F.write(text)
F.close()
