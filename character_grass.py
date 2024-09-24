from pico2d import *
import math

open_canvas()

#fill here

grass=load_image('grass.png')
boy=load_image('character.png')

def run_top():
    print('TOP')
    pass

def run_right():
    print('RIGHT')
    pass

def run_bottom():
    print('BOTTOM')
    pass

def run_left():
    print('LEFT')
    pass

def run_rectangle():
    print('rectangle')
    run_top()
    run_right()
    run_bottom()
    run_left()
    
    pass

def run_circle():
    print('circle')

    r=300
    cx=800 //2
    cy=600 //2

    for d in range(0,360):
        x=r*math.cos(math.radians(d)) + cx
        y=r*math.sin(math.radians(d)) + cy
        
        clear_canvas_now()
        boy.draw_now(x,y)
        delay(0.01)
    pass


while(True): #사각형 운동과 원 운동
    #run_circle()
    run_rectangle()
    break
    
    

close_canvas()
