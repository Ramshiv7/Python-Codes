# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
import string

def panagram(s):
    out = 0
    x = string.ascii_lowercase
    for i in x:
            if i in s:
                    out+=1
            else:
                    pass
    if out == 26:
            print(True)
    else:
            print(False)


#Panagram Inputs 
panagram("The quick brown fox jumps over the lazy dog")
panagram("waltz nymph for quick jigs vex bud dmitri borgmann")
panagram("sphinx of black quartz judge my vow")
panagram("pack my box with five dozen liquor jugs mark dunn")
panagram("glib jocks quiz nymph to vex dwarf")
panagram("jackdaws love my big sphinx of quartz")
panagram("the five boxing wizards jump quickly")
panagram("how vexingly quick daft zebras jump")
panagram("quick zephyrs blow vexing daft jim")
panagram("two driven jocks help fax my big quiz")
panagram("the jay pig fox zebra and my wolves quack")
panagram("sympathizing would fix quaker objectives")
panagram("a wizards job is to vex chumps quickly in fog")
panagram("watch jeopardy alex trebeks fun tv quiz game")
panagram("by jove my quick study of lexicography won a prize")
panagram("waxy and quivering jocks fumble the pizza")
#Not a Panagram Input 
panagram("wax and quivering jocks fumble the pizza")
