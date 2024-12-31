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

## Acknowledgements
- [face_recognition](https://github.com/ageitgey/face_recognition) library
- [dlib](http://dlib.net/) for ML models
- [Keyboard](https://pypi.org/project/keyboard/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [csv](https://docs.python.org/3/library/csv.html)
- [pynum](https://numpy.org/): I had most problem with this
