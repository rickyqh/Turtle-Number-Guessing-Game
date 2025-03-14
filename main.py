import turtle
import random
import time
screen=turtle.getscreen()
screen.setup(800,800)
screen.bgcolor("gold")
screen.title("Advanced updated 2.0 turtle")

turt=turtle.getturtle()
turt.speed(1)

def drawcircle():
    turt.penup()
    turt.goto(0,-100)
    turt.pendown()
    turt.circle(100)
    turt.penup()
def drawcross():
    turt.goto(-100,100)
    turt.pendown()
    turt.goto(100,-100)
    turt.penup()
    turt.goto(100,100)
    turt.pendown()
    turt.goto(-100,-100)

def write_text(text):
    turt.penup()
    turt.goto(0,-200)
    turt.pendown()
    turt.write(text,align='center')

def write_score(text):
    turt.penup()
    turt.goto(0,200)
    turt.pendown()
    turt.write(text,align='center')


def draw_arrow_up():
    turt.penup()
    turt.goto(0,-100)
    turt.pendown()
    turt.goto(0,100)
    turt.goto(-50,50)
    turt.penup()
    turt.goto(50,50)
    turt.pendown()
    turt.goto(0,100)
def draw_arrow_down():
    turt.penup()
    turt.goto(0,100)
    turt.pendown()
    turt.goto(0,-100)
    turt.goto(50,-50)
    turt.penup()
    turt.goto(-50,-50)
    turt.pendown()
    turt.goto(0,-100)
score=0

while True:
    random_number=random.randint(1,10)

    num_of_guesses=0
    while True:
        write_score(f"Score:{score}")
        guess_num=int(turtle.textinput("Input","guess a number"))
        turt.reset()
        num_of_guesses+=1

        if guess_num<random_number:
            draw_arrow_up()
            write_text("The number higher")
        elif guess_num>random_number:
            draw_arrow_down()
            write_text("The number lower")
        else:
            score+=1
            drawcircle()
            write_text(f"you made {num_of_guesses} tries")
            break
    if score==2:
        time.sleep(2)
        screen.reset()
        write_text("you win")
        break

input("enter to stop game")