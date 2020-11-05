''''BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'''

def blackjack(a,b,c):
    out = 0
    sumi = a+b+c
    if sumi <= 21:
        print(sumi)
    elif sumi > 21 and a == 11 or b == 11 or c == 11:
        out = sumi - 10
        print(out)
    else: 
        print('BUST')

    

blackjack(5,6,7) 
blackjack(9,9,9) 
blackjack(9,9,11)
blackjack(8,8,20)
blackjack(1,2,11)
