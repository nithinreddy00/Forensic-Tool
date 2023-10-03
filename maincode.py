# import tkinter as tk
# import platform
# from tkinter import *
# from tkinter.filedialog import asksaveasfilename
# import wmi
# import winreg
# import os
# import psutil
# import datetime
# import pickle


# def load_frame0():
#  clear_widgets(frame0)
#  clear_widgets(frame1)
#  frame0.tkraise()
#  frame0.pack_propagate(False)
#  tk.Label(frame0, 
#             text="Welcome to Forensic Tool",
#             bg="#ada489",
#             fg="#66461f",
#             font=("TkMenuFont",20)
#             ).pack(pady=15)
#  tk.Button(
#         frame0,
#         text="Device Forensic",
#         font=("TkHeadingFont",14),
#         bg="#66461f",
#         fg="white",
#         cursor="hand2",
#         activebackground="#badee2",
#         activeforeground="black",
#         command=lambda:load_frame1()
#     ).pack(pady=15)
#  tk.Button(
#         frame0,
#         text="Quit",
#         font=("TkHeadingFont",14),
#         bg="#66461f",
#         fg="white",
#         cursor="hand2",
#         activebackground="#badee2",
#         activeforeground="black",
#         command=lambda:root.destroy()
#     ).pack(pady=15)
   


# def load_frame1():
    
#     frame1.tkraise()
#     frame1.pack_propagate(False)
#     for frame in (frame1,frame2,frame3,frame4) :
#         clear_widgets(frame)

#     #button widget
#     tk.Button(
#         frame1,
#         text="Stand Alone check",
#         font=("TkHeadingFont",14),
#         bg="#66461f",
#         fg="white",
#         cursor="hand2",
#         activebackground="#badee2",
#         activeforeground="black",
#         command=lambda:load_frame2()
#     ).pack(pady=15)
    
#     tk.Button(
#         frame1,
#         text="Network Check",
#         font=("TkHeadingFont",14),
#         bg="#66461f",
#         fg="white",
#         cursor="hand2",
#         activebackground="#badee2",
#         activeforeground="black",
#         command=lambda:load_frame3()
#     ).pack(pady=15)

#     tk.Button(
#         frame1,
#         text="Full PC Check",
#         font=("TkHeadingFont",14),
#         bg="#66461f",
#         fg="white",
#         cursor="hand2",
#         activebackground="#badee2",
#         activeforeground="black",
#         command=lambda:load_frame4()
#     ).pack(pady=15)
#     button3=tk.Button(
#         frame1,
#         text="Back",
#         font=("TkHeadingFont",14),
#         bg="#66461f",
#         fg="white",
#         cursor="hand2",
#         activebackground="#badee2",
#         activeforeground="black",
#         command=lambda:load_frame0()
#     ).pack(pady=15)
    


# # def display_string():
# #     result = stand_alone()
# #     return result


# def load_frame2():                  # standlone-button1,2
#     frame2.pack_propagate(False)
#     clear_widgets(frame1)
#     #clear_widgets(frame2)
#     frame2.tkraise()
#     label=tk.Label(frame2,text=" ",font=("Arial", 12),bg="#66461f")
#     label.config(text=stand_alone())
#     label.config(justify="left",wraplength=300,relief="flat"                 
                 
#                  ,borderwidth=8)
#     label.pack(padx=20, pady=20)
#    # text=tk.Text(frame2)
#    # text.insert(tk.END, stand_alone())
#    # text.configure(tabs="10")
#    # text.pack()
#     tk.Button(
#         frame2,
#         text="Back",
#         font=("TkHeadingFont",14),
#         bg="#66461f",
#         fg="white",
#         cursor="hand2",
#         activebackground="#badee2",
#         activeforeground="black",
#         command=lambda:load_frame1()
#     ).pack(padx=20,pady=20)
#     #button1.place(x=200,y=500)
#     tk.Button(
#         frame2,
#         text="Save",
#         font=("TkHeadingFont",14),
#         bg="#66461f",
#         fg="white",
#         cursor="hand2",
#         activebackground="#badee2",
#         activeforeground="black",
#         command=lambda:save_file1()
#     ).pack(padx=20,pady=20)
#     #button2.place(x=280,y=500)
    

# def load_frame3():                      # network-button3,4
#     clear_widgets(frame1)
#     frame3.tkraise()
#     label=tk.Label(frame3,text=" ",font=("Arial", 6),bg="#66461f")
#     label.config(text=network())
#     label.config(justify="left",wraplength=300,relief="flat",borderwidth=8)
#     label.pack(padx=20, pady=20)
#     button3=tk.Button(
#         frame3,
#         text="Back",
#         font=("TkHeadingFont",14),
#         bg="#66461f",
#         fg="white",
#         cursor="hand2",
#         activebackground="#badee2",
#         activeforeground="black",
#         command=lambda:load_frame1()
#     )
#     button3.place(x=200,y=500)
#     button4=tk.Button(
#         frame3,
#         text="Save",
#         font=("TkHeadingFont",14),
#         bg="#66461f",
#         fg="white",
#         cursor="hand2",
#         activebackground="#badee2",
#         activeforeground="black",
#         command=lambda:save_file2()
#     )
#     button4.place(x=280,y=500)

# def load_frame4():                      # full pc-button 5,6
#     clear_widgets(frame1)
#     frame4.tkraise()
#     button5=tk.Button(
#         frame4,
#         text="Back",
#         font=("TkHeadingFont",14),
#         bg="#66461f",
#         fg="white",
#         cursor="hand2",
#         activebackground="#badee2",
#         activeforeground="black",
#         command=lambda:load_frame1()
#     )
#     button5.place(x=200,y=500)
#     button6=tk.Button(
#         frame4,
#         text="Save",
#         font=("TkHeadingFont",14),
#         bg="#66461f",
#         fg="white",
#         cursor="hand2",
#         activebackground="#badee2",
#         activeforeground="black",
#         command=lambda:save_file3()
#     )
#     button6.place(x=280,y=500)
# #os_version = platform.platform()
# #latest_antivirus_version = get_latest_antivirus_version()
# def clear_widgets(frame):
#     for widget in frame.winfo_children():
#         widget.destroy()

# #def stand_alone():
# #    os_version = platform.platform()
#     #hii="nithin"
# #    os_ve=["os_version"]

    
#     #hello="sai"
#     #return os_version
#     #osdict = {
#     #    "osversion" : "os_version"
#     #    #"hi" : "hii"
#     #    #"hello" : "hello"
#     #}
# #    return os_ve
#     #print("Current OS Version:", os_version)

