def turn_right():
    turn_left()
    turn_left()
    turn_left()

def one_take():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

i = 0
for i in range(0,6):
    one_take()
