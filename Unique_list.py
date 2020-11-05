#Write a Python function that takes a list and returns a new list with unique elements of the first list.


def unique_list(lst):

    uniq = []
    
    for i in set(lst):
        uniq.append(i)

    print(uniq)


unique_list([1,1,1,1,1,2,2,2,3,3,3,3,3,0,4,4,4,4,5])