# def network():
#     network1="hii"
#     return network1
# def full_pc():
#     pc="full pc analytics"
#     return pc



# def save_file1():
#     filepath= asksaveasfilename(defaultextension='.txt',filetypes=[("Text Files","*.txt"),("All Files","*.*")])
#     if not filepath:
#         return
#     with open(filepath,mode='w',encoding='utf-8') as output_file:
#         text=stand_alone()
#         #pickle.dump(text,output_file)      #text is a string
#         output_file.write(text) # a string should be passed
#         root.title('Forensic Tool ')
# def save_file2():
#     filepath= asksaveasfilename(defaultextension='.txt',filetypes=[("Text Files","*.txt"),("All Files","*.*")])
#     if not filepath:
#         return
#     with open(filepath,mode='w',encoding='utf-8') as output_file:
#         text2=network()      #text is a string
#         output_file.write(text2) # a string should be passed
#         root.title('Forensic Tool ')
# def save_file3():
#     filepath= asksaveasfilename(defaultextension='.txt',filetypes=[("Text Files","*.txt"),("All Files","*.*")])
#     if not filepath:
#         return
#     with open(filepath,mode='w',encoding='utf-8') as output_file:
#         text=full_pc()      #text is a string
#         output_file.write(text) # a string should be passed
#         root.title('Forensic Tool ')


# def detect_antivirus():
#     antivirus_keys = [
#         r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
#         r"SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall",  # For 64-bit systems
#     ]
#     antivirus_names = set()

#     if platform.system() == "Windows":
#         try:
#             for key in antivirus_keys:
#                 with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key) as reg_key:
#                     for i in range(winreg.QueryInfoKey(reg_key)[0]):
#                         subkey_name = winreg.EnumKey(reg_key, i)
#                         with winreg.OpenKey(reg_key, subkey_name) as subkey:
#                             try:
#                                 display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
#                                 if "antivirus" in display_name.lower() or "security" in display_name.lower():
#                                     antivirus_names.add(display_name)
#                             except Exception:
#                                 pass

#             if antivirus_names:
#                 return "Antivirus software detected:\n" + "\n".join(antivirus_names)
#             else:
#                 return "No antivirus software detected."
#         except Exception as e:
#             return f"Error: {str(e)}"
#     else:
#         return "This script is for Windows only."


# def is_antivirus_updated():
#   latest_antivirus_version = get_latest_antivirus_version()
# def get_latest_antivirus_version():
#   latest_antivirus_version = "1.1.22080.1"
#   return latest_antivirus_version
# def antivirus():
#   if __name__ == "__main__":
#     if is_antivirus_updated():
#       return("Antivirus is up to date.")
#     else:
#       return("Antivirus is not up to date.")
# antivirus_info = detect_antivirus()


# def get_number_of_external_devices():
#   # Get the list of all USB devices.
#   usb_devices = wmi.WMI().Win32_USBHub()

#   # Count the number of external devices.
#   number_of_external_devices = 0
#   for usb_device in usb_devices:
#     if usb_device.DeviceID.startswith("USBSTOR"):
#       number_of_external_devices += 1

#   return number_of_external_devices
# def current_number_of_external_devices():
#   if __name__ == "__main__":
#    return("Number of External Devices are:" + str(get_number_of_external_devices()))



# def find_exe_files(directory):
#     exe_files = []

#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             if file.lower().endswith('.exe'):
#                 exe_files.append(os.path.join(root, file))

#     return exe_files
# def list_of_exe_files():
#      if __name__ == "__main__":
#          directory_to_search = "C:\\"
#          exe_files = find_exe_files(directory_to_search)

#          if exe_files:
#             listofexe=[]
#         #listofexe=["List of .exe files :"]
#             for exe_file in exe_files:
#                 listofexe.append(exe_file)
#             return str(listofexe)
#          else:
#             #xy=["No .exe files found in the specified directory."]
#             #listofexe+xy
#             return ("nO")


# def get_system_boot_up_timestamp():
#   boot_time = psutil.boot_time()
#   boot_time_readable = datetime.datetime.fromtimestamp(boot_time).strftime("%Y-%m-%d %H:%M:%S")

#   return boot_time_readable
# def timestamps():
#   if __name__ == "__main__":
   
#    xyz=("The System Boot-up Time stamps are :"+ get_system_boot_up_timestamp())
#    return(xyz)



# import os 
# import platform
# def get_system_metadata():
#     # System information
#     system_info = {
#         "Platform": platform.platform(),
#         "OS Name": os.name,
#         "OS Release": platform.release(),
#         "OS Version": platform.version(),
#         "Architecture": platform.architecture(),
#         "Machine": platform.machine(),
#         "Processor": platform.processor(),

#     }
#     info_str = "\n".join([f"{key}: {value}" for key, value in system_info.items()])

#     return ("META DATA:\n" + info_str)
# def sysinfo():
#    if __name__ == "__main__":
#     systm_info = get_system_metadata()
#     return systm_info
    


# import os
# import time

# def list_updated_files_as_string(directory):
#     reference_time = time.mktime(time.strptime("2023-01-01", "%Y-%m-%d"))
#     updated_files = []

#     for root, files in os.walk(directory):
#         for file in files:
#             file_path = os.path.join(root, file)
#             modified_time = os.path.getmtime(file_path)

#             if modified_time > reference_time:
#                 updated_files.append(file_path)

#     if updated_files:
#         result = "Updated files:\n"
#         result += "\n".join(updated_files)
#     else:
#         result = "Status of updated files: No updated files found."

#     return result

# def listofupdated ():
#    if __name__ == "__main__":
#     directory_to_monitor = "C:\\Path\\To\\Directory"
#     updated_files_string = list_updated_files_as_string(directory_to_monitor)
#     return(updated_files_string)







# def stand_alone():
#     os_version = platform.platform()
#     text=["OS Version: "+os_version]
#     antivirus_info = detect_antivirus()
#     antiviruss=antivirus()
#     no_of_externaldev=current_number_of_external_devices()
#     #exefiles=list_of_exe_files()
#     timestamp=timestamps()
#     sys_info=sysinfo()
#     updatedfiles=listofupdated()
#     text.append(antivirus_info)
#     text.append(antiviruss)
#     text.append(no_of_externaldev)
#     #text.append(exefiles)
#     text.append(timestamp)
#     text.append(sys_info)
#     text.append(updatedfiles)
#     # lines = text.splitlines()
#     # for line in lines:
#     #  return ("\t" + line)
#     return ('\n'.join(text))



# import subprocess

