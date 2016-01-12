import copy

# Set size of the board
N = 8
class NQueen:
    def __init__(self):
        self.b = [0]*N
        self.n = 0

    def __str__(self):
        return str(self.b)

    def __repr__(self):
        return str(self)

    def pretty_print(self):
        print("+---"*N + "+")
        for i in range(1, N+1):
            row = ""
            for j in range(N):
                if self.b[j] == i:
                    row += "| Q "
                else:
                    row += "|   "
            row += "|"
            print(row)
            print("+---"*N + "+")

def initial_state():
    s = NQueen()
    s.b[s.n] = 2;
    s.n += 1;
    return s

def is_goal(s):
    if s.n == N:
        return True
    return False

def attack(r1, c1, r2, c2):
    # return True when the queen at row r1, column c1 attacks
    # the queen at row r2, column c2
    if r1 == r2 or c1 == c2:
        # Two queens are on the same row or column
        return True
    if (r1-r2) == (c1-c2) or (r1-r2) == (c2-c1):
        # Two queens are on the same diagonal line
        return True
    return False 

def is_okay_to_add(s, q):
    # return True when adding a queen into a state s at row q
    # does not cause any attack
    for i in range(s.n):
        if attack(s.b[i], i, q, s.n):
            return False
    return True

def successors(s):
    # Try to place a queen on the next column
    for i in range(1, N+1):
        if is_okay_to_add(s, i):
            t = copy.deepcopy(s)
            t.b[t.n] = i
            t.n += 1
            yield (t, 1)
