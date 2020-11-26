#Return the Square values of the Given list using Map 

def square(num):
    return num**2

sq_lt = [2,4,32,5,6,7,89,1,9]

print(list(map(square,sq_lt)))




# Print Even for Even numbers and Odd for Odd number in the give list
def odd_eve(arr):
    if arr % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


lst = [1,2,3,4,5,6,7,8,9,10,12,14,15,16,18]

map(odd_eve,lst)

print(list(map(odd_eve,lst)))
