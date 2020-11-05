#Write a function that checks whether a number is in a given range (inclusive of high and low)


def ran_check(num,low,high):

    if num in range(low,high+1):
        print(f'{num} is in the range between {low} and {high}')
    else:
        print(f'{num} is NOT the range between {low} and {high}')


ran_check(5,2,7)
ran_check(1,2,7)
ran_check(2,2,7)
ran_check(7,2,7)
ran_check(100,22,177)
