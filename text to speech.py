# text to speech
# !pip install audiobook
# pip install pyttsx3

from audiobook import AudioBook
ab = AudioBook(r'C:\Users\sshar127\Desktop\Learning\Data Science\DATA SCIENCE Day 01.pdf')
ab.text_to_speech()