# def get_installed_programs():
#     try:
#         data = subprocess.check_output(['wmic', 'product', 'get', 'name'], stderr=subprocess.STDOUT, text=True)
#         program_list = data.strip().split("\n")[1:]
#         return (program_list)
#     except subprocess.CalledProcessError as e:
#         return "Error: " + e.output.strip()

# def installed_programs():
#    if __name__ == "__main__":
#     installed_programs = get_installed_programs()
#     return(installed_programs)




# def network():
#    text2=installed_programs()
#    return ('\n'.join(text2))
   


# #intiallize app
# root = tk.Tk()
# root.title("Forensic Tool")
# #root.eval("tk::PlaceWindow . center")
# #create a frame widget
# frame0=tk.Frame(root,width = 900, height =700 ,bg="#ada489")
# frame1=tk.Frame(root, width = 900, height =700 ,bg="#ada489")

# frame2=tk.Frame(root, bg="#ada489")


# frame3=tk.Frame(root, bg="#ada489")


# frame4=tk.Frame(root, bg="#ada489")


# for frame in (frame0,frame1,frame2,frame3,frame4):
#     frame.grid(row=0,column=0, sticky='nesw')
    



# load_frame0()


# #run app
# root.mainloop()





# Network scan libraries

# from ping3 import ping
# from datetime import datetime,timedelta
# import sqlite3
# import shutil
# import os
# import socket
# import subprocess

# # Standalone check libraries
# import platform
# import winreg
# import win32com.client
# import psutil
# from datetime import datetime

# # Tkinter libraries
# import tkinter as tk
# from tkinter import scrolledtext

# #libraries to save as a pdf
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib.pagesizes import inch


# def network():
#     final = "Network Scan \n\n"

#     def network_details():
#         data = "Network Details\n\n"
#         IP = socket.gethostbyname(socket.gethostname())
#         if IP=='127.0.0.1':
#             data += "This PC is not connected to the internet\n"
#             return
#         else:
#             data += 'This PC is connected to the internet through the IP address ' + str(IP) +'\n'

#         data += "Type: "
#         interfaces = psutil.net_if_stats()
#         flag = 0
#         for interface,stats in interfaces.items():
#             if stats.isup:
#                 if 'Wi-Fi' in interface:
#                     data += "Wireless " + interface +"\n"
#                     flag = 1
#                 else:
#                     data += 'Wired '+ interface +"\n"
#                     flag = 2

#         if(flag ==1):
#             data += "SSID Name: "
#             try:
#                 ssid = subprocess.check_output(["netsh", "wlan", "show", "interfaces"]).decode("utf-8").split("\n")
#                 for line in ssid:
#                     if "SSID" in line:
#                         data += line.split(":")[1].strip() 
#             except Exception as e:
#                 return str(e)
#         return data + "\n\n"

#     final += network_details()
#     final += "Network Troubleshooting\n\n"

#     def check_connectivity(host, port):
#         try:
#             # Create a socket object and attempt to connect to the host and port
#             with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#                 s.settimeout(5)  # Set a timeout for the connection attempt
#                 s.connect((host, port))
#             return True
#         except Exception as e:
#             return False

#     # Specify the host and port to check (e.g., a web server)
#     host_to_check = "google.com"
#     port_to_check = 80  # HTTP port

#     # Perform the connectivity check
#     if check_connectivity(host_to_check, port_to_check):
#         final += f"Connection to Host: {host_to_check}, Port: {port_to_check} is successful.\n"
#     else:
#         final += f"Connection to Host: {host_to_check}, Port: {port_to_check} failed.\n"

#     def icmp_ping(host):
#         response_time = ping(host)
#         if response_time is not None:
#             return f"Response time: {response_time} ms\n\n"
#         else:
#             return "Host is unreachable or request timed out\n\n"

#     # Specify the host to ping
#     host_to_ping = "google.com"

#     # Perform ICMP ping
#     result = icmp_ping(host_to_ping)
#     final += result

#     def browser_hist():
#         user = os.getlogin()

#         history_file = r'C:\Users\\'+user+r'\AppData\Local\Microsoft\Edge\User Data\Default\History'
#         copied_history_file = 'copied_web_data.sqlite'
#         shutil.copyfile(history_file, copied_history_file)

#         end_date = datetime.now()
#         start_date = end_date - timedelta(days=7)

#         conn = sqlite3.connect(copied_history_file)
#         cursor = conn.cursor()

#         start_timestamp = int((start_date - datetime(1601, 1, 1)).total_seconds() * 1000000)
#         end_timestamp = int((end_date - datetime(1601, 1, 1)).total_seconds() * 1000000)

#         # Query the database for URLs accessed in the last 7 days
#         cursor.execute("SELECT url, last_visit_time FROM urls WHERE last_visit_time >= ? AND last_visit_time <= ?", (start_timestamp, end_timestamp))
#         history_data = cursor.fetchall()
#         data = ""

#         for row in history_data:
#             url = row[0]
#             timestamp = row[1] / 1000000  # Convert microseconds to seconds
#             visit_time = datetime(1601, 1, 1) + timedelta(seconds=timestamp)

#             data += "Website: "+url+"\n"
#             data += "Date and Time of Access: "+str(visit_time)+"\n"
        
#         conn.close()
#         return data

#     def list_files_downloaded():
#         user = os.getlogin()
#         base_directory = r'C:\Users\\'+ user+'\Downloads'  
#         cutoff_date = datetime.now() - timedelta(days=90)
#         downloaded_files = []
#         data = ""
#         for root, _, files in os.walk(base_directory):
#             for file in files:
#                 file_path = os.path.join(root, file)
#                 file_timestamp = datetime.fromtimestamp(os.path.getmtime(file_path))
#                 if file_timestamp >= cutoff_date:
#                     downloaded_files.append((file_path, file_timestamp))
#                     data += "File Name: " + file_path + " Timestamp: " + str(file_timestamp) + "\n"
#         return data
    
#     browser_history = browser_hist()
#     list_of_files = list_files_downloaded()

#     final +="Browser History\n\n" + browser_history    
#     final +=  "\n\nDownloaded Files History\n\n" + list_of_files
    
#     return  final


# def stand_alone():
#     final = "Stand Alone Scan \n\n"
    
#     def get_system_metadata():
#         system_info = {
#         "OS Name": platform.system(),
#         "OS Release": platform.release(),
#         "OS Version": platform.version(),
#         "Architecture": platform.architecture(),
#         "Machine": platform.machine(),
#         "Processor": platform.processor(),
#         }

#         info_str = "\n".join([f"{key}: {value}" for key, value in system_info.items()])
#         return ("System Information:\n" + info_str + "\n\n")
    
