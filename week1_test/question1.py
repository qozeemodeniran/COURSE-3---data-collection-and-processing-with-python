# -*- coding: utf-8 -*-
""" --QUESTION
The variable nested contains a nested list. Assign ‘snake’ to 
the variable output using indexing.

nested = [['dog', 'cat', 'horse'],
          ['frog', 'turtle', 'snake', 'gecko'], 
          ['hamster', 'gerbil', 'rat', 'ferret']] """

# --SOLUTION
nested = [['dog', 'cat', 'horse'],
          ['frog', 'turtle', 'snake', 'gecko'], 
          ['hamster', 'gerbil', 'rat', 'ferret']]

output = nested[1][2]
print(output)