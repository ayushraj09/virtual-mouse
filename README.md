# Virtual Mouse with OpenCV and MediaPipe

This project implements a **Virtual Mouse** using hand gesture recognition with OpenCV, MediaPipe, and Python. By tracking your hand through your webcam, you can move your mouse cursor and perform left/right clicks using finger gestures—no physical mouse required!

## Features

- **Hand tracking** using MediaPipe
- **Move mouse cursor** with your index finger
- **Left click** by pinching index and middle fingers together
- **Right click** by spreading index and middle fingers apart
- **Smooth cursor movement** for a natural feel
- **Works on Windows, macOS, and Linux** (with webcam and permissions)

## Requirements

- Python 3.7+
- Webcam
- [OpenCV](https://pypi.org/project/opencv-python/)
- [MediaPipe](https://pypi.org/project/mediapipe/)
- [numpy](https://pypi.org/project/numpy/)
- [pynput](https://pypi.org/project/pynput/)
- [screeninfo](https://pypi.org/project/screeninfo/)

Install all dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

1. **Clone this repository:**
    ```bash
    git clone https://github.com/yourusername/virtual-mouse-opencv.git
    cd virtual-mouse-opencv
    ```

2. **Run the virtual mouse:**
    ```bash
    python hand_tracking/virtual_mouse.py
    ```

3. **Allow accessibility permissions** if prompted (especially on macOS).

4. **Control your mouse:**
    - Move your index finger to move the cursor.
    - Pinch index and middle fingers to left-click.
    - Spread index and middle fingers wide to right-click.

## Notes

- Make sure your webcam is connected and accessible.
- On macOS, grant accessibility permissions to your terminal or IDE for mouse control.
- For best results, use in a well-lit environment.

---

**Enjoy controlling your computer