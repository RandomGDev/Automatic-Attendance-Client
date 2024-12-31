import cv2
import os

global_dir = ""
global_cl = ""
global_sec = ""
global_name = ""
global_rollno = ""

def Info(cl, sec, name, rollno):
    # Getting inputs from user
    dir = "Enrolled Students"
    sec = str(sec).upper()
    name = str(name).title()

    # Making directories to store images
    if not os.path.exists(dir):
        os.makedirs(dir)
    if not os.path.exists(f"{dir}/{cl}"):
        os.makedirs(f"{dir}/{cl}")
    if not os.path.exists(f"{dir}/{cl}/{sec}"):
        os.makedirs(f"{dir}/{cl}/{sec}")

    global global_dir, global_cl, global_sec, global_name, global_rollno
    global_dir = dir
    global_cl = cl
    global_sec = sec
    global_name = name
    global_rollno = rollno

def EnrollStudents(cap, cl, sec, name, rollno):
    sec = str(sec).upper()
    name = str(name).title()
    maindir = f"{global_dir}/{cl}/{sec}"          
    ret, frame = cap.read()

    if ret:
        image_path = f"{maindir}/{name}_{rollno}.jpeg"
        cv2.imwrite(image_path, frame)

        # Convert the image to RGB format if necessary
        img = cv2.imread(image_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(image_path, img)

    cv2.destroyAllWindows()
