# implementation of card game - Memory

import simplegui
import random

CARDS = range(8) * 2
flip_status = [False] * 16
draw_sequence = []
turns = 0
current_draw = []
    

# helper function to initialize globals
def new_game():
    global exposed, flip_status, turns, draw_sequence, current_draw
    random.shuffle(CARDS)
    flip_status = [False] * 16
    turns = 0
    draw_sequence = []
    current_draw = []
       
# define event handlers
def mouseclick(pos):
    global exposed, flip_status, turns, card_index, draw_sequence, current_draw
    for card_index in range(len(CARDS)):
        if (len(current_draw) <= 1 and 
            card_index == pos[0] // 50 and 
            flip_status[card_index] == False):
            current_draw.append(CARDS[card_index])
            flip_status[card_index] = True
            draw_sequence.append(card_index)
        elif (len(current_draw) == 2 and 
            card_index == pos[0] // 50 and 
            flip_status[card_index] == False):
            current_draw.append(CARDS[card_index])
            flip_status[card_index] = True
            draw_sequence.append(card_index)
            if current_draw[0] == current_draw[1]:
                flip_status[draw_sequence[0]] = True
                flip_status[draw_sequence[1]] = True
            elif current_draw[0] != current_draw[1]:
                flip_status[draw_sequence[0]] = False
                flip_status[draw_sequence[1]] = False
                turns += 1
            current_draw.pop(0)
            current_draw.pop(0)  
            draw_sequence.pop(0)
            draw_sequence.pop(0)
          
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for card_index in range(len(CARDS)):
        card_pos = [50 * card_index + 20, 50]
        canvas.draw_text(str(CARDS[card_index]), card_pos, 24, "White") 
        canvas.draw_polygon([(50 * card_index, 0), (50 * card_index + 50, 0), (50 * card_index + 50, 100), (50 * card_index, 100)], 1, "White", "Green")   
        if flip_status[card_index] == True:
            canvas.draw_polygon([(50 * card_index, 0), (50 * card_index + 50, 0), (50 * card_index + 50, 100), (50 * card_index, 100)], 1,"White", "Black")
            canvas.draw_text(str(CARDS[card_index]), [50 * card_index + 20, 50], 24, "White")  
    turns_label.set_text("Turns = " + str(turns))
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
turns_label = frame.add_label("Turns = 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric