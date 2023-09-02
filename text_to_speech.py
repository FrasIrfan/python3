from gtts import gTTS
import os

# Input text that you want to convert to speech
text = input("Enter text to speak: ")

# Create a gTTS object
tts = gTTS(text)

# Save the speech to an audio file
file_name = input("Enter the filename to be saved: ")
tts.save(file_name)
