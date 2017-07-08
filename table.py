def multiplicationTable():
    string = ''
    for y in range(0,12):
        for x in range(1,14):
            if x == 13:
                print string
                string = ''
            else:
                string += " "+ str(x+y * x)
multiplicationTable()