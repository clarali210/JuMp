## import
from livewires.beginners import *
from random import randrange

## play theme throughout the game
music.track = "theme.mid"
music.play(-1)

## let player choose from 4 backgrounds
s = input("Choose your background, input 1, 2, 3, or 4 --> ")
if s == 1:
    screen.background = "background.jpg"
if s == 2:
    screen.background = "background2.jpg"
if s == 3:
    screen.background = "background3.jpg"
if s == 4:
    screen.background = "background4.jpg"

## one or two player game
p = input("How many players, input 1 or 2 --> ")
if p == 1:
    mode = "one"
elif p == 2:
    mode = "two"

## let player choose the size of the ball
ball = Sprite(
    image="ball.png", x=screen.width / 2, bottom=screen.height / 4, dy=-7)

b = input("Choose your player, input 1, 2, or 3 --> ")
if b == 1:
    ball.image = "ball.png"
if b == 2:
    ball.image = "ball_medium.png"
if b == 3:
    ball.image = "ball_large.png"

if mode == "two":
    ball.x = screen.width * 3 / 4
    ball0 = Sprite(
        image="ball.png", x=screen.width / 4, bottom=screen.height / 4, dy=-7)
    b0 = input("2. Choose your player, input 1, 2, or 3 --> ")
    if b0 == 1:
        ball.image = "ball.png"
    if b0 == 2:
        ball.image = "ball_medium.png"
    if b0 == 3:
        ball.image = "ball_large.png"

## let player choose the ground
ground = Sprite(
    image="ground2.png",
    right=randrange(50, screen.width),
    bottom=randrange(ball.bottom, screen.height))

g = input("Choose a platform, input 1 or 2 --> ")
if g == 1:
    ground.image = "ground.png"
if g == 2:
    ground.image = "ground2.png"

if mode == "two":
    ground0 = Sprite(
        image="ground2.png",
        right=randrange(50, screen.width),
        bottom=randrange(ball.bottom, screen.height))
    g0 = input("2. Choose a platform, input 1 or 2 --> ")
    if g0 == 1:
        ground0.image = "ground.png"
    if g0 == 2:
        ground0.image = "ground2.png"

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

if mode == "two":
    c0 = input("2. Choose the color of text, input 1, 2, 3, or 4 --> ")
    if c0 == 1:
        COLOR0 = blue
    if c0 == 2:
        COLOR0 = red
    if c0 == 3:
        COLOR0 = black
    if c0 == 4:
        COLOR0 = dark_gray

## text displayed in the game
score = Text(value=0, size=50, color=COLOR, x=screen.width - 30, y=30)

move = Text(
    value="Use the left and right arrow keys to avoid falling",
    size=25,
    color=purple,
    x=screen.width / 2,
    y=30)
start = Text(
    value="Press the space key to start",
    size=50,
    color=purple,
    x=screen.width / 2,
    y=screen.height / 2)

end = Text(
    value="Game Over",
    size=50,
    color=purple,
    x=screen.width / 2,
    y=screen.height / 2)

best_score = Text(
    value=0, size=50, color=COLOR, top=end.bottom + 10, x=screen.width / 2)
new_best = Text(
    value="New Best Score: ",
    size=50,
    color=COLOR,
    x=screen.width / 2,
    top=end.bottom + 10)

if mode == "two":
    score0 = Text(value=0, size=50, color=COLOR0, x=30, y=30)

## sound effects
collide = Sound("collide.wav")
fall = Sound("fall.wav")
bounce = Sound("bounce.wav")

## initiate game status
status = "Start"

