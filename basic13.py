def print1to255():
    for i in range(1,256):
        print i
        
#print1to255()

def printOdds():
    for i in range(1,256):
        if i % 2 == 1:
            print i
#printOdds()

def intsAndSum():
    sum = 0
    for i in range(0,256):
        sum += i
        print i, sum

#intsAndSum()

def array(arr):
    print arr

#array([24,35,56,7,23])

def printMax(arr):
    max = 0
    for i in range(0,len(arr)):
        if arr[i] > max:
            max = arr[i]
    print max

#printMax([23,67,4,578,34,45])

def average(arr):
    sum = 0
    for i in range(0,len(arr)):
        sum += arr[i]
    avg = sum / len(arr)
    print avg

#average([34,56,4,2477,3434])

def oddsArray():
    arr = []
    for i in range(1,256):
        arr.append(i)
    print arr

#oddsArray()

def square(arr):
    for i in range(0, len(arr)):
        arr[i] *= arr[i]
    print arr

#square([1,3,5,3,12,7])

def greaterThanY(arr, y):
    count = 0
    for i in range(0, len(arr)):
        if arr[i] > y:
            count += 1
            print count, arr[i]

#greaterThanY([3,6,3,7,2], 5)

def negativeZero(arr):
    for i in range(0, len(arr)):
        if arr[i] < 0:
            arr[i] = 0
    print arr

#negativeZero([3,6,-3,7,2])

def minMaxAvg(arr):
    sum = 0
    max = arr[0]
    min = arr[0]
    avg = 0
    for i in range(0,len(arr)):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
        sum += arr[i]
    print max, min, sum/len(arr)

#minMaxAvg([23,67,4,578,34,45])

def shiftArray(arr):
    for i in range(0, len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr)-1] = 0
    print arr

#shiftArray([5,3,6,3,7,67,3])

def swap(arr):
    for i in range(0, len(arr)):
        if arr[i] < 0:
            arr[i] = 'Dojo'
    print arr

swap([5,34,87,-28,34])