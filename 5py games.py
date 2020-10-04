import pygame
import pyaudio
import playsound
import winsound

import turtle
from turtle import*
import tkinter
from tkinter import *
import random
from pygame import mixer

#winsound.PlaySound("endofline.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
#from playsound import playsound
#playsound("endofline.wav")
pygame.init()

mixer.music.load("endofline.wav")
mixer.music.play(-1)

tit = turtle.Screen()
tit.title("Pong")
tit.bgcolor("black")
tit.setup(width=800, height=600)
tit.tracer(0)



# score
score_a = 0
score_b = 0

#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed()
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=7, stretch_len=1, outline=2)
paddle_a.color("green")
paddle_a.penup()
paddle_a.goto(-350,0)


###paddle b

paddle_b = turtle.Turtle()
paddle_b.speed()
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=7, stretch_len=1, outline=2)
paddle_b.color("green")
paddle_b.penup()
paddle_b.goto(+350,0)

##
###ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball.dx = 1
ball.dy = -1
ball.vel = [ball.dy, ball.dx]

pen = turtle.Turtle()
pen.speed(0)
#pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "bold"))



#paddle control
def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)


#keyboard input

tit.listen()
tit.onkeypress(paddle_a_up, "w")
tit.onkeypress(paddle_a_down, "s")
tit.onkeypress(paddle_b_up, "Up")
tit.onkeypress(paddle_b_down, "Down")
#game loop
while True:
    tit.update()

    #winsound.PlaySound("endofline.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
#move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

# define the border/ top bottm#ycor
    if ball.ycor() > 290:
              
             
        ball.dy *= -1
        winsound.PlaySound("pongbounce", winsound.SND_ASYNC)
    if ball.ycor() < -290:
              
               
        ball.dy *= -1
        winsound.PlaySound("pongbounce", winsound.SND_ASYNC)    
    

# right border side
    if ball.xcor()>350:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}" .format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

#        winsound.PlaySound("pongbounce", winsound.SND_ASYNC)#sound on the right
#left side
        
    if ball.xcor()<-350:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        
        pen.write("Player A: {} Player B:{} " .format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
#        winsound.PlaySound("pongbounce", winsound.SND_ASYNC)# ound on the left
# paddle and ball meet ball.setx(340)#ball.setx(-340)< 350) and (ball.ycor()#> -350) and (ball.ycor() apaddl
    
    if(ball.xcor() > 340 and ball.ycor()  < paddle_b.ycor()+ 50 and ball.ycor() > paddle_b.ycor()-50):
        
        ball.dx *= -1
        winsound.PlaySound("pongbounce", winsound.SND_ASYNC)
        
    elif(ball.xcor() < -340 and ball.ycor()  < paddle_a.ycor()+ 50 and ball.ycor() > paddle_a.ycor()-50):
        
        ball.dx *= -1
        winsound.PlaySound("pongbounce", winsound.SND_ASYNC)
#        winsound.PlaySound("endofline.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
tk.mainloop()
        
turtle.done()














