'''

Functions - Exercise 1

The script defineis a function with two arguments:
get_values(arg1, arg2) 
that returns the sum, the difference, and the product 
of arg1 and arg2.

'''

def get_values(arg1, arg2):
    s = arg1 + arg2
    d = arg1 - arg2
    p = arg1 * arg2
    return s, d, p

# With default values for the arguments
def get_values_2(arg1 = 0, arg2 = 0):
    s = arg1 + arg2
    d = arg1 - arg2
    p = arg1 * arg2
    return s, d, p

sum, diff, prod = get_values_2(5, 15)
sum2, diff2, prod2 = get_values_2(15)

print "Sum: ", sum 
print "Difference: ", diff
print "Product", prod

print "Results with default arguments: ", sum2, diff2, prod2

