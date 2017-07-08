
def draw_star(arr):
    print "Started Printing Star:"
    for x in arr:
        print "*" * x
    print "Ended printing stars"
draw_star([10,12,18,7,16,15,4,3,2,3,4,5,6,7,8,9,10])


def draw_thing(array):
    print array
    string = ""
    for z in array:
        if type(z) == int:
            print "*" * z
        if type(z) == str:
            for k in range(0,len(z)):
                string += z[0]
            print string.lower() 
            string = ""
draw_thing([2,"Hir",8,6,9,8,"Chaudhary"])