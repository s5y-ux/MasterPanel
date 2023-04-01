from tkinter import *
from tkinter import filedialog 
from tkinter import simpledialog
import time
from paramiko import SSHClient
from scp import SCPClient

import os
win = Tk() 
win.geometry("200x200")
w = Label(win, text="SSH Client Prototype").pack()

def select():
	path = filedialog.askopenfile(title="Select file",
                    filetypes=(("txt files", "*.txt"),("all files", "*.*")))
	print(path.name)
	print(ipaddress.get())

	ssh = SSHClient()
	ssh.load_system_host_keys()
	ssh.connect("{0}".format(ipaddress.get()), username=Username.get(), password=Password.get())
	 
	scp = SCPClient(ssh.get_transport())
	 
	scp.put(path.name, recursive=True, remote_path='/home/{0}/Desktop'.format(Username.get()))

a = Button(win, text="Select File...", command=select).pack()

Label(win, text="Ip Address:").pack()
ipaddress = Entry(win);
ipaddress.pack()

Label(win, text="Username:").pack()
Username = Entry(win);
Username.pack()


Label(win, text="Password:").pack()
Password = Entry(win);
Password.pack()

def replacer(tkinter_object, string_to_parse):
	tkinter_object.delete(0, len(tkinter_object.get()))
	tkinter_object.insert(0, string_to_parse)

def load_file():
	path_to_load = filedialog.askopenfile(title="Select file",
                    filetypes=(("txt files", "*.txt"),("all files", "*.*")))
	file = open(path_to_load.name, "r")
	referencer = file.readlines()
	referencer = [sub[:-1] for sub in referencer]
	print(referencer)
	object_referencer = [ipaddress, Username, Password]
	for count in range(len(referencer)):
		replacer(object_referencer[count], referencer[count])

def save_file():
	typed_user = Username.get()
	typed_ip = ipaddress.get()
	typed_password = Password.get()
	file_name = simpledialog.askstring("New File", "Enter New File Name:")
	if(file_name == ""):
		file_name = typed_ip
	print(typed_ip, typed_user, typed_password)
	print(file_name)
	

file_save = Button(win, text="Save File", command = save_file)
file_load = Button(win, text="Load File", command = load_file)
file_load.pack(side = RIGHT)
file_save.pack(side = LEFT)

win.mainloop()