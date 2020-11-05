#FIND33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.


def has_33(num):

    pos_3 = num.index(3)
    
    if pos_3 == 0:
        if num[0] == 3 and num[1] == 3:
            print(True)
        else:
            print(False)
    elif pos_3 == 1:
        if num[0] == 3 and num[1] ==3 or num[1] ==3 and num[2] == 3:
            print(True)
        else:
            print(False)
   


has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3])
