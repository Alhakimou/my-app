# 📷 Real-Time Object Detection and Tracking with YOLOv8

This Python application uses your laptop's camera to perform live object detection and tracking. It leverages the **YOLOv8** deep learning model alongside **OpenCV** to track multiple objects in real time and assign persistent tracking IDs to them.

## 📋 Features
* **Live Camera Feed:** Captures video directly from your built-in webcam.
* **Real-Time Tracking:** Uses YOLOv8 tracking (`persist=True`) to maintain unique object IDs across frames.
* **Auto-Annotation:** Automatically draws bounding boxes and class labels around detected objects.

---

## 🛠️ Requirements & Installation

This project requires Python 3.8 or higher. You must install the `opencv-python` and `ultralytics` libraries.

### 1. Install Required Libraries
Open your terminal or command prompt and run the following command to install the dependencies:
```bash
pip install opencv-python ultralytics
```

*Note: The script uses the `yolov8n.pt` (YOLOv8 Nano) model weights. These weights will automatically download to your project folder the very first time you run the script.*

---

## 🚀 How to Run the Code

1. Open your terminal or command prompt.
2. Navigate to the folder where `detecte_multiobjects.py` is saved.
3. Execute the script using Python:
   ```bash
   python detecte_multiobjects.py
   ```

---

## 💡 How to Use the Application

1. Once the script starts, your laptop webcam will turn on, and a new window titled **"Suivi d'objets - Caméra Laptop"** will open.
2. Point your camera at objects (like people, phones, cups, or laptops) to see the tracking boxes.
3. To safely close the application and turn off the webcam, press the **`q`** key on your keyboard while focusing on the video window.
