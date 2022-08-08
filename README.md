# Computer Vision Project
This projects aim was to create a simple rock, paper, scissors game using computer vision tools

> ![image](https://user-images.githubusercontent.com/105006854/173890732-8cbc4833-7b3d-4da7-b10f-5b65948f6aa6.png)

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
## MIlestone 3
- This milestone consisted of creating a rock paper scissors game which took the user input via keyboard, compared to the computer random choice and returned a winner
- The first step was to create a rock, paper, scissors class define attributes and create get_computer_choice() and get_user_choice() functions.
- Some important considerations when creating the get_user_choice() function were to ensure the user could only enter one of the relevant options and to keep requesting an input until this was satified.
- The attributes of the class, get_user_choice() and get_computer_choice() functions can be seen below:

>>> python
``` python
    def __init__(self, option_list) -> None:
        self.computer_choice = random.choice(option_list)
    
        pass

    def get_computer_choice(self):
        return(self.computer_choice)
        
    def get_user_choice(self):

        user_choice = input("Choose Rock, Paper or Scissors: ")

        while True:
            if user_choice in option_list:
                rps.get_winner(self, user_choice)
                break
            else:
                print("Please enter either Rock, Paper or Scissors")
            break  
        pass
```
- The next step in this milestone was to create a function that could figure out who won the game by comparing the user input and the computer random selection. This was done using conditional statements and creating a new method for the rps class, get_winner(). 
- Some key considerations for this project was trying to make efficient code by finding the best way to determine the result. This was achieved by first determining whether the choices were the same which would result in a draw, then the checking reduced to a binary win or lose.
- The get_winner() can be seen below:

>>> python
``` python
    def get_winner(self, user_choice):
        if self.computer_choice == user_choice:
            print("It's a draw")
        else:
            if self.computer_choice == "Rock":
                if user_choice == "Paper":
                    print("You won")
                    print("The computer chose", self.computer_choice)
                else:
                    print("You lost")
                    print("The computer chose", self.computer_choice)
                
            elif self.computer_choice == "Paper":
                if user_choice == "Scissors":
                    print("You won")
                    print("The computer chose", self.computer_choice)
                else: 
                    print("You lost")
                    print("The computer chose", self.computer_choice)

            elif self.computer_choice == "Scissors":
                if user_choice == "Rock":
                    print("You won")
                    print("The computer chose", self.computer_choice)
                else:
                    print("You lost")
                    print("The computer chose", self.computer_choice)
```
- The final part of this milestone tied this all together in a final play() function, outside the class
- This function would initialise the class and call the relevant functions (get_user_choice() & get_computer_choice())
- A final if statement was then formed using __name__ == '__main__' to ensure the game would be automatically ran when the program was run
- These pieces of code can be seen below:
>>> python
``` python
def play(option_list):
    game = rps(option_list)

    game.get_computer_choice()
    game.get_user_choice()
    pass

if __name__ == '__main__':
    option_list = ["Rock", "Paper", "Scissors"]
    play(option_list)
```
## Milestone 4
- The final milestone required me to put this all together. So in essence replace the computer input via keys and change that to an input via the computer vision model I had built and trained in Milestones 1 & 2
- The first step was to create a new method for the class, get_prediction(). This method would switch the webcam on when the user was asked for an input and depending on what was displayed, the model would return the most probable outcome shown. This would then be translated into a user input which would then be feed into the get_winner function created in milestone 3. 
- This also saw the use of the "Nothing" class on the model as when this was the most probable outcome the computer would continue to ask for an input. 
- This was then taken further by creating a countdown so the user was able to show the camera their input at a specific time allowing them to get ready

>>> python
``` python
def get_prediction(self):
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        flag = False
        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('video', frame)
            # Press q to close the window 
            
            if cv2.waitKey(1) & 0xFF == ord('g'):
                flag = True
                start = time.time()
            if flag == True:
                end = 5 - (time.time() - start)
                current_score = "You: " + str(self.user_score), "Computer: " + str(self.computer_score)
                cv2.putText(frame, str(int(end)), (350,238), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 3, cv2.LINE_4)
                cv2.putText(frame, str(current_score), (31,445), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3, cv2.LINE_4)
                cv2.imshow('frame', frame)
                if end <= 0:
                    print(prediction)
                    if prediction[0][0] > 0.5:
                        user_choice ="Rock"
                    elif prediction[0][1] > 0.5:
                        user_choice ="Paper"
                    elif prediction[0][2] > 0.5:
                        user_choice = "Scissors"
                    elif prediction[0][3] > 0.5:
                        flag = False
                        continue
                    break
            else:
                continue 
        cap.release()
        cv2.destroyAllWindows()
        rps.get_winner(self, user_choice)
```
- In order to properly simultate the Rock, Paper, Scissors game a scoreboard was also created and the code looped so the first to 3 victories would win the game.

>>> python
``` python
class rps:
    def __init__(self, option_list) -> None:
        self.computer_choice = random.choice(option_list)
        self.computer_score = 0
        self.user_score = 0
        pass
```
>>> pyton
``` python
def play(option_list):
    game = rps(option_list)

    while True:
        game.get_prediction()
        if game.computer_score == 3:
            print("The computer has won the game! Better luck next time.")
            break
        elif game.user_score == 3:
            print("You have won the game! Congratulations")
            break
        else:
            continue
    
if __name__ == '__main__':
    option_list = ["Rock", "Paper", "Scissors"]
    play(option_list)
 ```
 Finally to extend the project further I also put the countdown and scoreboard on the camera screen in order to keep track of the score and countdown easier.
 
 ## Conclusion
 
