""" water_sample.py """
import water

s1 = water.initial_state()
print("initial state =", s1)
print("is_goal(s1) =", water.is_goal(s1))
print("successors(s1) =", end=" ")
for s in water.successors(s1):
    print(s, end=" ")
print()
print("-----------------")

s2 = water.State(3, 4)
print("s2 =", s2)
print("is_goal(s2) =", water.is_goal(s2))
print("successors(s2) =", end=" ")
for s in water.successors(s2):
    print(s, end=" ")
print()
