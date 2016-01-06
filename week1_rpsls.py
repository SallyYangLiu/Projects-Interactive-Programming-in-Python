# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    if name == "rock": 
        number = 0
    elif name == "Spock": 
        number = 1
    elif name == "paper": 
        number = 2
    elif name == "lizard": 
        number = 3
    elif name == "scissors": 
        number = 4
    else:
        number = "Wrong name"      
    return number


def number_to_name(number):
    if number == 0: 
        name = "rock"
    elif number == 1 : 
        name = "Spock"
    elif number ==2 : 
        name = "paper"
    elif number == 3: 
        name = "lizard"
    elif number == 4: 
        name = "scissors"
    else:
        name = "Wrong name"      
    return name
    
import random



def rpsls(player_choice): 
    if (player_choice == "rock" or 
        player_choice == "Spock" or 
        player_choice == "paper" or 
        player_choice == "lizard" or 
        player_choice == "scissors"):
        print "The player chooses", player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,4)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses", comp_choice
    difference(player_number, comp_number)

def difference(player_number, comp_number):
    if ((player_number - comp_number) % 5 == 1 or 
       (player_number - comp_number) % 5 == 2 or 
       (player_number - comp_number) % 5 == -3 or 
       (player_number - comp_number) % 5 == -4):
          print "Player wins!"
    elif ((player_number - comp_number) % 5 == -1 or 
          (player_number - comp_number) % 5 == -2 or 
          (player_number - comp_number) % 5  == 3 or 
          (player_number - comp_number) % 5 == 4):
          print "Computer wins!"
    else:
          print "Player and computer tie!"
    print" "
    
    
#def name_to_number(player_choice):
#    if player_choice == "rock":
#        player_number = 0
#    elif player_choice == "Spock":
#        player_number = 1    
#    elif player_choice == "paper":
#        player_number = 2
#    elif player_choice == "lizard":
#        player_number = 3
#    elif player_choice == "scissors":
#        player_number = 4
#    else:
#        player_number = "player picks a worng gesture"       
#        return player_number
    
    


    


#def number_to_name(comp_number):
#    if comp_number == 0: 
#        comp_choice = "rock"
#    elif comp_number == 1 : 
#        comp_choice = "Spock"
#    elif comp_number ==2 : 
#        comp_choice = "paper"
#    elif comp_number == 3: 
#        comp_choice = "lizard"
#    elif comp_number == 4: 
#        comp_choice = "scissors"
#    else:
#        comp_choice = "computer picks a worng gesture"
#        print "Computer chooses", comp_choice
#    return comp_choice



    
        
    # delete the following pass statement and fill in your code below
    pass
    
    # print a blank line to separate consecutive games

    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()
    
    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE

rpsls("rock")

rpsls("Spock")

rpsls("paper")

rpsls("lizard")

rpsls("scissors")
