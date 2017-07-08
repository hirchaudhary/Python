def typeList(arr):
    str_container = ''
    sum = 0
    count = 0
    count1 = 0
    for i in range(0,len(arr)):
        if type(arr[i]) == int:
            sum += arr[i]
            count +=1
        if type(arr[i]) == str:
            str_container += arr[i] + ' '
            count1 += 1
    if count < 1:
        print "The array you entered is of type String"
        print "String: " + str_container
    elif count1 < 1:
        print "The array you entered is of type Integer"
        print "Sum = ", sum 
    else:
        print "The array you entered is of mixed types"
        print "String: " + str_container
        print "Sum = ", sum 
typeList([34,'hir',65,'chaudhary',565])