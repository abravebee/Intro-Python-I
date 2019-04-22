"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

print('y is %f' %y) # %.2f will round to the second decimal place
print('x is %d, y is %.2f, z is %s' %(x, y, z))
# conversion types (%d, %s, etc) require certain datay types to work

# Use the 'format' string method to print the same thing
formatString = 'x is {}, y is {:.2f}, z is {}'
print(formatString.format(x, y, z))
# formatting with auto field numbering? YES. 1:.2f vs :.2f

# Finally, print the same thing using an f-string
print(f'x is {x}, y is {y:.2f}, z is {z}')