#Pick out the Even Numbers from the given numbers

output = []

def myfunc(*args):
    for _ in args:
        if _%2== 0:
           output.append(_)
    return output

myfunc(2,3,4,5,6,7,8)
print(output)
