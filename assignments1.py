def find_replace_min_max_sort_len():
    print "Find and Replace Function"
    words = "It's thanksgiving day. It's my birthday,too!"
    print words.find('day')
    word = words.replace('day', 'month')
    print word

    print "min and max function"
    arr = [2,54,-2,7,12,98]
    print max(arr)
    print min(arr)

    print "First and Last value"
    arr = ['Hello', 2,54,-2,7,12,98, 'World']
    arrnew = []
    arrnew.append(arr[0])
    arrnew.append(arr[len(arr)-1])
    print arrnew

    print "Sort and Split"
    x = [19,2,54,-2,7,12,98,32,10,-3,6]
    x.sort()
    print "After sort:", x
    arr_a  = x[0: (len(x)/2)]
    arr_b = x[len(x)/2:len(x)]
    arr_b.insert(0,arr_a)
    print arr_b
    
find_replace_min_max_sort_len()