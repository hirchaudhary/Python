
# we use comments like this
# no semicolon in line end
''' many 
lines comment
'''

def hello():
    hw = "hello world"
    h = "hello"
    a = '10'
    b = 20
    c = 0
    print hw.split()
    vaeggie = ['lettuce', 'cucumber', 'carrots']
    fruits = ['apple','banana']
    fv = fruits + vaeggie
    print len(fv)
    salad = 3 * vaeggie
    print salad
    print fruits[1]
    fruits.append('grapes')
    print fruits
    c = a + b
    print c
    print 'not matched'
    i = 0
    while len(vaeggie) > i:
        print vaeggie[i]
        i += 1
    else:
        print "end"
    print 'now we r out {} {}'.format(a, b)
hello()