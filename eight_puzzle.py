""" eight_puzzle.py """
import copy
class State:
    def __init__(self, b, r, c):
        # b   = a list showing the tile locations
        # r,c = the row and column of the blank
        self.b = b
        self.r = r
        self.c = c

    def __str__(self):
        return str(self.b)

    def __repr__(self):
        return str(self)

    def pretty_print(self):
        print("+---"*3 + "+")
        for i in range(9):
            print("|", self.b[i], end=" ")
            if i % 3 == 2:
                print("|")
                print("+---"*3 + "+")

    def move_blank_to(self, new_r, new_c):
        tmp = self.b[self.r*3 + self.c]
        self.b[self.r*3 + self.c] = self.b[new_r*3 + new_c]
        self.b[new_r*3 + new_c] = tmp
        self.r = new_r
        self.c = new_c

def initial_state():
    b = [7, 2, 4, 5, 0, 6, 8, 3, 1]
    r = 1
    c = 1
    return State(b, r, c)

def is_goal(s):
    return s.b == [1, 2, 3, 4, 5, 6, 7, 8, 0]

def is_valid_location(r, c):
    if r >= 0 and r <= 2 and c >= 0 and c <= 2:
        return True
    return False

def successors(s):
    # Case 1: Try to move the blank up
    new_r = s.r-1
    new_c = s.c
    if is_valid_location(new_r, new_c):
        t = copy.deepcopy(s)
        t.move_blank_to(new_r, new_c)
        yield (t, 1)

    # Case 2: Try to move the blank down
    new_r = s.r+1
    new_c = s.c
    if is_valid_location(new_r, new_c):
        t = copy.deepcopy(s)
        t.move_blank_to(new_r, new_c)
        yield (t, 1)
    
    # Case 3: Try to move the blank to the left
    new_r = s.r
    new_c = s.c-1
    if is_valid_location(new_r, new_c):
        t = copy.deepcopy(s)
        t.move_blank_to(new_r, new_c)
        yield (t, 1)

    # Case 4: Try to move the blank to the right
    new_r = s.r
    new_c = s.c+1
    if is_valid_location(new_r, new_c):
        t = copy.deepcopy(s)
        t.move_blank_to(new_r, new_c)
        yield (t, 1)
