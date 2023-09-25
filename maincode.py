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

from ping3 import ping
from datetime import datetime,timedelta
import sqlite3
import shutil
import os
import socket
import subprocess

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
from reportlab.lib.pagesizes import inch


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
        final += f"Connection to Host: {host_to_check}, Port: {port_to_check} failed.\n"

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
    
    sys_info=get_system_metadata()
    antivirus_info = "Antivirus Information: " + detect_antivirus() + "\n\n"
    external_devices = list_unique_usb_device_names()
    timestamp=timestamps()
    exefiles=listofexe()
    connections=list_connected_device()

    
    final = final + sys_info + antivirus_info + external_devices + timestamp + exefiles + connections
    return final




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