#     def detect_antivirus():
#         antivirus_keys = [
#             r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
#             r"SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall",  # For 64-bit systems
#         ]
#         antivirus_names = set()

#         if platform.system() == "Windows":
#             try:
#                 for key in antivirus_keys:
#                     with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key) as reg_key:
#                         for i in range(winreg.QueryInfoKey(reg_key)[0]):
#                             subkey_name = winreg.EnumKey(reg_key, i)
#                             with winreg.OpenKey(reg_key, subkey_name) as subkey:
#                                 try:
#                                     display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
#                                     if "antivirus" in display_name.lower() or "security" in display_name.lower():
#                                         antivirus_names.add(display_name)
#                                 except Exception:
#                                     pass

#                 if antivirus_names:
#                     return "Antivirus software detected:\n" + "\n".join(antivirus_names)
#                 else:
#                     return "No antivirus software detected."
#             except Exception as e:
#                 return f"Error: {str(e)}"
#         else:
#             return "This script is for Windows only."
    

#     def list_unique_usb_device_names():
#         wmi = win32com.client.GetObject("winmgmts:")
#         devices = wmi.ExecQuery("SELECT * FROM Win32_PnPEntity WHERE PNPClass = 'USB'")

#         usb_device_names = set()
#         data = ""
#         for device in devices:
#             if (device.Name is not None):
#                 name = device.Name.strip()
#                 # Exclude entries that are not actual USB devices
#                 if (
#                     not name.startswith("Intel") and
#                     not name.startswith("USB Root Hub") and
#                     not name.startswith("Generic USB Hub") and
#                     not name.startswith("USB Composite Device") 
#                 ):
#                     usb_device_names.add(name)
#         if usb_device_names:
#             data += "Number of devices connected = " +str(len(usb_device_names)) +"\nConnected USB device names:\n"
#             for name in usb_device_names:
#                 data += name +"\n"
#         else:
#             data += "Number of devices connected = 0 \n"+"No USB devices found.\n"
#         data +="\n"
#         return data


#     def timestamps():
#         uptime_seconds = psutil.boot_time()
#         boot_time = datetime.fromtimestamp(uptime_seconds)
#         return (f"System boot time: {boot_time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    
#     def listofexe():
#         directory_path = os.path.join(os.path.expanduser('~'), 'Downloads')
#         exe_files = []
#         for root, dirs, files in os.walk(directory_path):
#             for file in files:
#                 if file.lower().endswith('.exe'):
#                     exe_files.append(os.path.join(root, file))
#         resultstr="\n".join(exe_files)
#         return ("\n List of .exe files : \n" + resultstr)
#     def list_connected_device():
#     # Define the PowerShell command as a string
#         powershell_command = '''
#         Get-PnpDevice | Where-Object {{ $_.Class -eq 'USB' -or $_.InstanceId -match '^USB' }}
#         '''

#     # Run the PowerShell command
#         process = subprocess.Popen(['powershell', '-command', powershell_command], stdout=subprocess.PIPE)
#         result = process.communicate()[0].decode('utf-8')
#         return ("\n Wired and Wireless Connections \n" + result)
    
#     sys_info=get_system_metadata()
#     antivirus_info = "Antivirus Information: " + detect_antivirus() + "\n\n"
#     external_devices = list_unique_usb_device_names()
#     timestamp=timestamps()
#     exefiles=listofexe()
#     connections=list_connected_device()

    
#     final = final + sys_info + antivirus_info + external_devices + timestamp + exefiles + connections
#     return final


# Network scan libraries

from ping3 import ping
from datetime import datetime,timedelta
import sqlite3
import shutil
import os
import socket
import subprocess
import uuid

# Hopping scan libraries
import networkx as nx
import numpy as np
import pandas as pd
import getpass
import requests
import datetime
import smtplib
import time


# Standalone check libraries
import platform
import winreg
import win32com.client
import psutil
from datetime import datetime

# Tkinter libraries
import tkinter as tk
from tkinter import scrolledtext

#libraries to save as a pdf
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

