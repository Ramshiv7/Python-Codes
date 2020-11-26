#Print the Prime Numbers till the provided range

def prime_no(num):
    for i in range(2,num):
        if i % 2 == 0 :
            pass
        elif i % 2!=0 and i//1 ==i:
            print(i)

prime_no(27)
