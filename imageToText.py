from gtts import gTTS
import os
import pytesseract as tess
from PIL import Image

tess.pytesseract.tesseract_cmd = r'C:\Users\sadiya rafiq\AppData\Local\Tesseract-OCR\tesseract.exe'


img = Image.open('camera.jpg')
mytext1 = tess.image_to_string(img)

#write output in file
with open('abc.txt', mode='w') as file:
    file.write(mytext1)
    print(mytext1)

# Language we want to use
language = 'en'

myobj = gTTS(text=mytext1, lang=language, slow=False)

myobj.save("output.mp3")
# Play the converted file
os.system("start output.mp3")