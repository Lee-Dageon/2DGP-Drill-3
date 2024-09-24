from pico2d import *

open_canvas()

grass=load_image('grass.png')
boy=load_image('character.png')

#코딩에 있어서 첫번째로 생각해야 할 것. 나무를 보지 말고 숲을 봐야 한다.
#사각형 운동과 원 운동 무한루프

while(True): #사각형 운동과 원 운동
    run_rectangle()
    run_circle()
    

close_canvas()
