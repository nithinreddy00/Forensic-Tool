import tkinter as tk
import platform
from tkinter import *
from tkinter.filedialog import asksaveasfilename
import wmi
import winreg
import os
import psutil
import datetime
import pickle


def load_frame0():
 clear_widgets(frame0)
 clear_widgets(frame1)
 frame0.tkraise()
 frame0.pack_propagate(False)
 tk.Label(frame0, 
            text="Welcome to Forensic Tool",
            bg="#ada489",
            fg="#66461f",
            font=("TkMenuFont",20)
            ).pack(pady=15)
 tk.Button(
        frame0,
        text="Device Forensic",
        font=("TkHeadingFont",14),
        bg="#66461f",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame1()
    ).pack(pady=15)
 tk.Button(
        frame0,
        text="Quit",
        font=("TkHeadingFont",14),
        bg="#66461f",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:root.destroy()
    ).pack(pady=15)
   


def load_frame1():
    
    frame1.tkraise()
    frame1.pack_propagate(False)
    for frame in (frame1,frame2,frame3,frame4) :
        clear_widgets(frame)

    #button widget
    tk.Button(
        frame1,
        text="Stand Alone check",
        font=("TkHeadingFont",14),
        bg="#66461f",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame2()
    ).pack(pady=15)
    
    tk.Button(
        frame1,
        text="Network Check",
        font=("TkHeadingFont",14),
        bg="#66461f",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame3()
    ).pack(pady=15)

    tk.Button(
        frame1,
        text="Full PC Check",
        font=("TkHeadingFont",14),
        bg="#66461f",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame4()
    ).pack(pady=15)
    button3=tk.Button(
        frame1,
        text="Back",
        font=("TkHeadingFont",14),
        bg="#66461f",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame0()
    ).pack(pady=15)
    


# def display_string():
#     result = stand_alone()
#     return result


def load_frame2():                  # standlone-button1,2
    frame2.pack_propagate(False)
    clear_widgets(frame1)
    #clear_widgets(frame2)
    frame2.tkraise()
    label=tk.Label(frame2,text=" ",font=("Arial", 12),bg="#66461f")
    label.config(text=stand_alone())
    label.config(justify="left",wraplength=300,relief="flat"                 
                 
                 ,borderwidth=8)
    label.pack(padx=20, pady=20)
   # text=tk.Text(frame2)
   # text.insert(tk.END, stand_alone())
   # text.configure(tabs="10")
   # text.pack()
    tk.Button(
        frame2,
        text="Back",
        font=("TkHeadingFont",14),
        bg="#66461f",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame1()
    ).pack(padx=20,pady=20)
    #button1.place(x=200,y=500)
    tk.Button(
        frame2,
        text="Save",
        font=("TkHeadingFont",14),
        bg="#66461f",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:save_file1()
    ).pack(padx=20,pady=20)
    #button2.place(x=280,y=500)
    

def load_frame3():                      # network-button3,4
    clear_widgets(frame1)
    frame3.tkraise()
    label=tk.Label(frame3,text=" ",font=("Arial", 6),bg="#66461f")
    label.config(text=network())
    label.config(justify="left",wraplength=300,relief="flat",borderwidth=8)
    label.pack(padx=20, pady=20)
    button3=tk.Button(
        frame3,
        text="Back",
        font=("TkHeadingFont",14),
        bg="#66461f",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame1()
    )
    button3.place(x=200,y=500)
    button4=tk.Button(
        frame3,
        text="Save",
        font=("TkHeadingFont",14),
        bg="#66461f",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:save_file2()
    )
    button4.place(x=280,y=500)

def load_frame4():                      # full pc-button 5,6
    clear_widgets(frame1)
    frame4.tkraise()
    button5=tk.Button(
        frame4,
        text="Back",
        font=("TkHeadingFont",14),
        bg="#66461f",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame1()
    )
    button5.place(x=200,y=500)
    button6=tk.Button(
        frame4,
        text="Save",
        font=("TkHeadingFont",14),
        bg="#66461f",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:save_file3()
    )
    button6.place(x=280,y=500)
#os_version = platform.platform()
#latest_antivirus_version = get_latest_antivirus_version()
def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

#def stand_alone():
#    os_version = platform.platform()
    #hii="nithin"
#    os_ve=["os_version"]

    
    #hello="sai"
    #return os_version
    #osdict = {
    #    "osversion" : "os_version"
    #    #"hi" : "hii"
    #    #"hello" : "hello"
    #}
#    return os_ve
    #print("Current OS Version:", os_version)

def network():
    network1="hii"
    return network1
def full_pc():
    pc="full pc analytics"
    return pc



