import random
def coinToss():
    head = 0
    tail = 0
    for i in range(1,5001):
        rand = random.randint(0,1)
        if round(rand) == 1:
            head += 1
            print "Attempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far".format(i,head,tail)
        else:
            tail += 1
            print "Attempt #{}: Throwing a coin... It's a tail! ... Got {} head(s) so far and {} tail(s) so far".format(i,head,tail)
    print ""
    print "Ending the program, thank you!"

coinToss()