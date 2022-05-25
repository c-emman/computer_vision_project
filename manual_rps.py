import random

class rps:
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
        pass

def play(option_list):
    game = rps(option_list)

    game.get_computer_choice()
    game.get_user_choice()
    pass

if __name__ == '__main__':
    option_list = ["Rock", "Paper", "Scissors"]
    play(option_list)