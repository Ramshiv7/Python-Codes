#Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(n):

    if n in range(90, 100) or n in range(100, 110):
        print(True)
    elif n in range(190, 200) or n in range(200, 210):
        print(True)
    else:
        print(False)

almost_there(90)
almost_there(104)
almost_there(150)
almost_there(209)
