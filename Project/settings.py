from livewires.beginners import *
from random import randrange

def options():

    ## let player choose the size of the ball
    ball = Sprite(image = "ball.png", x = screen.width/2,
                  bottom = screen.height/4, dy = -7)

    b = input("Choose your player, input 1, 2, or 3 --> ")
    if b == 1:
        ball.image = "ball.png"
    if b == 2:
        ball.image = "ball_medium.png"
    if b == 3:
        ball.image = "ball_large.png"


    ## let player choose the ground
    ground = Sprite(image = "ground2.png",
                    right = randrange(50, screen.width),
                    bottom = randrange(ball.bottom, screen.height))

    g = input("Choose a platform, input 1 or 2 --> ")
    if g == 1:
        ground.image = "ground.png"
    if g == 2:
        ground.image = "ground2.png"


    ## let player choose the color of the text
    c = input("Choose the color of text, input 1, 2, 3, or 4 --> ")
    if c == 1:
        COLOR = blue
    if c == 2:
        COLOR = red
    if c == 3:
        COLOR = black
    if c == 4:
        COLOR = dark_gray

    return

