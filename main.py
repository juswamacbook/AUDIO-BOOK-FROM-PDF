import pyttsx3
import PyPDF2
from tkinter.filedialog import *

#read from pdf file
book = askopenfilename()
pdfreader = PyPDF2.PdfReader(book)

#get # of pages from pdf file
pages = len(pdfreader.pages)

#read all the data from the pages
for num in range(0, pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()
