#------------------------------------------------------------------------------------------------------------------------
# Program name – draw.py
# Written by – Naylene
# Date – April 9, 2017
# This program contains the functions for drawing
#--------------------------------------------------------------------------------------------------------------------------

def drawSquare(turtle, sidelength):
    """Draw a square"""
    turtle.clear()
    turtle.reset()
    turtle.pencolor("Black")
    for i in range(4):
        turtle.forward(sidelength)
        turtle.right(90)
        
def drawRectangle(turtle, sidelength):
    """Draw a Rectangle"""
    turtle.clear()
    turtle.reset()
    turtle.pencolor("Black")
    for i in range(2):
        turtle.forward(sidelength)
        turtle.right(90)
        turtle.forward(sidelength*2)
        turtle.right(90)


def nightVale(turtle,logo):
    """Draw Night Vale Logo"""

    if logo == 1:      #Allows entire design to be drawn
        turtle.clear()
        turtle.reset()
        #Backgrounds

        size = 3.5

        turtle.pensize(size)
        turtle.speed(0)


        for i in range(18):
            turtle.up()
            turtle.goto((-77)*size,(-71+ i)*size)
            turtle.down()
            turtle.pencolor("Black")
            turtle.forward((77)*size)
            
        for i in range(18, 71):
            turtle.up()
            turtle.goto((-77)*size,(-71+ i)*size)
            turtle.down()
            turtle.pencolor("#891C4F")
            turtle.forward((77)*size)

        #Black Designs
            #House
        x = 0
        y = 0
        move = 0
        for i in range(8):
            turtle.up()
            turtle.goto((-69 + x)*size,(-53 + y)*size)
            turtle.down()
            turtle.pencolor("Black")
            turtle.forward((30 + move)*size)
            x = x + 2
            y = y + 1
            move = move - 4

        #Antennae
        turtle.up()
        turtle.goto((-46)*size, (-53)*size)
        turtle.down()
        turtle.left(90)
        turtle.pencolor("Black")
        turtle.forward((7)*size)
        turtle.up()
        turtle.goto((-47)*size, (-53)*size)
        turtle.down()
        turtle.pencolor("Black")
        turtle.forward((10)*size)
        turtle.left(90)
        turtle.forward(2*size)
        turtle.right(180)
        turtle.forward(4*size)
        turtle.left(90)
        turtle.forward(1*size)
        turtle.left(90)
        turtle.forward(2*size)
        turtle.right(180)
        turtle.forward(4*size)

        #Logo
        #Background
        redact = 0
        x = 0
        y = 0
        for i in range(10):
            turtle.pencolor("#5F0B59")
            turtle.up()
            turtle.goto((-72 + x)*size, (-20 + y)*size)
            turtle.down()
            turtle.forward(140 + redact *size)
            x = x + 2
            y = y + 1
            redact = redact - 4

        redact = 0
        x = 0
        y = 0
        for i in range(10):
            turtle.pencolor("#5F0B59")
            turtle.up()
            turtle.goto((-73 + x)*size, (-20 - y)*size)
            turtle.down()
            turtle.forward(140 + redact *size)
            x = x + 2
            y = y + 1
            redact = redact - 4

        #Eye
        turtle.pencolor("#891C4F")
        turtle.fillcolor("#891C4F")
        turtle.up()
        turtle.goto((-53)*size, (-25)*size)
        turtle.down()
        turtle.begin_fill()
        turtle.circle(5*size)
        turtle.end_fill()

        #Moon
        turtle.pencolor("White")
        turtle.fillcolor("White")
        turtle.up()
        turtle.goto((-53)*size, (-17)*size)
        turtle.down()
        turtle.right(180)
        turtle.begin_fill()
        turtle.circle(3*size,180)
        turtle.end_fill()



        #Electric Tower
        turtle.pencolor("Black")
        turtle.up()
        turtle.goto((-29)*size, (-57)*size)
        turtle.down()
        turtle.left(90)
        turtle.forward(52*size)
        turtle.up()
        turtle.goto((-28)*size, (-57)*size)
        turtle.down()
        turtle.forward(52*size)
        turtle.up()
        turtle.goto((-28)*size, (-8)*size)
        turtle.down()
        turtle.right(90)
        turtle.forward(3*size)
        turtle.up()
        turtle.goto((-29)*size, (-8)*size)
        turtle.down()
        turtle.left(180)
        turtle.forward(3*size)

        #Wires
        turtle.right(220)
        turtle.up()
        turtle.goto((-25)*size, (-8)*size)
        turtle.down()
        turtle.circle(25*size,17.5*size)
        turtle.up()
        turtle.goto((-27)*size, (-8)*size)
        turtle.down()
        turtle.right(70)
        turtle.circle(27*size,20*size)

    if logo == 2:            #Allows only the eye to be drawn
        turtle.clear()
        turtle.reset()
        size = 3.5

        turtle.pensize(size)
        turtle.speed(0)

        #Background
        redact = 0
        x = 0
        y = 0
        for i in range(10):
            turtle.pencolor("#5F0B59")
            turtle.up()
            turtle.goto((-72 + x)*size, (-20 + y)*size)
            turtle.down()
            turtle.forward(140 + redact *size)
            x = x + 2
            y = y + 1
            redact = redact - 4

        redact = 0
        x = 0
        y = 0
        for i in range(10):
            turtle.pencolor("#5F0B59")
            turtle.up()
            turtle.goto((-73 + x)*size, (-20 - y)*size)
            turtle.down()
            turtle.forward(140 + redact *size)
            x = x + 2
            y = y + 1
            redact = redact - 4

        #Eye
        turtle.pencolor("#891C4F")
        turtle.fillcolor("#891C4F")
        turtle.up()
        turtle.goto((-53)*size, (-25)*size)
        turtle.down()
        turtle.begin_fill()
        turtle.circle(5*size)
        turtle.end_fill()

        #Moon
        turtle.pencolor("White")
        turtle.fillcolor("White")
        turtle.up()
        turtle.goto((-53)*size, (-17)*size)
        turtle.down()
        turtle.right(180)
        turtle.begin_fill()
        turtle.circle(3*size,180)
        turtle.end_fill()
