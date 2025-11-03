# def swap(x, y):
#    """
#    Task 1
#    - Create a function that would swap the value of x and y using only x and y as variables.
#    - x and y must be numeric.
#    - Return -1 if x and y is not numeric, and
#    - print the swapped values if both x and y are numeric.
#    """
#    return
#
#
# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
def swap(x,y):
  x, y=y, x
  import numbers
  if isinstance(x, numbers.Number) and isinstance(y, numbers.Number):
      print("x=",x,"y=",y)
  else:
      return -1

swap ("Apple",10)
swap (9,17)
