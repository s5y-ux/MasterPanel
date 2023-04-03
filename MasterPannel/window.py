from tkinter import *
from tkinter import filedialog 
from tkinter import simpledialog
import time
from paramiko import SSHClient
from scp import SCPClient
import subprocess


def btn_clicked():
    print("Button Clicked")

def arm():
	path = filedialog.askopenfile(title="Select file",
                    filetypes=(("txt files", "*.txt"),("all files", "*.*")))
	'''ssh = SSHClient()
	ssh.load_system_host_keys()
	ssh.connect("{0}".format(Ip_Address_Entry.get()), username=Username_Entry.get(), password=Password_Entry.get())
	scp = SCPClient(ssh.get_transport())'''
	recaller = list(path.name.split("/"))
	canvas.itemconfigure(file_name_holer, text=recaller[-1])

window = Tk()

window.geometry("800x500")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 500,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    416.0, 203.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
Copy_Button = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

Copy_Button.place(
    x = 536, y = 373,
    width = 146,
    height = 54)

Ip_Address_Entry_img = PhotoImage(file = f"img_textBox0.png")
Ip_Address_Entry_bg = canvas.create_image(
    235.0, 161.0,
    image = Ip_Address_Entry_img)

Ip_Address_Entry = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

Ip_Address_Entry.place(
    x = 132.0, y = 147,
    width = 206.0,
    height = 28)

Username_Entry_img = PhotoImage(file = f"img_textBox1.png")
Username_Entry_bg = canvas.create_image(
    235.0, 286.0,
    image = Username_Entry_img)

Username_Entry = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

Username_Entry.place(
    x = 132.0, y = 272,
    width = 206.0,
    height = 28)

Password_Entry_img = PhotoImage(file = f"img_textBox2.png")
Password_Entry_bg = canvas.create_image(
    235.0, 411.5,
    image = Password_Entry_img)

Password_Entry = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0,
    show="*")

Password_Entry.place(
    x = 132.5, y = 398,
    width = 205.0,
    height = 29)

img1 = PhotoImage(file = f"img1.png")
File_Select_Button = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = arm,
    relief = "flat")

File_Select_Button.place(
    x = 549, y = 144,
    width = 119,
    height = 25)

img2 = PhotoImage(file = f"img2.png")
Save_Button = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

Save_Button.place(
    x = 90, y = 36,
    width = 108,
    height = 30)

img3 = PhotoImage(file = f"img3.png")
Load_Button = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

Load_Button.place(
    x = 602, y = 36,
    width = 108,
    height = 30)

file_name_holer = canvas.create_text(
    609.0, 348.5,
    text = "[File Path]",
    fill = "#000000",
    font = ("Ubuntu-Regular", 9))

window.resizable(False, False)
window.mainloop()
