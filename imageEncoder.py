import os
import face_recognition
import csv

def encode_faces_in_directory(directory):
    face_encodings = []
    face_names = []

    # Walk through the directory and all its subdirectories
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            # Process only image files (you can add more extensions if needed)
            if file_name.lower().endswith(('jpg', 'jpeg', 'png')):
                file_path = os.path.join(root, file_name)
                try:
                    # Load the image and encode faces
                    image = face_recognition.load_image_file(file_path)
                    encodings = face_recognition.face_encodings(image)
                    
                    # Append encodings and names to lists
                    for encoding in encodings:
                        face_encodings.append(encoding)
                        face_names.append(file_path)  # Use the full file path as the name
                except Exception as e:
                    print(f"Could not process {file_name}: {e}")

    return face_encodings, face_names

def save_data_csv(face_encodings, face_names, file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(['Name', 'Face Encoding'])
        
        for name, encoding in zip(face_names, face_encodings):
            encoding_str = ','.join(map(str, encoding))
            writer.writerow([name, encoding_str])

image_folder = "Enrolled Students"  # Replace with your folder path

face_encodings, face_names = encode_faces_in_directory(image_folder)

save_data_csv(face_encodings, face_names, 'face_data.csv')

print("Face data saved to 'face_data.csv'.")
