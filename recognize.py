import cv2
import face_recognition
import csv
import numpy as np
import os
from datetime import datetime, time
import time
import keyboard
import csv
import imageEncoder

colour = ()
colour_red = (0,0,255)
colour_green = (0,255,0)

attendence_file = open(f"{datetime.today().date()}.csv","w")
attendence = csv.writer(attendence_file)
attendence.writerow(("Roll no",'Time',"Name","Class","Section"))

def load_face_data_from_csv(file_path):
    
    known_face_encodings = []
    known_face_names = []    
    
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:            
            full_path = row[0]
            encoding = np.array([float(x) for x in row[1].split(',')])
            
            #Seperating name from the complete path
            formatted_name = format_name(full_path)
            
            known_face_names.append(formatted_name)
            known_face_encodings.append(encoding)
    
    return known_face_encodings, known_face_names

def format_name(file_path):

    # Splitting the paths for better readability
    path_parts = file_path.split(os.sep)
    
    # Extracting Details
    if len(path_parts) >= 4:
        class_name = path_parts[-3]
        section = path_parts[-2]  
        full_name, roll_number = path_parts[-1].rsplit('_', 1) 
        roll_number = roll_number.split('.')[0]
        
        #Marking the name is attendence
        attendence.writerow((roll_number,time.strftime("%H:%M:%S", time.localtime()),full_name,class_name,section))

        # Formatting as "Name, Class, Section : Roll Number"
        return f"{full_name} ,{class_name}  {section} : {roll_number}"
    return "Unknown"

# Loading the face data from the CSV file referenced earlier
face_data = 'face_data.csv'
known_face_encodings, known_face_names = load_face_data_from_csv(face_data)

# Start webcam
video_capture = cv2.VideoCapture(0)

#tries to check if the face is matching
try:
    while True:
        # Capture each frame from the webcam
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to capture frame from camera. Exiting...")
            break

        # Resizing the frame for reduced size faster process
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        rgb_small_frame = cv2.cvtColor(rgb_small_frame , cv2.COLOR_BGR2RGB)  # Convert to RGB

        # Detecting faces and encoding them for the face_recognition library to understand
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            # Comparing detected faces with known faces in csv
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances) if len(face_distances) > 0 else None

            if best_match_index is not None and matches[best_match_index]:
                name = known_face_names[best_match_index]
                colour = colour_green
            else:
                name = "Unknown"
                colour= colour_red

            # Drawing rectangle around the face and displayin the relevant information
            top, right, bottom, left = [v * 4 for v in face_location]
            cv2.rectangle(frame, (left, top), (right, bottom), (colour), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        # Displaying the resulting frame
        cv2.imshow("Live Feed", frame)

        # Break loop when Esc is pressed
        if cv2.waitKey(1) & keyboard.is_pressed("escape"):
            break

except KeyboardInterrupt:
    print("\n Exiting...") #Exits the program if key pressed by user

finally:
    # Closes the webcan and window after use
    video_capture.release()
    cv2.destroyAllWindows()
    attendence_file.close()


