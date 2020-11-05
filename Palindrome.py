# Write a Python function that checks whether a word or phrase is palindrome or not

def palindrome(s):

    s = s.replace(" ","")
    
    if s == s[::-1]:
        print(True)
    else:
        print(False)


palindrome('helleh')
palindrome('kayak')
palindrome('racecar')
palindrome('nurses run')
palindrome('breakpoint')
