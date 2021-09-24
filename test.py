import tkinter as tk
from tkinter import filedialog
from PIL import Image

watermark = Image.open("image/image_7.jpg")


def browse_for_image():
    chosen_image = tk.filedialog.askopenfilename(title="Choose a file")
    return chosen_image


def add_watermark():
    file = browse_for_image()
    image = Image.open(file)
    img_x = image.size[0]
    img_y = image.size[1]
    mark_x = watermark.size[0]
    mark_y = watermark.size[1]
    box = (img_x - mark_x, img_y - mark_y, img_x, img_y)
    watermark.convert("RGBA")
    paste_mask = watermark.split()[3].point(lambda i: i * 50 / 100)
    image.paste(watermark, box, mask=paste_mask)
    image.show()


# config the window
window = tk.Tk()
window.title("WaterMark Adder")
window.geometry("400x100")


# Title label:
select_img_label = tk.Label(text="Select a photo:")
select_img_label.pack()
select_img_button = tk.Button(text="Add watermark", command=add_watermark)
select_img_button.pack()


window.mainloop()