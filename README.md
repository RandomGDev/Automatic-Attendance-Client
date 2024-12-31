# Automatic Attendance Client

This project helps making attendance easier as it has two clients one for teacher and other for user or device.


## Features
### Only One Image is enough per person

### Teacher's Client
- It can make the database for the images in `.jpg` format.
- It formats the folder according to class, section, roll no
  
### Machine's Client
- It can make use of the database to recognize the face.
- It can mark attendance as per roll no , class, section and name as in database

## Requirements
- Working Webcam or Device with camera

## Usage
1. Install the file from releases
2. Extract the files
3. Go to the Extracted folder and run Teacher's Client first to create database

## Output
The CSV file includes:
- **Time**: Time when the person first appeared.

## Contributing
Contributions and feedback are welcome. Submit issues or feature requests via GitHub.

## License
This is school project and is currently unlicensed.

## Libraries Used
- [face_recognition](https://github.com/ageitgey/face_recognition): Used for image recognition
- [open-cv](https://opencv.org/): Used for image management
- [dlib](http://dlib.net/): Used for ML models
- [Keyboard](https://pypi.org/project/keyboard/): Used to setup HotKeys
- [Tkinter](https://docs.python.org/3/library/tkinter.html): Used to setup GUI
- [csv](https://docs.python.org/3/library/csv.html): Used to make Final Files
- [pynum](https://numpy.org/): Used as substituent of Face_Recognition (I had most problem with this)
