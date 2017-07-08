def compare_array(arr, arrnew):
    count = 0
    for i in range(0, len(arr)):
        if arr[i] != arrnew[i]:
            count += 1
    if count > 0:
        print "The lists are not same"
    else:
        print "The lists are same."
        
compare_array([1,2,3],[1,2,3])