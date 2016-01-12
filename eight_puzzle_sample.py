""" eight_puzzle_sample.py """
import eight_puzzle as p
s1 = p.initial_state()
print("s1 is")
s1.pretty_print()
print("Successors of s1 are")
for t,c  in p.successors(s1):
    t.pretty_print()
