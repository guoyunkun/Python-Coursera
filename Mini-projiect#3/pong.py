# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = 300
ball_vel = 200

ball_pos_v = 0
ball_vel_v = 0

pad_v = 2

pad1_pos = PAD_WIDTH/2
pad1_vel = HEIGHT/2
pad2_pos = WIDTH - PAD_WIDTH/2
pad2_vel = HEIGHT/2


move_up1 = False
move_down1 = False
move_up2 = False
move_down2 = False



def timer_handler():
    global ball_pos,ball_vel,ball_pos_v,ball_vel_v
    ball_pos = ball_pos + ball_pos_v
    ball_vel = ball_vel + ball_vel_v 
    
    collide()
    global pad1_vel,pad2_vel,HALF_PAD_HEIGHT,HEIGHT
    global move_up1,move_up2,move_down1,move_down2
    if move_up1 == True and pad1_vel >= HALF_PAD_HEIGHT:
        pad1_vel -= pad_v
    if move_down1 == True and pad1_vel <= HEIGHT - HALF_PAD_HEIGHT:
        pad1_vel += pad_v
    if move_up2 == True and pad2_vel >= HALF_PAD_HEIGHT:
        pad2_vel -= pad_v
    if move_down2 == True and pad2_vel <= HEIGHT - HALF_PAD_HEIGHT:
        pad2_vel += pad_v
    

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos_v,ball_vel_v
    global ball_pos, ball_vel
    # these are vectors stored as lists
    if direction == False:
        ball_pos_v = float(random.randrange(120, 240))/100
    else:
        ball_pos_v = -float(random.randrange(120, 240))/100
    ball_vel_v = -float(random.randrange(60, 180))/100
    ball_pos = 300
    ball_vel = 200
   
def collide_by_pad1(ball_vel):
    global pad1_pos, HALF_PAD_HEIGHT,BALL_RADIUS
    if ball_vel < pad1_vel +  HALF_PAD_HEIGHT+BALL_RADIUS and ball_vel > pad1_vel -  HALF_PAD_HEIGHT - BALL_RADIUS:
        return True
    else:
        return False
    
    
def collide_by_pad2(ball_vel):
    global pad2_vel, HALF_PAD_HEIGHT,BALL_RADIUS,BALL_RADIUS
    if ball_vel < pad2_vel +  HALF_PAD_HEIGHT + BALL_RADIUS and ball_vel > pad2_vel -  HALF_PAD_HEIGHT - BALL_RADIUS:
        return True
    else:
        return False
    
   
def collide():
    global RIGHT,LEFT
    global ball_pos, ball_vel,ball_pos_v,ball_vel_v
    global flag_pos,flag_vel
    global score1,score2
    if ball_pos - BALL_RADIUS < PAD_WIDTH:
        if collide_by_pad1(ball_vel) == True:
            ball_pos_v = ball_pos_v * 1.1
            ball_vel_v = ball_vel_v * 1.1
            ball_pos_v = - ball_pos_v
        else:
            RIGHT = True
            LEFT = False
            score2 += 1
            new_game()
        
       
    
    if ball_pos + BALL_RADIUS > WIDTH - PAD_WIDTH:
       if collide_by_pad2(ball_vel):
            ball_pos_v = ball_pos_v * 1.1
            ball_vel_v = ball_vel_v * 1.1
            ball_pos_v = - ball_pos_v
       else:
            score1 += 1
            RIGHT = False
            LEFT = True
            new_game()
        
        
        
    if ball_vel + BALL_RADIUS > HEIGHT:
        ball_vel_v = - ball_vel_v
    if ball_vel - BALL_RADIUS < 0:
        ball_vel_v = - ball_vel_v
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(LEFT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global pad1_pos,pad1_vel,pad2_pos,pad2_vel
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT],1,"White")
        
    
    canvas.draw_circle([ball_pos,ball_vel],BALL_RADIUS,1,'White','White')
    # update paddle's vertical position, keep paddle on the screen
    point1 =[pad1_pos + HALF_PAD_WIDTH/2 , pad1_vel + PAD_HEIGHT/2]
    point2 =[pad1_pos + HALF_PAD_WIDTH/2 , pad1_vel - PAD_HEIGHT/2]
    point3 =[pad1_pos - HALF_PAD_WIDTH/2 , pad1_vel + PAD_HEIGHT/2]
    point4 =[pad1_pos - HALF_PAD_WIDTH/2 , pad1_vel - PAD_HEIGHT/2]
    point_set = [point1,point2,point3,point4]
    canvas.draw_polygon(point_set,4,'White','White')
    
    point1 =[pad2_pos + HALF_PAD_WIDTH/2 , pad2_vel + PAD_HEIGHT/2]
    point2 =[pad2_pos + HALF_PAD_WIDTH/2 , pad2_vel - PAD_HEIGHT/2]
    point3 =[pad2_pos - HALF_PAD_WIDTH/2 , pad2_vel + PAD_HEIGHT/2]
    point4 =[pad2_pos - HALF_PAD_WIDTH/2 , pad2_vel - PAD_HEIGHT/2]
    point_set = [point1,point2,point3,point4]
    canvas.draw_polygon(point_set,4,'White','White')
    
    canvas.draw_text(str(score1),(250,100),30,'White')
    canvas.draw_text(str(score2),(335,100),30,'White')
    
    
        
def keydown(key):
    global move_up1,move_up2,move_down1,move_down2
    
    if key == simplegui.KEY_MAP['W']:
        move_up1 = True
    if key == simplegui.KEY_MAP['S']:
        move_down1 = True
    if key == simplegui.KEY_MAP['up']:
        move_up2 = True
    if key == simplegui.KEY_MAP['down']:
        move_down2 = True
def keyup(key):
    global move_up1,move_up2,move_down1,move_down2
   
    if key == simplegui.KEY_MAP['W']:
        move_up1 = False
    if key == simplegui.KEY_MAP['S']:
        move_down1 = False
    if key == simplegui.KEY_MAP['up']:
        move_up2 = False
    if key == simplegui.KEY_MAP['down']:
        move_down2 = False

def restart_handle():
    global score1,score2,Left,RIGHT
    score1 = 0
    score2 = 0
    LEFT = False
    RIGHT = True
    new_game()
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart',restart_handle)
timer = simplegui.create_timer(10,timer_handler)
timer.start()

# start frame
new_game()
frame.start()
