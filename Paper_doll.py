#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

def paper_doll(text):

    #print(text)
    output = ''
    for i in text:
        for j in range(3):
            output+= i
    print(output)


paper_doll('Hello')
paper_doll('Mississippi')
