"""
Very simple, given a number, find its opposite.

Examples:

1: -1
14: -14
-34: 34
"""

def opposite(number):
  if number  > 0:
        number *= -1
  else:
        number *= -1
  
  return number

print(opposite(5))