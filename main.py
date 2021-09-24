import requests
from tkinter import *
from tkinter import filedialog
from PyPDF2 import PdfFileReader

url = "http://api.ispeech.org/api/rest"
api_key = "	77957b2d668d6c9b2be62ffbed813f0d"


def open_file():
    """Open PDF file"""
    file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    return file


def read_file():
    """Get the file and change from PDF to text in Tkinter TextBox"""
    filename = open_file()
    reader = PdfFileReader(filename)
    pageObj = reader.getNumPages()
    for page_count in range(pageObj):
        page = reader.getPage(page_count)
        page_data = page.extractText()
        text_box.insert(END, page_data)

def convert():
    content = text_box.get(1.0, "end-1c")
    response = requests.get(url=url, params={"apikey": api_key,
                                             "action": "convert",
                                             "text": content,
                                             "format": "mp3",
                                             "filename":"audio_file"})
    with open("audio_file.mp3", "wb") as file:
        file.write(response.content)


windows = Tk()
windows.title("PDF to Audiobook")
windows.geometry("500x500")
# windows.withdraw()
# open_pdf = Label(text="Select File : ")

scrollbar = Scrollbar(windows)
scrollbar.pack(side=RIGHT, fill=Y)

text_box = Text(windows, height=25, width=50, yscrollcommand=scrollbar.set)
text_box.pack()

open_button = Button(windows, text="Choose PDF File", command=read_file).pack(side=TOP,pady=10)
convert_button = Button(windows, text="Convert", command=convert).pack(side=BOTTOM, pady=5)

windows.mainloop()
