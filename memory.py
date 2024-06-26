from random import *
from turtle import *

from freegames import path

car = path('car.gif')
# Initialize the game with a set of letters instead of numbers, doubled for pairing
tiles = list("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEF") * 2
state = {'mark': None, 'taps' : 0}  # Track the current marked tile
hide = [True] * 64  # Track visibility of each tile, initially all are hidden

def square(x, y):
    """
    Draw a white square with a black outline at (x, y).

    Parameters:
    x (int): The x-coordinate of the square.
    y (int): The y-coordinate of the square.
    """
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    spot = index(x, y)
    mark = state['mark']

    if spot not in range(64) or not hide[spot]:
        return  # Ignora taps fuera de los cuadros o en cuadros ya descubiertos

    state['taps'] += 1  # Incrementa el contador de taps

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    if all(not h for h in hide):  # Verifica si todos los cuadros están descubiertos
        print("Todos los cuadros han sido descubiertos!")

def draw():
    """
    Draw the image and tiles, updating the game's visual state.
    """
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y + 5)  # Centering the text
        color('black')
        write(tiles[mark], align="center", font=('Arial', 30, 'normal'))

    goto(150, 120)  
    color('black')
    write("Taps: " + str(state['taps']), align="center", font=('Arial', 20, 'normal'))

    update()
    ontimer(draw, 100)

# Game initialization
shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
