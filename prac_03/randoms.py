"""
CP1404/CP5632 - Practical
Random Numbers and Functions


What did you see on line 1? 19
What was the smallest number you could have seen, what was the largest?

What did you see on line 2? 5
What was the smallest number you could have seen, what was the largest? 3, 9
Could line 2 have produced a 4? No, because it starts from 3 and takes every second number- 3-5-7-9

What did you see on line 3? 3.8672125398421677
What was the smallest number you could have seen, what was the largest? 2.5, 5.5

Write code, not a comment, to produce a random number between 1 and 100 inclusive."""

import random
print(random.randint(1, 100))