#Write a Python function to multiply all the numbers in a list.

def multiply(numbers):

    out = 1
    for i in numbers:
        out = out * i

    print(out)

multiply([1,2,3,-4])
multiply([2,3,4,5,6,7,8])
