#Every Even positioned letter should be lower case and odd positioned - upper case

def myfunc(args):
    output = ''
    a = len(args)

    for i in range(a):
        for _ in args[i]:
            if i%2 == 0:
                output = output + _.lower()
            else:
                output = output + _.upper()

    print(output)

myfunc('Anthropomorphism')
