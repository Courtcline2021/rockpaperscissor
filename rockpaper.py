import random 

# think about line these up for each possiblty for Rock Paper and Scissor there will be nine possible combos 
# Paper > Paper - Rock = w > Paper - Scissor = L > Paper - Paper = T 
# Rock > Rock - Paper = L > Rock - Scissor = W > Rock - Rock = T 
# Scissor > Scissor - Paper = W > Scissor - Rock = L > Scissor - Scissor = T 
# What would be the cleanest way to do this OOP or if statement 

while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissor \n ")

    choice = int(input("Enter you choice : "))

    while choice > 3 or choice < 1 : 
        choice = int(input("Enter a valid choice: "))
# sets choice name by user 
    if choice == 1: 
        choice_name = 'Rock'
    elif choice == 2 :
        choice_name = 'Paper'
    else :
        choice_name = 'Scissor'    
# displays what the user selected 
    print('User choice is \n ', choice_name) 
    print('Computers Turn')   

    comp_choice = random.randint(1,3)
# ensures that the comp choice is random 
    while comp_choice == choice:
        comp_choice = random.randint(1,3)
# sets the name of comp choice 
    if comp_choice == 1:
        comp_name = 'Rock'
    elif comp_choice == 2 :
        comp_name = 'Paper'   
    else:
        comp_name = 'Scissor'  

    print('Computer choice is \n ', comp_name)  
    print(choice_name, 'VS', comp_name)   

# checks is there is a draw btw user and computer         
    if choice == comp_choice:
        print("Its a draw!", end="")
        result = 'Draw'
# wins for Paper
    if (choice == 1 and comp_choice == 2 ):
        print('Paper wins => ', end="")    
        result = 'Paper'
    elif (choice == 2 and comp_choice == 1 ):
        print("Paper wins =>  ", end="")    
        result = 'Paper'
# wins for Rock
    if (choice == 1 and comp_choice == 3):
        print('Rock  wins => ', end="") 
        result = 'Rock'
    elif(choice == 3 and comp_choice == 1 ):  
        print("Rock wins => ", end="")  
        result = 'Rock'

    if (choice == 2 and comp_choice == 3):
        print('Scissor wins => ',end="")
        result = 'Scissor'
    elif (choice == 3 and comp_choice == 2):
        print('Scissor wins => ', end="") 
        result = 'Scissor'
# Prints out who the winner is 
    if result == 'Draw':
        print('<== Its a Draw ==> ')      
    if result == choice_name :
        print('<== User Wins ! ==>')  
    else :
        print('<== Computer Wins! ==>')  

    print('Do you want a rematch (Y/N)')   
    ans = input().lower()     
    if ans == 'n':
        break

