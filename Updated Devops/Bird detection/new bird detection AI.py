import numpy as np
from picamera2 import Picamera2
import picamera.array
import tflite_runtime.interpreter as tflite
import time

# Load the TensorFlow Lite model.
model_path = 'keras.tflite'
interpreter = tflite.Interpreter(model_path)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Configure the Pi camera.
camera = Picamera2()
camera.resolution = (640, 480)

# Define a function to perform bird detection on a single image.
def detect_bird(image):
    # Preprocess the image.
    input_data = np.expand_dims(image, axis=0).astype(np.float32)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    # Extract the output probabilities and classes.
    output_data = interpreter.get_tensor(output_details[0]['index'])
    class_ids = np.argmax(output_data, axis=1)
    scores = output_data[0, class_ids]

    # Return the class ID and score of the most probable bird.
    if scores > 0.5:
        return class_ids[0], scores[0]
    else:
        return None

# Create an array to store the output image.
with picamera.array.PiRGBArray(picam2) as output:
#output = picamera.array.PiRGBArray(camera)

# Continuously capture images from the camera and perform bird detection.
    for frame in picam2.capture_continuous(output, format='rgb', use_video_port=True):
    # Extract the image data from the output array.
        image = output.array

        # Perform bird detection on the image.
        bird= detect_bird(image)

        # Print the result.
        if bird is not None:
            print('Detected bird with class ID %d and score %f' % (bird[0], bird[1]))

        # Clear the output array for the next image.
        output.truncate(0)
