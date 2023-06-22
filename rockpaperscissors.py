import random
#assigning values to numbers in a dictionary
game_dictionary= {
    1:"rock",
    2:"paper",
    3:"scissors"    
}


#rps function
def rps():
    #getting the user's input
        gamer_input = input("Enter 1 for rock, 2 for paper, 3 for scissors:\n")

        #checking the correct input
        if gamer_input<str(1) or gamer_input>str(3):
            print("Incorrect entry")
        #printing user input
        else:
            print("you chose "+game_dictionary[int(gamer_input)])
            
            # comp input
            computerchoice = random.choice("123")
            computer = game_dictionary[int(computerchoice)]

            #printing comp choice
            print("the pc chose "+ computer)

            #declaring the winner, loser or tie
            if gamer_input=="1" and computerchoice=='3':
                print("You win")
            elif gamer_input=='2' and computerchoice=='1':
                print("You win")
            elif gamer_input=='3' and computerchoice=='2':
                print("You win")
            elif gamer_input==computerchoice:
                print("tie")
            else:
                print("Computer wins")
                
                
def continue_after_previous_trial():
    input2= input("\n\tTo continue press 'c'\n\tTo qiut press 'q'\n")
    second_try = True
    while second_try:
        if input2.lower()=='q':
            print("Bye")
            second_try=False
        elif input2.lower()=="c":
            rps()
            second_try=False
            continue_after_previous_trial()
        else:
            print("Wrong input")
            second_try=False
            
                    
input1= input("welcome to rock, paper, scissors game\n\tTo proceed press 'c'\n\tTo qiut press 'q'\n")


def game_loop():
    #setting active to be true
    active=True
    while active:
        
        if input1.lower()=="q":
            print("Bye")
            active=False
        elif input1.lower()=="c":
            rps()
            active=False
            continue_after_previous_trial()
        else:
            print("Wrong input.")
            active=False
            

game_loop()