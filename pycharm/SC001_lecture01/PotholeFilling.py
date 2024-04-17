"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
   for i in range(3):
       go_in()
       put_99_beeper()
       go_out()


def go_in():
    """
    pre-condition Karel is on the upper left of the pothole, facing east
    post-condition Karel is in the pothole, facing south
    """
    move()
    turn_right()
    move()


def go_out():
    """
    pre-condition Karel is in the pothole, facing south
    post-condition Karel is on the upper left of the pothole, facing east
    """
    turn_left()
    turn_left()
    move()
    turn_right()
    move()



    """
    TODO:
    """
    """
    move()
    turn_right()
    move()
    put_99_beeper()
    turn_left()
    turn_left()
    move()
    turn_right()
    move()
    move()
    turn_right()
    move()
    put_99_beeper()
    turn_left()
    turn_left()
    move()
    turn_right()
    move()
    move()
    turn_right()
    move()
    put_99_beeper()
    turn_left()
    turn_left()
    move()
    turn_right()
    move()
    """

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def put_99_beeper():
    for i in range(99):
        put_beeper()

# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
