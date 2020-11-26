##MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(text):
    a = text.split(" ")
    a.reverse()
    b = " ".join(a)
    print(b)

master_yoda("i am home")
master_yoda('We are ready')
