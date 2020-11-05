# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):

    p_7 = nums.index(7)
    p_0 = nums.index(0)

    nums.pop(p_0)
    nums.insert(p_0,"#")

    b = nums.index(0)
    #print(nums)

    a = nums.index('#')
    '''print(f'Position of 3 : {a}')
    print(f'Positon of another 3: {b}')
    print(f'Position of 7: {p_7}')'''

    if a < b < p_7:
        print(True)
    else:
        print(False)

    
spy_game([1,2,4,0,0,7,5]) 
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])
