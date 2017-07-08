def checkBoard():
    char = "*"
    space = " "
    multBy = 4
    for i in range(0,9):
        if i % 2 == 0:
            stringeven = (char + space) * multBy
            print stringeven
        else:
            stringodd = (space + char) * multBy
            print stringodd
checkBoard()