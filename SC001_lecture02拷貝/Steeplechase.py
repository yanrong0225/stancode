"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()



def jump():
    """
    pre-con: karel is on the left of the wal, facing East.
    post-con karel is facing north
    :return:
    """
    up()
    cross()
    down()
    turn_left()
def down():
    """
    pre-con: karel is at the upper right, facing east
    :return:
    """
    turn_right()
    while front_is_clear():
        move()
def cross():
    """
    pre-con: karel is facing north
    post-con: karel is at the upper right, facing south
    :return:
    """
    turn_right()
    move()
def turn_right():
    """
    karel will turn right
    :return:
    """
    turn_left()
    turn_left()
    turn_left()


def up():
    """
    Pre-con: karel is on the lest side of the wall, facing east
    post-con:karel is facing north
    """
    #facing north
    turn_left()
    while not right_is_clear():
        move()

    """
    while not front_is_clear():
        turn_left()
        move()
        turn_left()
        turn_left()
        turn_left()
    """

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