## main loop
while not keyboard.is_pressed(K_ESCAPE):

    ## erase
    ball.erase()
    ground.erase()
    score.erase()
    if mode == "two":
        ball0.erase()
        ground0.erase()
        score0.erase()
    move.erase()
    best_score.erase()

    ## start
    if status == "Start":
        start.draw()
        x = 0
        best_score.x = screen.width / 2
        ball.x = screen.width / 2
        ball.y = screen.height / 4
        ball.dy = -5
        score.value = 0
        if mode == "two":
            ball.x = screen.width * 3 / 4
            ball0.x = screen.width / 4
            ball0.y = screen.height / 4
            ball0.dy = -5
            score0.value = 0
        if keyboard.is_pressed(K_SPACE):
            start.erase()
            status = "In Game"
        if keyboard.is_pressed(K_RETURN):
            status == "Settings"

    ## in game
    if status == "In Game":

        ball.y += ball.dy
        ball.x += ball.dx

        ball.dy += 0.3

        if (ball.left < 0):
            ball.right = screen.width
        if (ball.right > screen.width):
            ball.left = 0

        if keyboard.is_pressed(K_LEFT):
            ball.x -= 7
        if keyboard.is_pressed(K_RIGHT):
            ball.x += 7

        if (ball.bottom >= screen.height):
            if x == 0:
                fall.play()
                x = 1
            ball.top = screen.height
            status = "End"

        if ball.overlaps(ground):
            ground.right = randrange(ground.width, screen.width)
            ground.left = randrange(0, screen.width - ground.width)
            ground.bottom = randrange(ball.bottom, screen.height)
            ball.dy *= -1
            ball.dx *= -1
            score.value += 1
            collide.play()

        if mode == "two":
            ball0.y += ball0.dy
            ball0.x += ball0.dx

            ball0.dy += 0.3

            if (ball0.left < 0):
                ball0.right = screen.width
            if (ball0.right > screen.width):
                ball0.left = 0

            if keyboard.is_pressed(K_a):
                ball0.x -= 7
            if keyboard.is_pressed(K_d):
                ball0.x += 7

            if ball.bottom >= screen.height:
                ball0.top = screen.height

            if (ball0.bottom >= screen.height):
                if x == 0:
                    fall.play()
                    x = 1
                ball0.top = screen.height
                ball.top = screen.height
                status = "End"

            if ball0.overlaps(ground):
                ground.right = randrange(ground.width, screen.width)
                ground.left = randrange(0, screen.width - ground.width)
                ground.bottom = randrange(ball.bottom, screen.height)
                ball.dy *= -1
                ball.dx *= -1
                score.value += 1
                collide.play()

            if ball0.overlaps(ground0):
                ground0.right = randrange(ground0.width, screen.width)
                ground0.left = randrange(0, screen.width - ground0.width)
                ground0.bottom = randrange(ball0.bottom, screen.height)
                ball0.dy *= -1
                ball0.dx *= -1
                score0.value += 1
                collide.play()

            if ball.overlaps(ground0):
                ground0.right = randrange(ground0.width, screen.width)
                ground0.left = randrange(0, screen.width - ground0.width)
                ground0.bottom = randrange(ball.bottom, screen.height)
                ball.dy *= -1
                ball.dx *= -1
                score.value += 1
                collide.play()

            if ball.overlaps(ball0):
                ball.dy *= -1
                ball.dx *= -1
                ball.left = ball0.right
                ball0.dy *= -1
                ball0.dx *= -1
                bounce.play()

    ## end
    if status == "End":
        if score.value > best_score.value:
            best_score.value = score.value
            best_score.left = new_best.right
            best_score.color = COLOR
            new_best.color = COLOR
            new_best.draw()
        if mode == "two":
            if score0.value > score.value and score0.value > best_score.value:
                best_score.value = score0.value
                best_score.left = new_best.right
                best_score.color = COLOR0
                new_best.color = COLOR0
                new_best.draw()
            elif score.value == score0.value:
                new_best.color = purple
                best_score.color = purple
        best_score.draw()
        end.draw()
        if keyboard.is_pressed(K_SPACE):
            new_best.erase()
            end.erase()
            status = "Start"

    ## draw
    ball.draw()
    ground.draw()
    score.draw()
    if mode == "two":
        ball0.draw()
        ground0.draw()
        score0.draw()
    move.draw()

    ## update
    screen.update()

pygame.quit()
