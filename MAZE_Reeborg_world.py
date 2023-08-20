def turn_right():
    turn_left()
    turn_left()
    turn_left()


#To be able to fix the endless loop    
while front_is_clear():
    move()
    
turn_left()



# to be able to tackle walls 
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    
    elif front_is_clear():
        move()
    
    else:
        turn_left()