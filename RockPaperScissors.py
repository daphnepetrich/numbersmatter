print("Daphne Petrich. Blog soon to come.")
loose=("The computer wins")
win=("You Win")
lives=5
score=0
drew=0
computer_lives=7
password_list=[]
while True:
    print ("To begin, fill in the below information.")
    username = input ("Please enter your username:   ")
    password = input ("Please enter your password:   ")
    searchfile = open("accounts.txt", "r")
    for i in searchfile:
        password_list.append(i.strip())
        if username and password in password_list:
            print("Access Granted")
            print("-----------------------------------------------------------------------------")
            print("                  ___________       _______    _________   __     __         ")
            print("                 |           |     |       |  |         | |  |  /  /         ")
            print("                 |         __|     |       |  |   ______| |  |/  /           ")
            print("                 |    |\    \      |       |  |  |        |     |            ")
            print("                 |    |  \    \    |       |  |  |_____   |   \ \            ")
            print("                 |    |    \    \  |       |  |        |  |  | \  \          ")
            print("                 |____|      \__|  |______ |  |________|  |__|  \ __\        ")
            print("Live Rules")
            print("You start with", lives, "lives")
            print("If you win you get an extra life.")
            print("If you loose you loose a life.")
            print("If you draw, the lives stay the same")
            print("**************************************")
            print("MAKE SURE YOU DON'T USE CAPITALS")
            print("**************************************")
            print("To see a list of rules type rules")
            print("**************************************")
            print("At any point type 'exit' to leave the game")
            print("At any point type 'display score' to see your score")
            print("At any point type 'display lives' score to see how many lives you have left")
            print("At any point type 'display drew' to see how many times you drew with the computer.")
            print("**************************************")
            print("Can you beat the computer?")
            print("GOOD LUCK!")
            while True:
                rps=input("rock, paper, scissors?   ")
                import random
                computer = ("rock", "paper", "scissors")
                computer = random.choice(computer)
                #rock if statements
                if rps =="rock" and computer == "paper":
                    print ("The computer chose", computer)
                    print(loose)
                    lives -=1
                if rps == "rock" and computer == "scissors":
                    print ("The computer chose", computer)
                    print(win)
                    computer_lives -=1
                    score +=1
                if rps == "rock" and computer == "rock":
                    print ("The computer chose", computer)
                    print("You drew")
                    drew +=1
                #paper if statements
                if rps == "paper" and computer == "rock":
                    print ("The computer chose", computer)
                    print(win)
                    computer_lives -=1
                    score+=1
                if rps == "paper" and computer == "scissors":
                    print ("The computer chose", computer)
                    print(loose)
                    lives -=1
                if rps == "paper" and computer == "paper":
                    print ("The computer chose", computer)
                    print("You drew")
                    drew +=1
                #scissor if statements
                if rps =="scissors" and computer == "paper":
                    print ("The computer chose", computer)
                    print(win)
                    computer_lives -=1
                    score +=1
                if rps == "scissors" and computer == "rock":
                    print ("The computer chose", computer)
                    print(loose)
                    lives -=1
                if rps == "scissors" and computer == "scissors":
                    print ("The computer chose", computer)
                    print("You drew")
                    drew +=1
                #system
                if rps == "rules":
                    print("*******************************************************")
                    print("RULES")
                    print("Rock beats Scissors but looses against Paper")
                    print("Paper beats Rock but looses against Scissors")
                    print("Scissors beats Paper but looses against against Rock")
                    print("*******************************************************")
                if rps == "display lives":
                    print(lives)
                if rps == "display score":
                    print(score)
                if rps == "display drew":
                    print(drew)
                #lives
                if lives ==0 or rps == "test":
                    print("Thanks for playing.")
                    print("You have run out of lives.....")
                    print("You beat the computer", score, "times")
                    print("You drew", drew, "times")
                    stop = input ("Press enter to exit")
                    import time
                    time.sleep(900)
                if computer_lives==0:
                    print("Thanks for playing.")
                    print("The computer lost all its lives. You win.")
                    print("You beat the computer", score, "times")
                    print("You drew", drew, "times")
                    stop = input ("Press enter to exit")
                    import time
                    time.sleep(900)
                #exit
                if rps == "exit":
                    break
            else:
                print("Your username or password is incorrect.")
                break
                        
                        
                
                
                        