def network():
    final = "Network Scan \n\n"

    def network_details():
        data = "Network Details\n\n"
        IP = socket.gethostbyname(socket.gethostname())
        if IP=='127.0.0.1':
            data += "This PC is not connected to the internet\n"
            return
        else:
            data += 'This PC is connected to the internet through the IP address ' + str(IP) +'\n'

        data += "Type: "
        interfaces = psutil.net_if_stats()
        flag = 0
        for interface,stats in interfaces.items():
            if stats.isup:
                if 'Wi-Fi' in interface:
                    data += "Wireless " + interface +"\n"
                    flag = 1
                else:
                    data += 'Wired '+ interface +"\n"
                    flag = 2

        if(flag ==1):
            data += "SSID Name: "
            try:
                ssid = subprocess.check_output(["netsh", "wlan", "show", "interfaces"]).decode("utf-8").split("\n")
                for line in ssid:
                    if "SSID" in line:
                        data += line.split(":")[1].strip() 
            except Exception as e:
                return str(e)
        return data + "\n\n"

    final += network_details()
    final += "Network Troubleshooting\n\n"

    def check_connectivity(host, port):
        try:
            # Create a socket object and attempt to connect to the host and port
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5)  # Set a timeout for the connection attempt
                s.connect((host, port))
            return True
        except Exception as e:
            return False

    # Specify the host and port to check (e.g., a web server)
    host_to_check = "google.com"
    port_to_check = 80  # HTTP port

    # Perform the connectivity check
    if check_connectivity(host_to_check, port_to_check):
        final += f"Connection to Host: {host_to_check}, Port: {port_to_check} is successful.\n"
    else:
        fianl += f"Connection to Host: {host_to_check}, Port: {port_to_check} failed.\n"

    def icmp_ping(host):
        response_time = ping(host)
        if response_time is not None:
            return f"Response time: {response_time} ms\n\n"
        else:
            return "Host is unreachable or request timed out\n\n"

    # Specify the host to ping
    host_to_ping = "google.com"

    # Perform ICMP ping
    result = icmp_ping(host_to_ping)
    final += result

    def browser_hist():
        user = os.getlogin()

        history_file = r'C:\Users\\'+user+r'\AppData\Local\Microsoft\Edge\User Data\Default\History'
        copied_history_file = 'copied_web_data.sqlite'
        shutil.copyfile(history_file, copied_history_file)

        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)

        conn = sqlite3.connect(copied_history_file)
        cursor = conn.cursor()

        start_timestamp = int((start_date - datetime(1601, 1, 1)).total_seconds() * 1000000)
        end_timestamp = int((end_date - datetime(1601, 1, 1)).total_seconds() * 1000000)

        # Query the database for URLs accessed in the last 7 days
        cursor.execute("SELECT url, last_visit_time FROM urls WHERE last_visit_time >= ? AND last_visit_time <= ?", (start_timestamp, end_timestamp))
        history_data = cursor.fetchall()
        data = ""

        for row in history_data:
            url = row[0]
            timestamp = row[1] / 1000000  # Convert microseconds to seconds
            visit_time = datetime(1601, 1, 1) + timedelta(seconds=timestamp)

            data += "Website: "+url+"\n"
            data += "Date and Time of Access: "+str(visit_time)+"\n"
        
        conn.close()
        return data

    def list_files_downloaded():
        user = os.getlogin()
        base_directory = r'C:\Users\\'+ user+'\Downloads'  
        cutoff_date = datetime.now() - timedelta(days=90)
        downloaded_files = []
        data = ""
        for root, _, files in os.walk(base_directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_timestamp = datetime.fromtimestamp(os.path.getmtime(file_path))
                if file_timestamp >= cutoff_date:
                    downloaded_files.append((file_path, file_timestamp))
                    data += "File Name: " + file_path + " Timestamp: " + str(file_timestamp) + "\n"
        return data


    browser_history = browser_hist()
    list_of_files = list_files_downloaded()

    final +="Browser History\n\n" + browser_history    
    final +=  "\n\nDownloaded Files History\n\n" + list_of_files
    
    return  final

def network_hopping():
    final="Network Hopping Details \n\n"
            


    def network_hopping_analysis(network, nodes):
    
    # This function performs network hopping analysis on a given network and a list of nodes.

    # Args:
    #     network: A networkx graph object.
    #     nodes: A list of nodes to be analyzed.

    # Returns:
    #     A string representation of the network hopping statistics for each node.
    

        # Create the network if not provided
        if network is None:
            network = nx.Graph()

        # Create nodes and edges if not provided
        if len(network.nodes) == 0 or len(network.edges) == 0:
            network.add_nodes_from([1, 2, 3, 4, 5])
            network.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)])

        # Create a pandas DataFrame to store the results.
        results = pd.DataFrame(columns=['node', 'avg_hop_distance', 'max_hop_distance', 'std_hop_distance'])

        # Calculate the network hopping statistics for each node.
        for node in nodes:
            hop_distances = []
            for other_node in nodes:
                if other_node != node:
                    hop_distance = nx.shortest_path_length(network, node, other_node)
                    hop_distances.append(hop_distance)

            # Calculate the average, maximum, and standard deviation of the hop distances.
            avg_hop_distance = np.mean(hop_distances)
            max_hop_distance = np.max(hop_distances)
            std_hop_distance = np.std(hop_distances)

            # Add the results to the DataFrame.
            results.loc[node] = [node, avg_hop_distance, max_hop_distance, std_hop_distance]

        # Convert the DataFrame to a string representation.
        results_string = results.to_string(index=False)

        return results_string

    nodes = [1, 2, 3, 4, 5]
    final = "\n\n NETWORK HOPPING \n\nNetwork Hopping Analysis\n\n " + network_hopping_analysis(None, nodes)

    def get_system_info():
        def get_full_name(username):
            # Implement the logic to retrieve the full name based on the username
            name_mapping = {
                "user1": "John Doe",
                "user2": "Jane Smith",
                # Add more username-full name mappings as needed
            }
            return name_mapping.get(username, "Unknown")

        def get_ip_address():
            ip_address = socket.gethostbyname(socket.gethostname())
            return ip_address

        def get_user_context():
            # Get the currently logged-in username
            username = getpass.getuser()

            # Get the user's home directory
            home_directory = os.path.expanduser("~")

            # Get the user's full name (if available)
            full_name = get_full_name(username)

            user_context = {
                "Username": username,
                "Full Name": full_name,
                "Home Directory": home_directory
            }

            return user_context

        def get_device_context():
          # Get the hostname of the device
            hostname = platform.node()

            # Get the operating system information
            os_info = platform.platform()

            # Get the device's IP address (if available)
            ip_address = get_ip_address()

            device_context = {
                "Hostname": hostname,
                "Operating System": os_info,
                "IP Address": ip_address
            }

            return device_context

        user_context = get_user_context()
        device_context = get_device_context()

        context_string = "User Context:\n"
        for key, value in user_context.items():
            context_string += f"{key}: {value}\n"

        context_string += "\nDevice Context:\n"
        for key, value in device_context.items():
            context_string += f"{key}: {value}\n"

        return context_string

    final += "\n\nSystem Information\n\n" + get_system_info()

    def detect_malicious_ip(event_ip):
        # Define a list of known malicious IP addresses (simplified for demonstration)
        malicious_ips = [
            "192.168.1.100",
            "10.0.0.2",
            "malicious.example.com",
        ]

     # Fetch threat intelligence feeds (simplified for demonstration)
        def fetch_threat_intelligence_feeds():
            feed_url = "https://example.com/threat-intelligence-feed.json"
        
            try:
                response = requests.get(feed_url)
                if response.status_code == 200:
                    return response.json()
            except Exception as e:
                print(f"Error fetching threat intelligence feed: {e}")
        
            return []

        # Check if an IP address is in the list of known malicious IPs
        def is_ip_malicious(ip_address):
            return ip_address in malicious_ips

        # Check if an IP address is in the threat intelligence feed
        def is_ip_in_threat_feed(ip_address, threat_feed):
            return ip_address in threat_feed

        # Check the detection result for the given IP address
        def get_detection_result(event_ip):
            threat_feed = fetch_threat_intelligence_feeds()
            result_string = ""

            # Check if the IP is in the list of known malicious IPs
            if is_ip_malicious(event_ip):
                result_string += f"Malicious IP detected: {event_ip}\n"

            # Check if the IP is in the threat intelligence feed
            if is_ip_in_threat_feed(event_ip, threat_feed):
                result_string += f"IP in the threat intelligence feed: {event_ip}\n"

            return result_string

        return get_detection_result(event_ip)

    event_ip = "192.168.1.100"
    final += "\n\nDetection of Malicious IP Address\n\n" + detect_malicious_ip(event_ip)

    def correlate_log_events(log_data, correlation_rules):
        # Function to correlate log events
        def correlate_events(log_data, correlation_rules):
            correlated_events = []

            for log_entry in log_data:
                for rule_name, rule in correlation_rules.items():
                    if all(log_entry.get(key) == value for key, value in rule.items()):
                        correlated_events.append({"timestamp": log_entry["timestamp"], "rule_name": rule_name})

            return correlated_events

        # Function to get correlated events as a string
        def get_correlated_events_string(correlated_events):
            result_string = ""

            if correlated_events:
                result_string += "Correlated Events:\n"
                for event in correlated_events:
                    result_string += f"Rule: {event['rule_name']} - Timestamp: {event['timestamp']}\n"

            return result_string

        correlated_events = correlate_events(log_data, correlation_rules)
        correlated_events_string = get_correlated_events_string(correlated_events)

        return correlated_events_string

    # Example usage:

    # Simulated log data (replace with real log sources)
    log_data = [
        {"timestamp": "2023-09-01T12:34:56", "event_type": "Login", "user": "user1"},
        {"timestamp": "2023-09-01T13:45:00", "event_type": "FileAccess", "user": "user2"},
        {"timestamp": "2023-09-01T14:20:30", "event_type": "Login", "user": "user1"},
        {"timestamp": "2023-09-01T15:30:15", "event_type": "FileAccess", "user": "user3"},
    ]

    # Define correlation rules (replace with actual rules)
    correlation_rules = {
        "rule1": {"event_type": "Login", "user": "user1"},
        "rule2": {"event_type": "FileAccess", "user": "user2"},
    }

    final +=  "\n\nAnomalies Details\n\n" + correlate_log_events(log_data, correlation_rules)


    def get_boot_time_and_elapsed_time():
        try:
            # Get the system's boot time in seconds since epoch
            boot_time_seconds = psutil.boot_time()

            # Convert the boot time to a human-readable format
            boot_time = datetime.fromtimestamp(boot_time_seconds)

            current_time = datetime.now()

            # Calculate the time elapsed since boot-up
            elapsed_time = current_time - boot_time

            boot_time_str = f"System Boot-up Time: {boot_time}"
            elapsed_time_str = f"Elapsed Time Since Boot-up: {elapsed_time}"

            return f"{boot_time_str}\n{elapsed_time_str}"

        except Exception as e:  
            return f"Error: {e}"

    

    final += "\n\nBOOTUP ANALYSIS\n\n" + get_boot_time_and_elapsed_time()




    def send_network_hopping_alert():
        try:
            # Email configuration
            sender_email = "your_email@example.com"
            receiver_email = "recipient_email@example.com"
            smtp_server = "smtp.example.com"
            smtp_port = 587
            smtp_username = "your_username"
            smtp_password = "your_password"

            # Create the email message
            subject = "Network Hopping Alert"
            body = "Network hopping detected!"
            email_message = f"Subject: {subject}\n\n{body}"

            # Send the email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.sendmail(sender_email, receiver_email, email_message)

            return "Email alert sent successfully"

        except Exception as e:
            return f"Failed to send email alert: {e}"


    final += "\n\nAlert Mechanism\n\n " + send_network_hopping_alert()

    def check_for_network_hopping():
        def get_current_ip():
            return requests.get('https://api.ipify.org').text

        previous_location = None

        while True:
            current_ip = get_current_ip()
            response = requests.get(f'https://ipinfo.io/{current_ip}/json')

            if response.status_code == 200:
                location_info = response.json()
                location = location_info.get('city')  # You can change this to 'country', 'region', etc. as needed

            if location and location != previous_location:
                network_hopping_message = f"Network hopping detected: {previous_location} -> {location}"
                previous_location = location
                return network_hopping_message

            time.sleep(60)

    final += "\n\nGeoIP And GeoLocation \n\n" + check_for_network_hopping()
    

    def check_for_network_hopping():
        previous_ip = None

        while True:
            current_ip = requests.get('https://api.ipify.org').text

            if current_ip != previous_ip:
                network_hopping_message = f"Network hopping detected: {previous_ip} -> {current_ip}"
                return network_hopping_message
            previous_ip = current_ip
            time.sleep(60)



    final += "\n\n BASIC DETECTION \n\n " + check_for_network_hopping()
    

    return final

