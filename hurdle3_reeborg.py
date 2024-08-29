def turn_right():
    turn_left()
    turn_left()
    turn_left()

def one_take():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        one_take()
    else:
        move()
