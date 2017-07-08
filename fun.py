def odd_even():
    print "Even Or Odd"
    for i in range(1,2001):
        if i % 2 == 0:
            print "Number is ", i,". This is an even number"
        else:
            print "Number is ", i,". This is an odd number"

odd_even()

def multiply(arr,num):
    print " "
    print "Multiply by Num to entire array"
    print " "
    for i in range(0, len(arr)):
        arr[i] *= num
    return arr
b = multiply([4,8,3,5,6,8,1], 5)
print b

def layered_multiples(arr):
    print "Printing 1 to array"
    new_arr = []
    new_array = []
    for x in arr:
        for y in range(0,x):
            new_arr.append(1)
        new_array.append(new_arr)
        new_arr = []
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x
