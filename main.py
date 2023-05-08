from random import randint
import random
import turtle
import time

#VARIABLE
game_active = True
timer= 10
score = 0
is_clicked = False

#DRAWING BOARD
drawin_board = turtle.Screen()
drawin_board.setup(500,500)
drawin_board.bgcolor("light blue")
drawin_board.title("Catch The Turtle")

#TURTLE PEN

turtle_pen = turtle.Turtle("turtle")
turtle_pen.penup()
turtle_pen.shapesize(2)

#TIMER PEN

timer_pen = turtle.Turtle()
timer_pen.hideturtle()
timer_pen.penup()
timer_pen.setposition(170,200)
timer_pen.write(arg= f"Time: {timer} ",move=False,align="center",font=10)

#SCORE PEN

score_pen = turtle.Turtle()
score_pen.penup()
score_pen.hideturtle()
score_pen.setposition(170,220)
score_pen.write(arg=f"Score: {score}",move=False,align="center",font=15)

#GAME FUNC
def play():
    turtle_pen.showturtle()
    global game_active
    global timer
    global score
    global is_clicked
    timer = 10
    score = 0
    is_clicked = False
    score_pen.clear()
    score_pen.goto(170,220)
    score_pen.write(arg=f"Score: {score}",move=False,align="center",font=15)
    game_active = True
    drawin_board.ontimer(moving_turtle, 1000)
    decreasing_time()
    turtle_pen.onclick(score_up)

#EXIT FUNC

def exit_game():
    drawin_board.bye()

#MOVING TURTLE
def moving_turtle():
    global is_clicked
    global game_active
    if is_clicked == True and game_active == True:
        turtle_pen.hideturtle()
        turtle_pen.goto(randint(-200,200),randint(-200,200))
        turtle_pen.showturtle()
        is_clicked = False

#DECREASING TIME
def decreasing_time():
    global game_active
    global timer

    if game_active:
        timer -=1
        timer_pen.clear()
        timer_pen.write(arg=timer,move=False,align="center",font=15)
        drawin_board.ontimer(decreasing_time,2000)

        if timer == 0:
            game_active = False
            drawin_board.listen()
            drawin_board.onkey(play, key="a")
            drawin_board.onkey(exit_game,key="x")

    else:
        turtle_pen.hideturtle()
        score_pen.clear()
        timer_pen.clear()
        timer_pen.penup()
        score_pen.goto(0,0)
        score_pen.write(arg=f"Your score: {score}", move=False, align="center", font=70)

#CLICKED TURTLE
def score_up(x,y):
    global score
    global is_clicked
    global game_active

    if is_clicked == False and game_active == True:
        score +=1
        is_clicked = True
        score_pen.clear()
        score_pen.write(arg=f"Your score: {score}",move=False,align="center",font=15)
        moving_turtle()

#RESET CLICKED
def reset_clicked():
    global game_active
    global is_clicked
    is_clicked = False
    drawin_board.ontimer(reset_clicked,1000)
    if game_active:
        drawin_board.ontimer(reset_clicked,1000)


drawin_board.ontimer(moving_turtle, 1000)
decreasing_time()
turtle_pen.onclick(score_up)

drawin_board.mainloop()