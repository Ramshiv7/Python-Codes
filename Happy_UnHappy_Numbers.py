'''Input: n = 19
Output: True
19 is Happy Number,
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1 '''


n = input()

a = int(n[0]) 
b = int(n[1])

res = str(n)

res_list = []


while int(res) > 1 and (int(res) not in res_list):
    
        
    if res != 1  :
        if len(str(res)) == 2 :
            tmp = str(res)
            x = tmp[0]
            y = tmp[1]
            res_list.append(res)
            res_temp = int(x) ** 2 + int(y) ** 2
            res = res_temp
            
            
            
            
        elif len(str(res)) == 3 :
            tmp = str(res)
            x = tmp[0]
            y = tmp[1]
            z = tmp[2]
            res_list.append(res)
            res_temp = int(x) ** 2 + int(y) ** 2 + int(z) ** 2 
            res = res_temp
            
            
            
            
        else:
            pass
    
    else:
        print("its an unhappy")
        break

    
    
    print(res)


print(res_list)


