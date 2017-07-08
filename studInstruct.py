def studentInstructor():
    print "Part 1"
    print ""
    students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    for student in students:
            print student['first_name'] + " " + student['last_name']
    print ""
    print "Part 2"
    print ""

    users = {
        'Students': [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'}
        ],
        'Instructors': [
            {'first_name' : 'Michael', 'last_name' : 'Choi'},
            {'first_name' : 'Martin', 'last_name' : 'Puryear'}
        ]
    }
    for key in users:
        print key
        num = 0
        for count in users[key]:
            num += 1
            sum = len(count['first_name']) + len(count['last_name'])
            print "{} - {} {} - {}".format(num,count['first_name'].upper(),count['last_name'].upper(),sum)
           
studentInstructor() 
