""" water.py """
# Define how to represent a state
class State:
    # Each state stores the amount of water in both bottles
    def __init__(self, x, y):
        self.x = x  # amount of water in bottle X
        self.y = y  # amount of water in bottle Y
    
    def __str__(self):
        # Convert a state into a string
        return "[%d, %d]" % (self.x, self.y)

    def __repr__(self):
        # Representation of a state
        return str(self)

# Define the initial state
def initial_state():
    # We start from the state where both bottles are empty
    return State(0, 0)

# Define how to check if a state is a goal state
def is_goal(s):
    # It is a goal when bottle Y contains 4 liters
    if (s.y == 4):
        return True
    return False

# Define how to generate successors according to the problem
def successors(s):
    # This function returns a list of (state, cost) pairs
    # where state is a successor of s, and
    #       cost  is the cost required to generate this state
    # Case 1: Try to empty the bottle X
    if s.x > 0:
        # State(0, s.y) = a state where X is empty and 
        #                 Y remains unchanged
        # Cost = s.x since we throw away the water in X
        yield (State(0, s.y), s.x)

    # Case 2: Try to empty the bottle Y
    if s.y > 0:
        yield (State(s.x, 0), s.y)

    # Case 3: Try to fill up the bottle X
    if s.x < 3:
        yield (State(3, s.y), 3-s.x)

    # Case 4: Try to fill up the bottle Y
    if s.y < 5:
        yield (State(s.x, 5), 5-s.y)

    # Case 5: Try to pour water from X to Y
    t = 5-s.y   # available space of Y
    if s.x > 0 and t > 0:
        if s.x > t:
            # Pour until Y is full
            yield (State(s.x-t, 5), t)
        else:
            # Pour until X is empty
            yield (State(0, s.y+s.x), s.x)

    # Case 6: Try to pour water from Y to X
    t = 3-s.x   # available space of X
    if s.y > 0 and t > 0:
        if s.y > t:
            # Pour until X is full
            yield (State(3, s.y-t), t)
        else:
            # Pour until Y is empty
            yield (State(s.x+s.y, 0), s.y)