def save_file1():
    filepath= asksaveasfilename(defaultextension='.txt',filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if not filepath:
        return
    with open(filepath,mode='w',encoding='utf-8') as output_file:
        text=stand_alone()
        #pickle.dump(text,output_file)      #text is a string
        output_file.write(text) # a string should be passed
        root.title('Forensic Tool ')
def save_file2():
    filepath= asksaveasfilename(defaultextension='.txt',filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if not filepath:
        return
    with open(filepath,mode='w',encoding='utf-8') as output_file:
        text2=network()      #text is a string
        output_file.write(text2) # a string should be passed
        root.title('Forensic Tool ')
def save_file3():
    filepath= asksaveasfilename(defaultextension='.txt',filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if not filepath:
        return
    with open(filepath,mode='w',encoding='utf-8') as output_file:
        text=full_pc()      #text is a string
        output_file.write(text) # a string should be passed
        root.title('Forensic Tool ')


def detect_antivirus():
    antivirus_keys = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        r"SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall",  # For 64-bit systems
    ]
    antivirus_names = set()

    if platform.system() == "Windows":
        try:
            for key in antivirus_keys:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key) as reg_key:
                    for i in range(winreg.QueryInfoKey(reg_key)[0]):
                        subkey_name = winreg.EnumKey(reg_key, i)
                        with winreg.OpenKey(reg_key, subkey_name) as subkey:
                            try:
                                display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                                if "antivirus" in display_name.lower() or "security" in display_name.lower():
                                    antivirus_names.add(display_name)
                            except Exception:
                                pass

            if antivirus_names:
                return "Antivirus software detected:\n" + "\n".join(antivirus_names)
            else:
                return "No antivirus software detected."
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        return "This script is for Windows only."


def is_antivirus_updated():
  latest_antivirus_version = get_latest_antivirus_version()
def get_latest_antivirus_version():
  latest_antivirus_version = "1.1.22080.1"
  return latest_antivirus_version
def antivirus():
  if __name__ == "__main__":
    if is_antivirus_updated():
      return("Antivirus is up to date.")
    else:
      return("Antivirus is not up to date.")
antivirus_info = detect_antivirus()


def get_number_of_external_devices():
  # Get the list of all USB devices.
  usb_devices = wmi.WMI().Win32_USBHub()

  # Count the number of external devices.
  number_of_external_devices = 0
  for usb_device in usb_devices:
    if usb_device.DeviceID.startswith("USBSTOR"):
      number_of_external_devices += 1

  return number_of_external_devices
def current_number_of_external_devices():
  if __name__ == "__main__":
   return("Number of External Devices are:" + str(get_number_of_external_devices()))



def find_exe_files(directory):
    exe_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.exe'):
                exe_files.append(os.path.join(root, file))

    return exe_files
def list_of_exe_files():
     if __name__ == "__main__":
         directory_to_search = "C:\\"
         exe_files = find_exe_files(directory_to_search)

         if exe_files:
            listofexe=[]
        #listofexe=["List of .exe files :"]
            for exe_file in exe_files:
                listofexe.append(exe_file)
            return str(listofexe)
         else:
            #xy=["No .exe files found in the specified directory."]
            #listofexe+xy
            return ("nO")


def get_system_boot_up_timestamp():
  boot_time = psutil.boot_time()
  boot_time_readable = datetime.datetime.fromtimestamp(boot_time).strftime("%Y-%m-%d %H:%M:%S")

  return boot_time_readable
def timestamps():
  if __name__ == "__main__":
   
   xyz=("The System Boot-up Time stamps are :"+ get_system_boot_up_timestamp())
   return(xyz)



import os 
import platform
def get_system_metadata():
    # System information
    system_info = {
        "Platform": platform.platform(),
        "OS Name": os.name,
        "OS Release": platform.release(),
        "OS Version": platform.version(),
        "Architecture": platform.architecture(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),

    }
    info_str = "\n".join([f"{key}: {value}" for key, value in system_info.items()])

    return ("META DATA:\n" + info_str)
def sysinfo():
   if __name__ == "__main__":
    systm_info = get_system_metadata()
    return systm_info
    


import os
import time

def list_updated_files_as_string(directory):
    reference_time = time.mktime(time.strptime("2023-01-01", "%Y-%m-%d"))
    updated_files = []

    for root, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            modified_time = os.path.getmtime(file_path)

            if modified_time > reference_time:
                updated_files.append(file_path)

    if updated_files:
        result = "Updated files:\n"
        result += "\n".join(updated_files)
    else:
        result = "Status of updated files: No updated files found."

    return result

def listofupdated ():
   if __name__ == "__main__":
    directory_to_monitor = "C:\\Path\\To\\Directory"
    updated_files_string = list_updated_files_as_string(directory_to_monitor)
    return(updated_files_string)







def stand_alone():
    os_version = platform.platform()
    text=["OS Version: "+os_version]
    antivirus_info = detect_antivirus()
    antiviruss=antivirus()
    no_of_externaldev=current_number_of_external_devices()
    #exefiles=list_of_exe_files()
    timestamp=timestamps()
    sys_info=sysinfo()
    updatedfiles=listofupdated()
    text.append(antivirus_info)
    text.append(antiviruss)
    text.append(no_of_externaldev)
    #text.append(exefiles)
    text.append(timestamp)
    text.append(sys_info)
    text.append(updatedfiles)
    # lines = text.splitlines()
    # for line in lines:
    #  return ("\t" + line)
    return ('\n'.join(text))



import subprocess

def get_installed_programs():
    try:
        data = subprocess.check_output(['wmic', 'product', 'get', 'name'], stderr=subprocess.STDOUT, text=True)
        program_list = data.strip().split("\n")[1:]
        return (program_list)
    except subprocess.CalledProcessError as e:
        return "Error: " + e.output.strip()

def installed_programs():
   if __name__ == "__main__":
    installed_programs = get_installed_programs()
    return(installed_programs)




def network():
   text2=installed_programs()
   return ('\n'.join(text2))
   


#intiallize app
root = tk.Tk()
root.title("Forensic Tool")
#root.eval("tk::PlaceWindow . center")
#create a frame widget
frame0=tk.Frame(root,width = 900, height =700 ,bg="#ada489")
frame1=tk.Frame(root, width = 900, height =700 ,bg="#ada489")

frame2=tk.Frame(root, bg="#ada489")


frame3=tk.Frame(root, bg="#ada489")


frame4=tk.Frame(root, bg="#ada489")


for frame in (frame0,frame1,frame2,frame3,frame4):
    frame.grid(row=0,column=0, sticky='nesw')
    



load_frame0()


#run app
root.mainloop()
