# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = 4
HALF_PAD_HEIGHT = 40
LEFT = False
RIGHT = True
paddle1_pos = [4, 200]
paddle2_pos = [596, 200]
paddle1_vel = [0, 2]
paddle2_vel = [0, 2]

# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [300, 200]
ball_vel = [0, 0]
time = 0

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [300, 200]
    ball_vel[0] = random.randrange(120, 240)/100
    ball_vel[1] = random.randrange(60, 180)/100   
    if direction == RIGHT: 
        RIGHT == True
        ball_vel[0] = ball_vel[0] 
        ball_vel[1] = -ball_vel[1] 
    elif direction == LEFT:
        RIGHT == False      
        ball_vel[0] = -ball_vel[0] 
        ball_vel[1] = -ball_vel[1]
    return ball_vel[0], ball_vel[1]
            

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, ball_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = [4, 200]
    paddle2_pos = [596, 200]
    paddle1_vel = [0, 0]
    paddle2_vel = [0, 0]
    score1 = 0
    score2 = 0
    spawn_ball(LEFT)

def restart():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, ball_vel  # these are numbers
    global score1, score2
    new_game()
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel 
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1] += paddle1_vel[1]
    paddle2_pos[1] += paddle2_vel[1]
    if paddle1_pos[1] == HALF_PAD_HEIGHT or paddle1_pos[1] == HEIGHT - HALF_PAD_HEIGHT:
        paddle1_vel[1] = - paddle1_vel[1]
    elif paddle2_pos[1] == HALF_PAD_HEIGHT or paddle2_pos[1] == HEIGHT - HALF_PAD_HEIGHT:
        paddle2_vel[1] = - paddle2_vel[1]         
    
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos[1] - 40], [8, paddle1_pos[1] - 40], [8, paddle1_pos[1] + 40], [0, paddle1_pos[1] + 40]], 1, "White", "White")
    canvas.draw_polygon([[600, paddle2_pos[1] - 40], [600 - 8, paddle2_pos[1] - 40], [600 - 8, paddle2_pos[1] + 40], [600, paddle2_pos[1] + 40]], 1, "White", "White")                    
    
    # determine whether paddle and ball collide
     
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS and paddle1_pos[1] - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle1_pos[1] + HALF_PAD_HEIGHT:
        ball_vel[0] = - 1.1 * ball_vel[0]
        ball_vel[1] = 1.1 * ball_vel[1]
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS and paddle2_pos[1] - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle2_pos[1] + HALF_PAD_HEIGHT:
        ball_vel[0] = - 1.1 * ball_vel[0]
        ball_vel[1] = 1.1 * ball_vel[1]
    elif ball_pos[0] <= PAD_WIDTH + BALL_RADIUS and ball_pos[1] < paddle1_pos[1] - HALF_PAD_HEIGHT:
        spawn_ball(RIGHT)
        score2 += 1
    elif ball_pos[0] <= PAD_WIDTH + BALL_RADIUS and ball_pos[1] > paddle1_pos[1] + HALF_PAD_HEIGHT:
        spawn_ball(RIGHT)
        score2 += 1 
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS and ball_pos[1] < paddle2_pos[1] - HALF_PAD_HEIGHT:
        spawn_ball(LEFT)
        score1 += 1
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS and ball_pos[1] > paddle2_pos[1] + HALF_PAD_HEIGHT:
        spawn_ball(LEFT) 
        score1 += 1  
        
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[0] = ball_vel[0]
        ball_vel[1] = -ball_vel[1]
        
    # draw scores    
    canvas.draw_text(str(score1), [200, 60], 32, "White")
    canvas.draw_text(str(score2), [380, 60], 32, "White")
                                          
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = 2
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = -2       
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 2
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = -2
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = [0, 0]
    paddle2_vel = [0, 0]


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("New Game", new_game, 100)
frame.add_button("Restart", restart, 100)


# start frame
new_game()
frame.start()