from pico2d import *
import math

open_canvas()

#fill here

grass=load_image('grass.png')
boy=load_image('character.png')

def draw_boy(x,y):
    clear_canvas_now()
    boy.draw_now(x,y)
    delay(0.01)


def run_top():
    for x in range(0,750,10):
        draw_boy(x,550)
    pass

def run_right():
    for y in range(550,0,-10):
        draw_boy(750,y)
    pass

def run_bottom():
    for x in range(750,0,-10):
        draw_boy(x,50)
    pass

def run_left():
    for y in range(50,550,10):
        draw_boy(20,y)
    pass



def run_left_tri():
    for y in range(100, 500, 10):
        x = 100 + (y - 100) * (400 - 100) / (500 - 100)  # 기울기를 계산하여 x 좌표를 계산
        draw_boy(x, y)
        delay(0.01) 
    pass

def run_right_tri():
    for x in range(400, 700, +10):
        y = 100 + (x - 700) * (500 - 100) / (400 - 700)  # 기울기를 계산하여 y 좌표를 계산
        draw_boy(x, y)
        delay(0.01)
    pass

def run_bottom_tri():
    for x in range(700, 100, -10):
        draw_boy(x, 100)
        delay(0.01)
    pass


#사각형 모양 함수 정의
def run_rectangle():
    run_top()
    run_right()
    run_bottom()
    run_left()
    
    pass

#원 모양 함수 정의
def run_circle():

    r=300
    cx=800 //2
    cy=600 //2

    for d in range(0,360):
        x=r*math.cos(math.radians(d)) + cx
        y=r*math.sin(math.radians(d)) + cy

        draw_boy(x,y)
    pass

def run_triangle():
    run_left_tri()
    run_right_tri()
    run_bottom_tri()


while(True): #사각형 운동과 원 운동
    run_circle()
    run_rectangle()
    run_triangle()
    
    

close_canvas()
