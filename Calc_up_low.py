#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.



def up_low(s):
    
    up = 0
    low =0 
    for _ in s:
        if _.isupper():
            up+= 1
            
        elif _.islower():
            low+= 1
            
        else:
            pass

    print(f'No. of Upper Case Characters : {up}')
    print(f'No. of Lower Case Characters : {low}')



up_low(s = 'Hello Mr. Rogers, how are you this fine Tuesday?')
up_low(s = 'Hello Mr.Ramshiv')
