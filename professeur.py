import random

def get_level():
    while True:
        level_difficulty = int(input("What level, beginner, intermediate or genius ? [1, 2, 3]"))
        if level_difficulty in [1,2,3]:
            return level_difficulty

get_level()