# Use the Filter method to check the Even numbers from a given list 

def check_even(num):
    if num % 2 == 0:
        return num
    else:
        pass

lst = [1,2,3,4,5,6,7,8]

filter(check_even,lst)
