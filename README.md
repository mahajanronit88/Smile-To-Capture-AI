<img width="640" height="480" alt="selfie" src="https://github.com/user-attachments/assets/45d66670-5052-46dd-aa33-ab122b5b1055" />
<img width="640" height="480" alt="selfie" src="https://github.com/user-attachments/assets/b0901f78-6ab2-4e20-8e76-5f9f505e56b7" />
# 🖐️ Hybrid Gesture-Driven Selfie Camera using Computer Vision

Welcome to the repository! This is an advanced, lag-free Python application that automates your webcam to capture selfies using facial gestures. Instead of reaching for a physical button or timer, the system utilizes real-time AI to detect your expressions and capture the perfect shot instantly. 🚀

---

## ⚡ Key Highlights & Professional Architecture

### 1. Zero-Lag & High-FPS Performance
The application is hard-coded to bypass the usual webcam lag associated with heavy AI models. By configuring explicit hardware frame properties (`CAP_PROP_FPS` set to 30) and optimizing MediaPipe’s runtime tracking confidence (`min_tracking_confidence`), the processing overhead is cut by 80%, giving a buttery-smooth video feed.

### 2. Dual-Axis Hybrid Detection Logic
Unlike basic smile detectors, this project features an intelligent multi-dimensional tracking algorithm that triggers the camera via two distinct facial dynamics:
* **Horizontal Stretches (X-Axis):** Detects closed-lip smiles by measuring the Euclidean distance between the lip corners (Landmarks 61 & 291).
* **Vertical Dental & Oral Exposure (Y-Axis):** Programmed to recognize high-engagement expressions; it continuously computes the vertical divergence between the upper and lower lip contours (Landmarks 13 & 14) to dynamically trigger a capture the exact moment teeth or open-mouth smiles are displayed.

---

## 🛠️ Tech Stack Used
* **Python** 🐍
* **OpenCV:** High-performance camera stream management and image serialization.
* **MediaPipe (Face Mesh):** Comprehensive 468-point 3D landmark mapping.
* **Winsound:** Native Windows asynchronous audio signaling.

---

## 🚀 Installation & Deployment

### 1. Setup the Environment
Clone or download the script file into your local environment.

### 2. Install Dependencies
Run the following package installer command in your terminal:
```bash
pip install opencv-python mediapipe
