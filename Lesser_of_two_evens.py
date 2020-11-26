#Given two integers, return minimum value of two integers if both the Integers are Even.Else return the greatest of 2 integers

def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 ==0:
        print(min(a,b))
    else:
        print(max(a,b))

lesser_of_two_evens(2,4)
lesser_of_two_evens(2,5)
lesser_of_two_evens(10,5)
lesser_of_two_evens(24,100)
lesser_of_two_evens(25,99)
