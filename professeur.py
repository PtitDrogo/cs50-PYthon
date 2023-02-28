import random

def main():
    Difficulty = get_level()
    while True:
        problem = generate_integer(Difficulty)
        print(problem)

def get_level():
    while True:
        level_difficulty = int(input("What level, beginner, intermediate or genius ? [1, 2, 3]"))
        if level_difficulty in [1,2,3]:
            return level_difficulty
        

def generate_integer(level):
    
    if level == 1:
        X = random.randint(1,9)
        Y = random.randint(1,9)
        math_problem = X + Y
        return math_problem
        
    elif level == 2:
        X = random.randint(10,99)
        Y = random.randint(10,99)
        math_problem = X + Y
        return math_problem
    
    elif level == 3:
        X = random.randint(100,999)
        Y = random.randint(100,999)
        math_problem = X + Y
        return math_problem
