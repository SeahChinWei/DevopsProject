import tflite_runtime.interpreter as tflite
import numpy as np
import cv2
from PIL import Image, ImageOps

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the TensorFlow Lite model
interpreter = tflite.Interpreter(model_path="keras.tflite")
interpreter.allocate_tensors()

# Get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Load the labels
class_names = open("labels.txt", "r").readlines()

# Create the array of the right shape to feed into the TensorFlow Lite model
data = np.ndarray(shape=input_details[0]['shape'], dtype=np.float32)

while True:
    # Replace this with the path to your image
    # image = Image.open("<IMAGE_PATH>").convert("RGB")
    cap = cv2.VideoCapture("usb://1-5")
    ret, frame = cap.read()
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Run the TensorFlow Lite model and get the predictions
    interpreter.set_tensor(input_details[0]['index'], data)
    interpreter.invoke()
    prediction = interpreter.get_tensor(output_details[0]['index'])

    # Find the class with the highest confidence score
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", confidence_score)

