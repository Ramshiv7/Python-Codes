#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(name):

    return f'{name[0].upper()}{name[1:3]}{name[3].upper()}{name[4:]}'

old_macdonald('macdonal')
