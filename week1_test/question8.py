# -*- coding: utf-8 -*-

"""
--QUESTION

Iterate through the contents of l_of_l and assign the third element of
sublist to a new list called third.
 
l_of_l = [
          ['purple', 'mauve', 'blue'], 
          ['red', 'maroon', 'blood orange', 'crimson'], 
          ['sea green', 'cornflower', 'lavender', 'indigo'], 
          ['yellow', 'amarillo', 'mac n cheese', 'golden rod']
        ]
"""

# --ANSWER
l_of_l = [
          ['purple', 'mauve', 'blue'], 
          ['red', 'maroon', 'blood orange', 'crimson'], 
          ['sea green', 'cornflower', 'lavender', 'indigo'], 
          ['yellow', 'amarillo', 'mac n cheese', 'golden rod']
        ]

third = []
for stuffs in l_of_l:
    third.append(stuffs[2])
print(third)