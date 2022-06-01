import pyttsx3
import PyPDF2

from tkinter.filedialog import *

livre = askopenfilename()
lecteur = PyPDF2.PdfFileReader(livre)
pages = lecteur.numPages

for num in range(0, pages):
    page = lecteur.getPage(num)
    text = page.extractText()
    lire = pyttsx3.init()
    lire.say(text)
    lire.runAndWait()
    
