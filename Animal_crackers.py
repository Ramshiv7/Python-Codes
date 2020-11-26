#Compare the First Letter of Each word and returns True if Matches, Else False


def animal_crackers(text):
    msg = text.lower().split(" ")

    print(msg[0][0] == msg[1][0])

animal_crackers('Levelheaded Llama')
animal_crackers('Crazy Kangaroo')
