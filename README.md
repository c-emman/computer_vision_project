# Computer Vision Project
This rojects aim was to create a simple rock, paper, scissors game using computer vision tools

## Milestone 1
- This first step in this milestone was to create a model for my rock, paper, scissors game. The tool utilised for this was Teachable-Machine. I used this website to create a model with 4 classes being, "Rock", "Paper", "Scissors" and "Nothing". This would be used later on in my code to integrate the game with my webcam.
- A key consideration here was to ensure the model was taught using multiple different views to ensure the model could detect various different look of me showing either rock, paper or scissors. Another consideration was to not use too many datapoints as this could effectively 'break' the model and cause it to give false results
- Once this was done the model was then downloaded locally for testing

## Milestone 2
- Initially this milestone began with creating a new virtual environment for my project with the necessary requirements of tensorflow and open-cv. 
- Next the model could then be tested locally using the following code and given insufficient results I would return to milestone 1 and repeat:

>>> python
``` python
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if prediction[0][0] > 0.7:
        print("Rock")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    elif prediction[0][1] > 0.7:
        print("Paper")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    elif prediction[0][2] > 0.7:
        print("Scissors")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    elif prediction[0][3] > 0.7:
        print("Nothing")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
```
