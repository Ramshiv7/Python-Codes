#Simple Try and Except 

try:
	for i in [0,1,2]:
		print(i**2)
except:
	print('Oops! Error Occured')


#Simple - Try, Except, and Finally


x = 5
y = 0

try :
	z = x/y
except ZeroDivisionError:
	print("Can't Divide by Zero !!!")
finally:
	print('Calculation Completed')


#Function that takes integer as input and returns square. use Try, excvept, else, and finally to catch error.

def sqr():
    
    while True:
        try:
            num = int(input('Please enter a integer: '))
        except:
            print('OOps!! Invalid input')
            continue
        else:
            print(f'Squared number is: {num**2}')
            break


sqr()
