from tkinter import *
from tkinter import filedialog 
from tkinter import simpledialog
import re
import time
import socket
from paramiko import SSHClient
from scp import SCPClient
import subprocess

'''
Listen buddy, I got a few algorithms I gotta change up here and a few features to add.
As a matter afact, I might have to change the entire UI up a bit so this project is going to take awhile.

Hmmm.

But anyway, this was my main project over spring break and i'm pretty stoked to have got it up and running in the 
amount of time I had. So below is the WORKING code for an SCP interface that I personally use for my own file server

Aren't I a spoiled brat

Anyway, Feel free to give me some suggestions on some things to change and whatnot.
Keep in mind that this project is FAR from finished or polish. Enjoy reading.
'''

#Used as a global variable to determine if the data being copied is a directory or file.
if_File = False

#Function used for the IP scanner
def scan():
    #Opens a new tkinter window for the IP scan
    scan = Tk()

    #Sets the title of the window for the IP scan
    scan.title("IP Scan")

    #Sets the demensions of the window for the IP scan
    scan.geometry("150x100")

    #Uses socket (Low level network programming for finding local IPV4 address)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #checking routing tables and local interfaces in order to decide which IP address 
    #to use as source in case one would actually use the socket to send data.
    s.connect(("8.8.8.8", 80))
    
    #Setting pattern for meta programming when we pipe the NMAP scan to resolve IP addresses
    #and hostnames
    pattern = r".lan"

    #Will absolutley come back to this algorithm
    Local_Ip_Address = list(s.getsockname()[0].split("."))
    Local_Ip_Address.pop(len(Local_Ip_Address)-1)
    Local_Ip_Address.append("0")
    '''
    |
    V
    Step 1:     Gets local IP address and splits it into a list EX: 192.168.1.10 => [192, 168, 1, 10]
    Step 2:     Gets rid of the last index [192, 168, 1, 10] => [192, 168, 1]
    Setp 3:     Appends 0, [192, 168, 1] => [192, 168, 1, 0] 
    '''

    #Used to store total IP
    concatinate = ""

    #Will absolutley come back to this algorithm
    for count in range(len(Local_Ip_Address)):
        if(count != len(Local_Ip_Address)-1):
            concatinate += Local_Ip_Address[count] + "."
        else:
            concatinate += Local_Ip_Address[count]
    '''
    |
    V
    Note: Refers local IP address List (refer to above algorithm)
    
    Step 1:     Through every element but the last, concatinates it to empty string with "." 
    Step 2:     appends last element giving us "192.168.1.0" now we can perform an IP scan
    on the local area network.
    '''

    #Performs scan through subprocess and outputs the entire scan to recaller as string
    recaller = subprocess.run(['nmap', '-sn', '{0}/24'.format(concatinate)], check=True, capture_output=True)
    
    #Creates a list with all of the information split at the spaces
    nmap_scan = list(recaller.stdout.decode('utf-8').split(" "))

    #Used to store a list with all of our IP addresses and hostnames from the IP scan
    objects = list()

    #Iterates through our entire Nmap scan list
    #Will absolutley come back to this algorithm
    for count in range(len(nmap_scan)):
        
        #Remember when I created the meta pattern for later in the program? ;)
        if(re.search(pattern, nmap_scan[count])):
            
            #increments the index by 1 (refering to the hostname first) to get the IP address
            #From the Nmap scan and splits it at the () to isolate the IP address.
            IP_Address = list(nmap_scan[count+1].split("("))
            IP_Address_Final = list(IP_Address[1].split(")"))

            #Appends the hostname and IP address to objects list
            objects.append([nmap_scan[count][0:len(nmap_scan[count])-4], IP_Address_Final[0]])
    
    #Closes the socket but this entire function can be programmed better
    s.close()

    #Creates an option to select our host to upload file to
    OPTIONS = list()

    #Iterates through out list of IP addresses and hostnames
    for count in range(len(objects)):

        #Appends the hosts and IP's to the menu on tkinter
        OPTIONS.append(objects[count][0]) 

    #From here on out in the function is the tkinter objects. This is so we can set a text value and retrieve it later 
    variable = StringVar(scan)

    #Setting the default value to the first element in OPTIONS
    variable.set(OPTIONS[0])

    #Creating the actual options menu in the new tkinter window
    w = OptionMenu(scan, variable, *OPTIONS)

    #Packing the options menu in the UI "scan"
    w.pack()

    #This is the function for the button that finalizes the selection
    def ok():

        #Iterates through the objects lists to match our selection
        for count in range(len(objects)):

            #Checks to see if out hostnames match
            if(objects[count][0] == variable.get()):

                #If they do, we call the replacer function (The next function in the code)
                replacer(Ip_Address_Entry, objects[count][1])
                break

    #Creating the button in scan
    button = Button(scan, text="OK", command=ok)

    #Packing it so it appears in the UI
    button.pack()

#This is the replacer function. You give is an entry object and it replaces it with a string (Used alot in the code)
def replacer(tkinter_object, string_to_parse):

    #First, if there is something in the entry it will get rid of it
    tkinter_object.delete(0, len(tkinter_object.get()))

    #Second, it will start from 0 and replace it with the string
    tkinter_object.insert(0, string_to_parse)

#Used to save computer information (Will be updating with an encryption algorithm soon)
def save_file():

    #Stores the username data
    typed_user = Username_Entry.get()

    #Stores the IP data
    typed_ip = Ip_Address_Entry.get()

    #Stores the Password data
    typed_password = Password_Entry.get()

    #Prompts for the name of the file to store the computer data to 
    file_name = simpledialog.askstring("New File", "Enter New File Name:")

    #If there is no name enterd in the ip
    if(file_name == ""):

        #It will save the file as the computers IP address
        file_name = typed_ip

    #After the prompt, we use the subprocess library to create the file in the MasterPannel Directory
    subprocess.run(['touch', '{0}'.format(file_name)])

    #Need to change with a "with" statement, but this opens the file
    file = open(file_name, "w")

    #And writes the data stored in the entry objects 
    file.writelines(["{0}\n".format(typed_ip), "{0}\n".format(typed_user), "{0}\n".format(typed_password)])

    #And then closes the file
    file.close()

#Used to load the computer data stored in the files (Will add decryption algorithm)
def load_file():

    #Asks for the text files (Will change this to new more secure file)
    path_to_load = filedialog.askopenfile(title="Select file",
                    filetypes=(("txt files", "*.txt"),("all files", "*.*")))

    #Opens the file in "read" mode
    file = open(path_to_load.name, "r")

    #Used to reference data stored on file
    referencer = file.readlines()

    #Gets rid of the newline
    referencer = [sub[:-1] for sub in referencer]

    #Stores the objects in a list so we can loop through it and replace the values with the values stored in the file
    object_referencer = [Ip_Address_Entry, Username_Entry, Password_Entry]

    #Iteration through the objects
    for count in range(len(referencer)):

        #Replaces the entry with the data in the file
        replacer(object_referencer[count], referencer[count])

#Used to arm the program with a directory to copy
def arm_directory():

    #References variable path as global
    global path

    #Remember at the beginning of the program? Here it is 
    global is_File

    #Asks for directory to copy
    path = filedialog.askdirectory()

    #Used to isolate the name of the directory
    recaller = list(path.split("/"))

    #Replaces the text above the copy button with the name of the directory
    canvas.itemconfigure(File_Name_Holer, text=recaller[-1])

    #Sets to "Directory mode" by setting this variable to false
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
    window.title("MasterPannel")
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