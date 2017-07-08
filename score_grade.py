import random
def scoresAndGrades():
    random_num = 0
    print random_num
    print "Scores and Grades"
    for i in range(1,11):
        random_num = random.randint(60,101)
        if random_num >=90:
            print "Score: {} ; Your grade is A".format(random_num)
        elif random_num >=80:
            print "Score: {} ; Your grade is B".format(random_num)
        elif random_num >=70:
            print "Score: {} ; Your grade is C".format(random_num)
        elif random_num >=60:
            print "Score: {} ; Your grade is D".format(random_num)
    print "End of the Program"
scoresAndGrades()