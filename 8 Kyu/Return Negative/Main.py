"""
In this simple assignment you are given a number and have to make it negative. 
But maybe the number is already negative?

Examples
make_negative(1);  # return -1
make_negative(-5); # return -5
make_negative(0);  # return 0
"""

# MY PROGRAM
def make_negative( number ):
    if number  > 0:
        number *= -1
    else:
        number *= 1
   
    return number

print(make_negative(-5))


# SOLUSI DARI PARA MASTER

# Pertama
# def make_negative( number ):
#     return -abs(number)

# Kedua
# def make_negative( number ):
#     return (-1) * abs(number)

# Ketiga
# def make_negative(number):
#     if number >= 0:
#         return (0 - number)
#     else:
#         return number