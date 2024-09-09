from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\0001\Subject\ENGCE110\termproject\build\assets\frame0")

def op_en():
    from fucntion_en_de import openfile_encryption
    openfile_encryption()

def op_de():
    from fucntion_en_de import openfile_decryption
    openfile_decryption()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def event_encryption_button():
    from fucntion_en_de import encrypt_button_event
    encrypt_button_event()

def event_decryption_button():
    from fucntion_en_de import decrypt_button_event
    decrypt_button_event()

window = Tk()
window.title("CryptoQuest!")
window.geometry("700x550")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 550,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    705.0,
    35.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    340.0,
    35.0,
    360.0,
    550.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    100.0,
    79.0,
    190.0,
    169.0,
    fill="#FFFFFF",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    169.0,
    103.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    536.0,
    105.0,
    image=image_image_2
)

canvas.create_text(
    463.0,
    376.0,
    anchor="nw",
    text="Key To Decryption file",
    fill="#000000",
    font=("Inter", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    536.0,
    407.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=423.5,
    y=395.0,
    width=225.0,
    height=23.0
)

canvas.create_text(
    58.0,
    179.0,
    anchor="nw",
    text="Support file : .txt, .csv, .png, .jpg, .mp3 and .mp4*",
    fill="#000000",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    420.0,
    180.0,
    anchor="nw",
    text="Support file : .txt, .csv, .png, .jpg, .mp3 and .mp4*",
    fill="#000000",
    font=("Inter", 10 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    172.0,
    350.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=59.5,
    y=338.0,
    width=225.0,
    height=23.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=op_en
)

button_1.place(
    x=120.0,
    y=210.0,
    width=100.0,
    height=108.0
)


entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    536.0,
    348.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=423.5,
    y=336.0,
    width=225.0,
    height=23.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    command=op_de,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0
)
button_2.place(
    x=484.0,
    y=208.0,
    width=100.0,
    height=108.0
)

canvas.create_text(
    96.0,
    376.0,
    anchor="nw",
    text="Key To Encryption file",
    fill="#000000",
    font=("Inter", 14 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    168.0,
    407.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=55.5,
    y=395.0,
    width=225.0,
    height=23.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    command=event_encryption_button,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0
)
button_3.place(
    x=81.0,
    y=458.0,
    width=174.0,
    height=57.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    command=event_decryption_button,
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0
)
button_4.place(
    x=452.0,
    y=458.0,
    width=174.0,
    height=57.0
)
window.resizable(False, False)
window.mainloop()
