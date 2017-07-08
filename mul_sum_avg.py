def printOdd():
    print "Print Odd Numbers....."
    for i in range(1,1000):
        if i % 2 == 1:
            print i
    print ""

printOdd()

def mul():
    print "Multiplies by 5"
    for j in range(5, 1000000, 5):#iterates through loop and adds 5 each time
        print j
    print ""

mul()

def sumofArray(arr):
    sum = 0
    for k in range(0,len(arr)):
        sum += arr[k]
    print sum

sumofArray([3,6,8,3,2,7,4,2,5,7])

def avgofArray(array):
    sum = 0
    avg = 0
    for k in range(0,len(array)):
        sum += array[k]
    avg = sum/len(array)
    print avg
avgofArray([3,6,8,3,2,7,4,2,5,7])
    