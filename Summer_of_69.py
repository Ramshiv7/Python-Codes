'''SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 
and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.'''

def summer_69(nums):

    def su_69():
        output = 0
        for i in nums:
            output+= i

        print(output)

    def s_69():
        output = 0
        for i in nums:
            
            if nums.index(i) >= pos_6 and nums.index(i) <= pos_9:
                pass
            else:
                output+= i
        print(output)        
    
    if 6 in nums or 9 in nums:
        pos_6 = nums.index(6)
        pos_9 = nums.index(9)
        s_69()
        
    else:
        su_69()

 


summer_69([1, 3, 5])
summer_69([4, 5, 6, 7, 8, 9])
summer_69([2, 1, 6, 9, 11])
