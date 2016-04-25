# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number 
    secret_number = random.randrange(0,100,1)


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    # remove this when you add your code    
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    pass
    
def input_guess(guess):
    # main game logic goes here	
    guess_number = int(guess)
    print "Gaess was",guess_number
    if guess_number<0 or guess_number>99:
        print "Out of guesses"
    elif guess_number < secret_number:
        print "Lower"
    elif guess_number > secret_number:
        print "Higher"
    elif guess_number == secret_number:
        print "Correct"
    
    
    # remove this when you add your code
    pass

    
# create frame
frame = simplegui.create_frame("Gaess the Number!",300,200)
inp = frame.add_input("input guess:",input_guess,100)

# register event handlers for control elements and start frame


# call new_game 
new_game()
print secret_number

# always remember to check your completed program against the grading rubric