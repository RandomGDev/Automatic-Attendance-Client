from tkinter import *
from tkinter import ttk
import keyboard
import cv2
from PIL import Image, ImageTk
import enroll as en
import threading


cap = cv2.VideoCapture(0)
# Open Camera
def start_video_stream(label):
    def update_frame():
        ret, frame = cap.read()
        if ret:
            # Converting frame to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            label.imgtk = imgtk
            label.configure(image = imgtk)
        if cap.isOpened():
            label.after(10, update_frame)
    update_frame()

# Window GUI and Size
window = Tk()
window.geometry("1000x720")
window.title("Automatic Attendance Client")
window.config(background="#212528")

# Navbar
navbar = Frame(window, bg="#3c4444", height=40)
navbar.pack(fill="x")
title = Label(navbar, text="Automatic Attendance Client \n Teacher's Client", font=("Bebas Neue", 30), fg="#ffffff", bg="#3c4444",pady=10)
title.pack(pady=10)

# Showing camera feed
video_frame = Frame(window, bg="#212528", width=500 ,height=400)
video_frame.pack(pady=20)
video_label = Label(video_frame, bg="#212528", width=500, height=400)
video_label.pack()

# Parameters section
params_frame = Frame(window, bg="#212528")
params_frame.pack(pady=30)

# Ussing Tkinter to make UI and customize it
params = [("Class", ""), ("Section", ""), ("Full Name", ""), ("Roll No", "")]
entries = {}

for param, placeholder in params:
    frame = Frame(params_frame, bg="#212528")
    frame.pack(fill="x", pady=5)

    label = Label(frame, text=param, font=("Arial", 20), fg="white", bg="#212528", width=20, anchor="w")
    label.pack(side="left", padx=5)

    entry = Entry(frame, font=("Arial", 17), fg="black", bg="#FFFFFF", width=40)
    entry.insert(0, placeholder)
    entry.pack(side="right", padx=5)
    entries[param] = entry

# Enroll
enroll_button = Button(window, text="Enroll", font=("Arial", 20), bg="#2d77da", fg="white", command=lambda: enroll(entries),width=20)
enroll_button.pack(pady= 2)

def enroll(entries):  
    if keyboard.is_pressed("enter") :
        details = {key: entry.get() for key, entry in entries.items()}    
        cla = details["Class"]
        sec = details["Section"]
        rollno = details["Roll No"]
        name = details["Full Name"]
        en.Info(cla,sec,name,rollno)
        en.EnrollStudents(cap,cla,sec,name,rollno)
        print("Enrolled Details:", details)  
    else:
        details = {key: entry.get() for key, entry in entries.items()}    
        cla = details["Class"]
        sec = details["Section"]
        rollno = details["Roll No"]
        name = details["Full Name"]
        en.Info(cla,sec,name,rollno)
        en.EnrollStudents(cap,cla,sec,name,rollno)
        print("Enrolled Details:", details)  

    

start_video_stream(video_label)

window.mainloop()
