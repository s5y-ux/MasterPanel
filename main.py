from tkinter import *
from tkinter import filedialog 
from tkinter import simpledialog
import re
import time
import socket
from paramiko import SSHClient
from scp import SCPClient
import subprocess

if_File = False

def scan():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    pattern = r".lan"

    Local_Ip_Address = list(s.getsockname()[0].split("."))
    Local_Ip_Address.pop(len(Local_Ip_Address)-1)
    Local_Ip_Address.append("0")
    concatinate = ""
    for count in range(len(Local_Ip_Address)):
        if(count != len(Local_Ip_Address)-1):
            concatinate += Local_Ip_Address[count] + "."
        else:
            concatinate += Local_Ip_Address[count]

    recaller = subprocess.run(['nmap', '-sn', '{0}/24'.format(concatinate)], check=True, capture_output=True)
    nmap_scan = list(recaller.stdout.decode('utf-8').split(" "))

    objects = []

    for count in range(len(nmap_scan)):
        if(re.search(pattern, nmap_scan[count])):
            IP_Address = list(nmap_scan[count+1].split("("))
            IP_Address_Final = list(IP_Address[1].split(")"))
            objects.append([nmap_scan[count][0:len(nmap_scan[count])-4], IP_Address_Final[0]])
    print(objects)

    s.close()

def btn_clicked():
    print("Feature not added yet")

def replacer(tkinter_object, string_to_parse):
    tkinter_object.delete(0, len(tkinter_object.get()))
    tkinter_object.insert(0, string_to_parse)

def save_file():
    typed_user = Username_Entry.get()
    typed_ip = Ip_Address_Entry.get()
    typed_password = Password_Entry.get()
    file_name = simpledialog.askstring("New File", "Enter New File Name:")
    if(file_name == ""):
        file_name = typed_ip
    subprocess.run(['touch', '{0}'.format(file_name)])
    file = open(file_name, "w")
    file.writelines(["{0}\n".format(typed_ip), "{0}\n".format(typed_user), "{0}\n".format(typed_password)])
    file.close()

def load_file():
    path_to_load = filedialog.askopenfile(title="Select file",
                    filetypes=(("txt files", "*.txt"),("all files", "*.*")))
    file = open(path_to_load.name, "r")
    referencer = file.readlines()
    referencer = [sub[:-1] for sub in referencer]
    object_referencer = [Ip_Address_Entry, Username_Entry, Password_Entry]
    for count in range(len(referencer)):
        replacer(object_referencer[count], referencer[count])

def arm_directory():
    global path
    global is_File
    path = filedialog.askdirectory()
    recaller = list(path.split("/"))
    canvas.itemconfigure(File_Name_Holer, text=recaller[-1])
    is_File = False


def arm():
    global path
    global is_File
    path = filedialog.askopenfile(title="Select file",filetypes=(("txt files", "*.txt"),("all files", "*.*")))
    recaller = list(path.name.split("/"))
    canvas.itemconfigure(File_Name_Holer, text=recaller[-1])
    is_File = True

def fire():
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect("{0}".format(Ip_Address_Entry.get()), username=Username_Entry.get(), password=Password_Entry.get())
     
    scp = SCPClient(ssh.get_transport())
     
    if(is_File):
        scp.put(path.name, recursive=True, remote_path='/home/{0}/Desktop'.format(Username_Entry.get()))
    else:
        scp.put(path, recursive=True, remote_path='/home/{0}/Desktop'.format(Username_Entry.get()))

if __name__ == '__main__':

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
        669.0, 38.0,
        image=background_img)

    img0 = PhotoImage(file = f"img0.png")
    Copy_Button = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = fire,
        relief = "flat")

    Copy_Button.place(
        x = 583, y = 385,
        width = 146,
        height = 54)

    Ip_Address_Entry_img = PhotoImage(file = f"img_textBox0.png")
    Ip_Address_Entry_bg = canvas.create_image(
        235.0, 161.0,
        image = Ip_Address_Entry_img)

    Ip_Address_Entry = Entry(
        bd = 0,
        bg = "#ffffff",
        fg = "#4287f5",
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
        fg = "#4287f5",
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
        fg = "#4287f5",
        show="*",
        highlightthickness = 0)

    Password_Entry.place(
        x = 132.5, y = 398,
        width = 205.0,
        height = 29)

    img1 = PhotoImage(file = f"img1.png")
    File_Button = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = arm,
        relief = "flat")

    File_Button.place(
        x = 534, y = 176,
        width = 119,
        height = 25)

    img2 = PhotoImage(file = f"img2.png")
    Directory_Button = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = arm_directory,
        relief = "flat")

    Directory_Button.place(
        x = 658, y = 176,
        width = 119,
        height = 25)

    img3 = PhotoImage(file = f"img3.png")
    Save_Button = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = save_file,
        relief = "flat")

    Save_Button.place(
        x = 90, y = 36,
        width = 108,
        height = 30)

    img4 = PhotoImage(file = f"img4.png")
    Load_Button = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = load_file,
        relief = "flat")

    Load_Button.place(
        x = 602, y = 36,
        width = 108,
        height = 30)

    img5 = PhotoImage(file = f"img5.png")
    Scan_Button = Button(
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = scan,
        relief = "flat")

    Scan_Button.place(
        x = 353, y = 37,
        width = 108,
        height = 30)

    File_Name_Holer=canvas.create_text(
        656.0, 360.5,
        text = "[File Path]",
        fill = "#0076e3",
        font = ("Ubuntu-Regular", 10))

    window.resizable(False, False)
    window.mainloop()