def stand_alone():
    final = "Stand Alone Scan \n\n"
    
    def get_system_metadata():
        system_info = {
        "OS Name": platform.system(),
        "OS Release": platform.release(),
        "OS Version": platform.version(),
        "Architecture": platform.architecture(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        }

        info_str = "\n".join([f"{key}: {value}" for key, value in system_info.items()])
        return ("System Information:\n" + info_str + "\n\n")
    
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
    

    def list_unique_usb_device_names():
        wmi = win32com.client.GetObject("winmgmts:")
        devices = wmi.ExecQuery("SELECT * FROM Win32_PnPEntity WHERE PNPClass = 'USB'")

        usb_device_names = set()
        data = ""
        for device in devices:
            if (device.Name is not None):
                name = device.Name.strip()
                # Exclude entries that are not actual USB devices
                if (
                    not name.startswith("Intel") and
                    not name.startswith("USB Root Hub") and
                    not name.startswith("Generic USB Hub") and
                    not name.startswith("USB Composite Device") 
                ):
                    usb_device_names.add(name)
        if usb_device_names:
            data += "Number of devices connected = " +str(len(usb_device_names)) +"\nConnected USB device names:\n"
            for name in usb_device_names:
                data += name +"\n"
        else:
            data += "Number of devices connected = 0 \n"+"No USB devices found.\n"
        data +="\n"
        return data


    def timestamps():
        uptime_seconds = psutil.boot_time()
        boot_time = datetime.fromtimestamp(uptime_seconds)
        return (f"System boot time: {boot_time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    


    def list_unique_usb_device_names():
        wmi = win32com.client.GetObject("winmgmts:")
        devices = wmi.ExecQuery("SELECT * FROM Win32_PnPEntity WHERE PNPClass = 'USB'")

        usb_device_names = set()
        data = ""
        for device in devices:
            if (device.Name is not None):
                name = device.Name.strip()
                # Exclude entries that are not actual USB devices
                if (
                    not name.startswith("Intel") and
                    not name.startswith("USB Root Hub") and
                    not name.startswith("Generic USB Hub") and
                    not name.startswith("USB Composite Device") 
                ):
                    usb_device_names.add(name)
        if usb_device_names:
            data += "Number of devices connected = " +str(len(usb_device_names)) +"\nConnected USB device names:\n"
            for name in usb_device_names:
                data += name +"\n"
        else:
            data += "Number of devices connected = 0 \n"+"No USB devices found.\n"
        data +="\n"
        return data


    def timestamps():
        uptime_seconds = psutil.boot_time()
        boot_time = datetime.fromtimestamp(uptime_seconds)
        return (f"System boot time: {boot_time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    
    def listofexe():
        directory_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        exe_files = []
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.lower().endswith('.exe'):
                    exe_files.append(os.path.join(root, file))
        resultstr="\n".join(exe_files)
        return ("\n List of .exe files : \n" + resultstr)
    def list_connected_device():
    # Define the PowerShell command as a string
        powershell_command = '''
        Get-PnpDevice | Where-Object {{ $_.Class -eq 'USB' -or $_.InstanceId -match '^USB' }}
        '''

    # Run the PowerShell command
        process = subprocess.Popen(['powershell', '-command', powershell_command], stdout=subprocess.PIPE)
        result = process.communicate()[0].decode('utf-8')
        return ("\n Wired and Wireless Connections \n" + result)
    
    def get_installed_updates():
     # PowerShell script to get installed updates
        powershell_script = '''
        $installedUpdates = Get-HotFix
        $installedUpdates | Format-Table -AutoSize
        '''

        try:
            # Run PowerShell script and capture the output
            result = subprocess.run(['powershell', '-Command', powershell_script], capture_output=True, text=True, check=True)
        
            # Return the output as a string
            return result.stdout

        except subprocess.CalledProcessError as e:
            return "Error: " + e.stderr

    sys_info=get_system_metadata()
    antivirus_info = "Antivirus Information: " + detect_antivirus() + "\n\n"
    external_devices = list_unique_usb_device_names()
    timestamp=timestamps()
    exefiles=listofexe()
    connections=list_connected_device()
    patchupdates=("\n Patch Updates \n" + get_installed_updates())
    
    final = final + sys_info + antivirus_info + external_devices + timestamp + exefiles + connections + patchupdates
    return final



def fullpc():
    final = "Full-PC Scan\n\n"
    final+="Device ID:\n"
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    final+="Device MAC:"
    final+=":".join([mac[e:e+2] for e in range(0, 12, 2)])
    IP = socket.gethostbyname(socket.gethostname())
    if IP=='127.0.0.1':
        final += "\nThis PC is not connected to the internet\n"
    else:
        final += '\nInternet IP address ' + str(IP) +'\n'


    full = "\n"+stand_alone()
    full += network()
    full += network_hopping()
    final += full
    
    return final

# Create the main window
window = tk.Tk()
window.title("Forensic Tool")

# Create a label for the title
title_label = tk.Label(window, text="\tWelcome to Forensic Tool\t", font=("Times New Roman", 20))
title_label.pack(pady=20)

# Function to save a string to a PDF file
def save(output_filename, input_string):
    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    styles = getSampleStyleSheet()

    # Create a list of flowables (elements) for the PDF
    formatted_text = input_string.replace('\n', '<br/>')
    formatted_paragraph = Paragraph(formatted_text, styles["Normal"])

    # Create a list of flowables (elements) for the PDF
    flowables = [formatted_paragraph]
    # Build the PDF document
    doc.build(flowables)

def standalone_scan():
    win = tk.Tk()
    win.geometry("700x500")
    win.title("StandAlone Scan")

    info = stand_alone()
    text = scrolledtext.ScrolledText(win, wrap=tk.WORD, width=80, height=25)
    text.pack(padx=20, pady=20)
    text.insert(tk.INSERT, info)
    
    start_index = info.find("Standalone Scan")
    end_index = start_index + len("Standalone Scan  ")
    text.tag_add("underline", f"1.{start_index}", f"1.{end_index}")
    text.tag_configure("underline", underline=True)
    text.tag_add("font_change", f"1.{start_index}", f"1.{end_index}")
    text.tag_configure("font_change", font= ("Times New Roman", 16))
    
    text.config(state="disabled")

    user = os.getlogin()
    base_directory = r'C:\Users\\'+ user+'\Downloads'  
    savebutton = tk.Button(win, text="Save", font=("Times New Roman",14),command = save(os.path.join(base_directory,"Standalone Scan.pdf"),info))
    savebutton.place(x=250,y=450)
    quit_button = tk.Button(win, text="Quit", font=("Times New Roman",14),command = win.destroy)
    quit_button.place(x=330,y=450)
    win.mainloop()
    

def network_scan():

    win = tk.Tk()
    win.geometry("800x600")
    win.title("Network Scan")

    info = network() 
    text = scrolledtext.ScrolledText(win, wrap=tk.WORD, width=100, height=32)
    text.pack(padx=20, pady=20)

    text.insert(tk.INSERT, info)
    
    start_index = info.find("Network Scan")
    end_index = start_index + len("Network Scan")
    text.tag_add("underline", f"1.{start_index}", f"1.{end_index}")
    text.tag_configure("underline", underline=True)
    text.tag_add("font_change", f"1.{start_index}", f"1.{end_index}")
    text.tag_configure("font_change", font= ("Times New Roman", 16))

    text.config(state="disabled")

    user = os.getlogin()
    base_directory = r'C:\Users\\'+ user+'\Downloads'  
    saveb = tk.Button(win, text="Save", font=("Times New Roman",14),command = save(os.path.join(base_directory,"Network Scan.pdf"),info)).place(x=280,y=550)
    quitb = tk.Button(win, text="Quit", font=("Times New Roman",14),command = win.destroy).place(x=360,y=550)
    win.mainloop()

def hopping():
    win=tk.Tk()
    win.geometry("700x600")
    win.title("Hopping Details")
    info=network_hopping()
    text = scrolledtext.ScrolledText(win, wrap=tk.WORD, width=100, height=32)
    text.pack(padx=20, pady=20)

    text.insert(tk.INSERT, info)
    start_index = info.find("Network Hopping Details")
    end_index = start_index + len("Network Hopping Details ")
    text.tag_add("underline", f"1.{start_index}", f"1.{end_index}")
    text.tag_configure("underline", underline=True)
    text.tag_add("font_change", f"1.{start_index}", f"1.{end_index}")
    text.tag_configure("font_change", font= ("Times New Roman", 16))

    text.config(state="disabled")
    user = os.getlogin()
    base_directory = r'C:\Users\\'+ user+'\Downloads'  
    saveb = tk.Button(win, text="Save", font=("Times New Roman",14),command = save(os.path.join(base_directory,"Network Hopping Details.pdf"),info)).place(x=280,y=550)
    quitb = tk.Button(win, text="Quit", font=("Times New Roman",14),command = win.destroy).place(x=360,y=550)
    win.mainloop()
    


def fullpc_scan():
    win = tk.Tk()
    win.geometry("700x500")
    win.title("Full-PC Scan")

    info = fullpc()
    text = scrolledtext.ScrolledText(win, wrap=tk.WORD, width=80, height=25)
    text.pack(padx=20, pady=20)

    text.insert(tk.INSERT, info)
    
    start_index = info.find("Full-PC Scan")
    end_index = start_index + len("Full-PC Scan")
    text.tag_add("underline", f"1.{start_index}", f"1.{end_index}")
    text.tag_configure("underline", underline=True)
    text.tag_add("font_change", f"1.{start_index}", f"1.{end_index}")
    text.tag_configure("font_change", font= ("Times New Roman", 16))

    text.config(state="disabled")

    user = os.getlogin()
    base_directory = r'C:\Users\\'+ user+'\Downloads'  
    saveb = tk.Button(win, text="Save", font=("Times New Roman",14),command = save(os.path.join(base_directory,"Full-PC Scan.pdf"),info)).place(x=250,y=450)
    quitb = tk.Button(win, text="Quit", font=("Times New Roman",14),command = win.destroy).place(x=330,y=450)
    win.mainloop()
    

# Create buttons with styling and functionality
standalone_button = tk.Button(window, text="Stand Alone check", font=("Times New Roman",14),command = standalone_scan)
network_button = tk.Button(window, text="Network Check", font=("Times New Roman",14),command = network_scan)
network_hop_button = tk.Button(window,text="Network Hopping", font=("TImes New Roman",14),command= hopping)
fullpc_button = tk.Button(window, text="Full PC Check", font=("Times New Roman",14),command = fullpc_scan)
quit_button = tk.Button(window, text="Quit", font=("Times New Roman",14), command=window.destroy)

# Pack buttons with spacing
standalone_button.pack(pady=10)
network_button.pack(pady=10)
network_hop_button.pack(pady=10)
fullpc_button.pack(pady=10)
quit_button.pack(pady=20)

# Start the main event loop
window.mainloop()




def fullpc():
    final = "Full-PC Scan\n\n"
    full=stand_alone()
    full+=network()
    final += full

    
    return final

# Create the main window
window = tk.Tk()
window.title("Forensic Tool")

# Create a label for the title
title_label = tk.Label(window, text="\tWelcome to Forensic Tool\t", font=("Times New Roman", 20))
title_label.pack(pady=20)

# Function to save a string to a PDF file
def save(output_filename, input_string):
    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    styles = getSampleStyleSheet()

    # Create a list of flowables (elements) for the PDF
    formatted_text = input_string.replace('\n', '<br/>')
    formatted_paragraph = Paragraph(formatted_text, styles["Normal"])

    # Create a list of flowables (elements) for the PDF
    flowables = [formatted_paragraph]
    # Build the PDF document
    doc.build(flowables)

def standalone_scan():
    win = tk.Tk()
    win.geometry("1200x800")
    win.title("StandAlone Scan")

    info = stand_alone()
    text = scrolledtext.ScrolledText(win, wrap=tk.WORD, width=500, height=40)
    text.pack(padx=20, pady=20)
    text.insert(tk.INSERT, info)
    
    start_index = info.find("Standalone Scan")
    end_index = start_index + len("Standalone Scan  ")
    text.tag_add("underline", f"1.{start_index}", f"1.{end_index}")
    text.tag_configure("underline", underline=True)
    text.tag_add("font_change", f"1.{start_index}", f"1.{end_index}")
    text.tag_configure("font_change", font= ("Times New Roman", 16))
    
    text.config(state="disabled")

    user = os.getlogin()
    base_directory = r'C:\Users\\'+ user+'\Downloads'  
    savebutton = tk.Button(win, text="Save", font=("Times New Roman",14),command = save(os.path.join(base_directory,"Standalone Scan.pdf"),info))
    savebutton.place(x=300,y=700)
    quit_button = tk.Button(win, text="Quit", font=("Times New Roman",14),command = win.destroy)
    quit_button.place(x=380,y=700)
    win.mainloop()
    

def network_scan():

    win = tk.Tk()
    win.geometry("800x600")
    win.title("Network Scan")

    info = network()
    text = scrolledtext.ScrolledText(win, wrap=tk.WORD, width=100, height=32)
    text.pack(padx=20, pady=20)

    text.insert(tk.INSERT, info)
    
    start_index = info.find("Network Scan")
    end_index = start_index + len("Network Scan")
    text.tag_add("underline", f"1.{start_index}", f"1.{end_index}")
    text.tag_configure("underline", underline=True)
    text.tag_add("font_change", f"1.{start_index}", f"1.{end_index}")
    text.tag_configure("font_change", font= ("Times New Roman", 16))

    text.config(state="disabled")

    user = os.getlogin()
    base_directory = r'C:\Users\\'+ user+'\Downloads'  
    saveb = tk.Button(win, text="Save", font=("Times New Roman",14),command = save(os.path.join(base_directory,"Network Scan.pdf"),info)).place(x=280,y=550)
    quitb = tk.Button(win, text="Quit", font=("Times New Roman",14),command = win.destroy).place(x=360,y=550)
    win.mainloop()

def fullpc_scan():
    win = tk.Tk()
    win.geometry("700x500")
    win.title("Full-PC Scan")

    info = fullpc()
    text = scrolledtext.ScrolledText(win, wrap=tk.WORD, width=80, height=25)
    text.pack(padx=20, pady=20)

    text.insert(tk.INSERT, info)
    
    start_index = info.find("Full-PC Scan")
    end_index = start_index + len("Full-PC Scan")
    text.tag_add("underline", f"1.{start_index}", f"1.{end_index}")
    text.tag_configure("underline", underline=True)
    text.tag_add("font_change", f"1.{start_index}", f"1.{end_index}")
    text.tag_configure("font_change", font= ("Times New Roman", 16))

    text.config(state="disabled")

    user = os.getlogin()
    base_directory = r'C:\Users\\'+ user+'\Downloads'  
    saveb = tk.Button(win, text="Save", font=("Times New Roman",14),command = save(os.path.join(base_directory,"Full-PC Scan.pdf"),info)).place(x=250,y=450)
    quitb = tk.Button(win, text="Quit", font=("Times New Roman",14),command = win.destroy).place(x=330,y=450)
    win.mainloop()
    

# Create buttons with styling and functionality
standalone_button = tk.Button(window, text="Stand Alone check", font=("Times New Roman",14),command = standalone_scan)
network_button = tk.Button(window, text="Network Check", font=("Times New Roman",14),command = network_scan)
fullpc_button = tk.Button(window, text="Full PC Check", font=("Times New Roman",14),command = fullpc_scan)
quit_button = tk.Button(window, text="Quit", font=("Times New Roman",14), command=window.destroy)

# Pack buttons with spacing
standalone_button.pack(pady=10)
network_button.pack(pady=10)
fullpc_button.pack(pady=10)
quit_button.pack(pady=20)

# Start the main event loop
window.mainloop()
