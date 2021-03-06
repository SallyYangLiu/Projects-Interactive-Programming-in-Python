# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math


    
# initialize global variables used in your code here

num_range = 100 

#----------------------------
secret_number = -1
n=-1
Guess =-1
typeWeArePlaying =-1

#----------------------------

# helper function to start and restart the game

def new_game():    
    global secret_number 
    global num_range
    num_range = 100
    secret_number= random.randrange(0, num_range) 
    return secret_number

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global n
    global typeWeArePlaying
    typeWeArePlaying=100
    n = 7
    print "New game. Range is from 0 to 100"
    print "Remaining guesses is", n 
    print ""
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game 
    global n
    global typeWeArePlaying
    typeWeArePlaying=1000
    n = 10
    global num_range
    num_range = 1000
    secret_number= random.randrange(0, num_range)    
    print "New game. Range is from 0 to 1000"
    print "Remaining guesses is", n 
    print ""
    new_game()
    
def get_input(guess):
    # main game logic goes here	
    global Guess
    global secret_number
    global n
    global typeWeArePlaying
    Guess = int(guess)
    print "Guess was", Guess 
    n = n - 1
    print "The remaining guesses is", n
    if n &lt;= 0:
        print "Out of guesses"
        print " "
        if typeWeArePlaying == 100:
            range100()
        elif typeWeArePlaying == 1000:
            range1000()
    else:
        if Guess  &lt; secret_number:
            print "Higher"
        elif Guess  &gt; secret_number:
            print "Lower"
        elif Guess  == secret_number:   
            print "Correct"
            print " "
            if typeWeArePlaying == 100:
                range100()
            elif typeWeArePlaying == 1000:
                range1000()  
        print " "



    
# create frame
f = simplegui.create_frame("Guess the number", 300, 300)

                                        
                                        
# register event handlers for control elements and start frame
f.add_button("Range is [0,100)", range100, 100)
f.add_button("Range is [0,1000)", range1000, 100)
f.add_input("Input the guess", get_input, 100)

f.start()

# call new_game 
new_game()
