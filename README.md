# Gesture-Controlled LED using MediaPipe and Arduino

This project demonstrates how to control an LED using hand gestures detected with MediaPipe and Arduino. By leveraging the power of computer vision through MediaPipe, we can detect specific hand gestures in real-time and use them to trigger actions on an Arduino board, such as turning an LED on or off.

## Requirements

- Python 3.x
- MediaPipe
- OpenCV
- PySerial
- Arduino IDE
- Arduino board (e.g., Arduino Uno)
- LED
- Resistor (appropriate value for your LED)
- Breadboard
- Jumper wires

## Setup

1. **Install Python dependencies:** First, make sure you have Python 3.x installed on your system. Then, install the required Python packages using pip:

   ```
   pip install mediapipe opencv-python pyserial
   ```

2. **Install Arduino IDE:** Download and install the Arduino IDE from the official [Arduino website](https://www.arduino.cc/en/software).

3. **Set up the Arduino:** Connect your Arduino board to your computer using a USB cable. Open the Arduino IDE, go to `File` > `Examples` > `Firmata` and upload the StandardFirmata sketch to your Arduino board.

4. **Connect the LED:** Connect the LED to your Arduino board as follows:
   
   - Connect the longer leg (anode) of the LED to digital pin 13 on the Arduino board.
   - Connect the shorter leg (cathode) of the LED to a resistor.
   - Connect the other end of the resistor to the ground (GND) pin on the Arduino board.

5. **Clone the repository:** Clone or download the repository containing the Python scripts for gesture detection and Arduino control.

## Usage

1. **Run the Python script:** Navigate to the directory containing the Python scripts and run the `gesture_detection.py` script:

   ```
   python gesture_detection.py
   ```

2. **Calibrate the gestures:** Follow the on-screen instructions to calibrate the hand gestures. This step helps in detecting gestures accurately.

3. **Interact with the LED:** Once the calibration is complete, perform the predefined hand gestures to control the LED. For example, make a fist to turn the LED on, and open your palm to turn it off.

## Troubleshooting

- **Serial port not found:** If the Python script cannot find the serial port connected to your Arduino board, make sure the Arduino IDE is closed, as it might be occupying the serial port.

- **Poor gesture recognition:** Ensure that the lighting conditions are adequate for accurate hand gesture detection. You may need to recalibrate the gestures if recognition is inconsistent.

## Credits

This project was inspired by [MediaPipe](https://mediapipe.dev/) and [Arduino](https://www.arduino.cc/), and it utilizes their respective libraries and tools.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
