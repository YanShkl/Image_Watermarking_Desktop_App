import tkinter
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageDraw, ImageFont

# ---------------------------- CONSTANTS ------------------------------- #

BLUE = "#00477B"
WHITE = "white"

# ---------------------------- DATAs ------------------------------- #

OptionList = [
"Blue",
"Green",
"White",
"Orange",
"Grey",
"Black",
"Purple",
]

color_dict = {'Blue': "#00477B",
              'Green': '#008000',
              'White': 'white',
              'Orange': '#f29202',
              'Grey': '#808080',
              'Black': '#000000',
              'Purple': '#800080'
              }
# ---------------------------- FUNCTIONS ------------------------------- #


def browseFiles():

    filename = filedialog.askopenfilename()
    image = Image.open(filename)
    width, height = image.size

    draw = ImageDraw.Draw(image)
    text = input_text.get()
    font = ImageFont.truetype("Raleway-Black.ttf",100)
    textwidth, textheight = draw.textsize(text, font)

    watermark_color = variable.get()
    color = color_dict.get(f'{watermark_color}')

    margin = 20
    x_watermark = width - textwidth - margin
    y_watermark = height - textheight - margin
    draw.text((x_watermark, y_watermark), text, font=font,fill=color )
    image.show()
    image.save('watermark.png')



def display_selected(choice):
    choice = variable.get()
    print(choice)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Image Watermarking Desktop App")

window.minsize(width = 200, height = 450)
window.config(background = BLUE, padx=100, pady=10, bg = BLUE)

label = tkinter.Label(text = "The Watermarker App", font = ("Courier", 56), foreground = WHITE, background = BLUE, pady=20)
label.grid(column=1, row=0)


label_instructions = Label(text = "Please enter watermark text, below.\nAfter selecting image for watermarking, watermarked image will be saved as\n'watermarked.png' in the current directory.\n", font = ("Courier", 15), foreground = WHITE, background = BLUE)
label_instructions.grid(column=1, row=1)


input_text = Entry(width = 35, font='Aerial', )
input_text.focus()
input_text.grid(column=1, row=2)

select_photo_button = tkinter.Button(text='Browse image', command=browseFiles, height=2, width=15)
select_photo_button.grid(pady=10, column=1, row=4)

# setting variable for Integers
variable = StringVar()
variable.set(OptionList[3])

# creating widget
dropdown = OptionMenu(
    window,
    variable,
    *OptionList,
    command=display_selected
)
dropdown.grid(column=1, row=3, pady=20)


dropdown_label = tkinter.Label(text = "Choose watermark color:", font = ("Courier", 12), foreground = WHITE, background = BLUE, pady=20)
dropdown_label.place(x=170, y =242)


# ---------------------------- APP ------------------------------- #

window.mainloop()
