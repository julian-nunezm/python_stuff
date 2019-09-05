#!pip3 install keras

from tensorflow.keras.preprocessing.text import text_to_word_sequence as ttws

text = "This is a good day y/n? Please restart or reset reset reset your url (http://google.com)"

result = set(ttws(text))

print(result)
