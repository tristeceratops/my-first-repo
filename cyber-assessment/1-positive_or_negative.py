#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
text = ""
if number == 0:
    text = "is zero"
elif number > 0:
    text = "is positive"
else:
    text = "is negative"
text = "" + str(number) + " " + text
print(text)