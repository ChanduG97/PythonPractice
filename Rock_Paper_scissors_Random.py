import random
def Get_Choices():
    player_choice = input("Select your choice ( Rock , Paper , Scissors ): ")
    options = ["Rock","Paper","Scissor"]
    if player_choice.lower() =="rock" or player_choice.lower()=="paper" or player_choice.lower()=="scissors":
        computer_choice = random.choices(options)
        choices = {"Player":player_choice,"Computer":computer_choice}
        return choices
    else:
        print("Enter Correct Choice.")
choices = Get_Choices()
print(choices)