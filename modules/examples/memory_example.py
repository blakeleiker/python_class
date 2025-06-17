"""
This file contains a quick intro to how the memory model in python works. 

This is heavily inpired by this blog post:
https://nedbatchelder.com/text/names.html 
"""

# This line assigns a new name, x, which refers to a list with the given elements.
x = [2,5,7]

# In python, multiple names can refer to the same value.
# This line creates a new name, y, which refers to the same list as x.
# Another way to say this is that we are assigning the value of x to y. 
# Note that no data is being copied here! We have created a new name, y, which refers to
# the same list as x. 
y = x

# Check the memory address of the value of both x and y. They are equal!
print(f"Value of x: {x}")
print(f"Value of y: {y}")
print(f"id of x: {id(x)}")
print(f"id of y: {id(y)}")
assert id(x) == id(y)
assert x is y

# In the above example, the name "y" refered to the same value as "x".
# In the following example, we create a new list for both "a" and "b". 
# Note that just because two lists are equal, it does not mean they are the
# same list!
a = [1,2,3]
b = [1,2,3]

# Check the memory address of the value of both a and b. They are different, showing
# that these names refer to different objects.
print(f"Value of a: {a}")
print(f"Value of b: {b}")
print(f"id of a: {id(a)}")
print(f"id of b: {id(b)}")
assert id(a) != id(b)
assert a is not b

# In python, lists are mutable objects, meaning they are able to change "in place".
# Adding a new number to the list doesn't change the value of x or y.
x.append(9)
print(f"Value of x after x.append(9): {x}")
print(f"Value of y after x.append(9): {y}")
assert id(x) == id(y)

# An important implication of name assignment: When calling a function, assignment is 
# performed to create a new reference to the value inside the scope of the function. 
# This means that any operations performed on mutable objects inside of a function will 
# reflected in all other names which refer to that same object! 
# In other words, when we call my_func(x), we are assigning the local function variable 
# func_list to have the same value as x, similar to how we assigned the name y to have 
# the same value as x earlier with "y=x". 
def my_func(func_list):
    func_list.append(99)

my_func(x)

print(f"Value of x after my_func(x): {x}")
print(f"Value of y after my_func(x): {y}")
assert id(x) == id(y)

# Its very important to understand when a value is being mutated in place and when a 
# name is being reassigned. Its possible to design another function which rebinds the value
# of the argument to a new list, rather than operating on the input list.
def my_func2(func_list):
    # Adding 2 lists together creates a new list with the contents of both input lists.
    # Here, we are re-assigning the value of func_list to point to a newly created list,
    # so it no longer points to the same value as the original input.
    func_list = func_list + [100]
    return func_list

returned_value = my_func2(x)

# Check the value of both x and y. Note that they were not modified by my_func2.
print(f"Value of x after my_func2(x): {x}")
print(f"Value of y after my_func2(x): {y}")
print(f"Value of returned_value:      {returned_value}")
assert id(x) == id(y)