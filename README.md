# Fruit Detection with YOLOv5 using Webcam

## Overview
This project is designed to detect fruits using the YOLOv5 object detection model and a webcam. By utilizing Python and the YOLOv5 model, the program captures video frames from the webcam, processes them, and identifies fruits in real-time. This project can be extended to detect various types of fruits and can be used as a base for applications in agriculture, inventory systems, or interactive educational tools.

### Key Features:
- Real-time fruit detection using YOLOv5
- Webcam integration for live video feed
- Simple and easy-to-understand code

## Installation

### Prerequisites:
- Python 3.7 or higher
- A working webcam (USB or built-in)
- An internet connection for downloading necessary dependencies

### Steps to Install:

1. **Clone the repository:**
   First, clone the repository to your local machine.
   ```bash
   git clone https://github.com/your-username/fruit-detection-yolov5.git
   cd fruit-detection-yolov5
Install required libraries: Use pip to install the necessary libraries. You can create a virtual environment for this project to manage dependencies.

bash
Copy
Edit
pip install -r requirements.txt
Alternatively, if you're not using a requirements.txt file, manually install the following libraries:

bash
Copy
Edit
pip install torch torchvision
pip install opencv-python
pip install yolov5
Run the program: Once all dependencies are installed, you can run the fruit detection program with the following command:

bash
Copy
Edit
python detect_fruits.py
The webcam should open, and the program will begin detecting fruits in real-time.

Exit the program: To stop the program, press q while the video feed window is open.

Example Output
Once the program is running, it will show the webcam feed with bounding boxes around the detected fruits.

License
This project is open-source and available under the MIT License.

Acknowledgements
YOLOv5 model by Ultralytics
OpenCV for webcam handling
