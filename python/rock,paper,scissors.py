import random
import time

time.sleep(1)
# print multiline instruction
# perform f string
print("Winning rules of the game ROCK PAPER SCISSORS are :\n"
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n"
      )
time.sleep(1)

while True:
    
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    
    # take the input from user
    choice = int(input("Select your number: "))

    # looping until user enter invalid input 
    while choice > 3 or choice < 1:
        choice = int(input("Enter a Valid number pls🙂"))
    
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = "Paper"
    elif choice == 3:
        choice_name = "Scissors"
    else:
        print("Really🙄\n \tI'm just gonna end it here.")
        break
    
    time.sleep(1)
    
    #print user choice
    print(f"User choice is {choice_name}\n ")
    print("Now it's comp's turn...\n")
    
    time.sleep(1)
    
    comp_choice = random.randint(1,3)
    
    while comp_choice == choice:
        comp_choice = random.randint(1,3)
        
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    elif comp_choice == 3:
        comp_choice_name = 'Scissor'
    else:
        quit()
    
    time.sleep(1)
        
    print(f"Computer's choice is {comp_choice_name}\n")
    print(f"{choice_name} VS {comp_choice_name}")
    
    if choice == comp_choice:
        print("DRAW!!",end='')
        result = 'DRAW'
    
    if (choice == 1 and comp_choice==2):
        print("paper wins =>",end='')
        result = "Paper"
    elif (choice==2 and comp_choice==1):
        print("paper wins =>0",end='')
        result = 'Paper'
        
        
    if choice == 1 and comp_choice == 3:
        print("Rock wins =>",end='')
        result = "Rock"
    elif choice == 3 and comp_choice == 1:
        print("Rock wins =>",end='')
        result = "Rock"

    if choice == 2 and comp_choice == 3:
        print("Scissors wins =>",end='')
        result = 'Scissors'
    elif choice == 3 and comp_choice == 2:
        print("Scissors wins =>",end='')
        result = "Scissors"
        
    if result == 'DRAW':
        print("<== It's a tie ==>")
    elif result == choice_name:
        print("<== User wins ==>")
    else:
        print(f"<== Computer wins ==>")
    print("Wanna play again... Y/N")
    
    ans = input().lower()
    
    if ans == 'y':
        print("Awesome")
        time.sleep(1)
        
    if ans == 'n':
        break

print("Byeeee🙂")