# Tlil 02/04/2020
# This program reads the text from the image placed in the current directory, 'image.png'
# It extracts the text and writes it to extracted.txt. Then it translates it to Swahili and
# reads it aloud

# Convert image to text string
import pytesseract

# add image processing capabilities
from PIL import Image

# convert text to speech
import pyttsx3

# translate into english
from googletrans import Translator

# path to tesseract command
pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# open the image
img = Image.open('image.png')

# describe image format in the output
print(img)

result = pytesseract.image_to_string(img)

# write text in a text file and save it to source path
with open('extracted.txt',mode = 'w') as file:

          file.write(result)
          print(result)

p = Translator()

# translate the text into Swahili
k = p.translate(result,dest='swahili')
print(k)
engine = pyttsx3.init()

# an audio will be played speaking the text if pytesseract recognizes it
engine.say(k)
engine.runAndWait()
