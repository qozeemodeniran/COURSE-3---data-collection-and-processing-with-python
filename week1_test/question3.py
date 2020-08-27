# -*- coding: utf-8 -*-
"""
--QUESTION
Below, we’ve provided a list of lists. Use in statements to create 
variables with Boolean values - see the ActiveCode window for further 
directions.

L = [[5, 8, 7], 
     ['hello', 'hi', 'hola'], 
     [6.6, 1.54, 3.99], 
     ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1

# Test if [5, 8, 7] is in the list L. Save to variable name test2

# Test if 6.6 is in the third element of list L. Save to variable name 
test3

"""
#ANSWER
L = [[5, 8, 7], 
     ['hello', 'hi', 'hola'], 
     [6.6, 1.54, 3.99], 
     ['small', 'large']]

test1 = 'holla' in L

test2 = L[0] in L

test3 = L[2][0] in L[2]

