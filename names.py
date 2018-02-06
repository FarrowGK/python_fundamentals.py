def names(students):
    for names in students:
        print names["first_name"], names["last_name"]
students = [
     {'first_name' :  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
names(students)
def names(users):
    count1 = 0
    count2 = 0
    print "Students"
    for names in range(0, len(users["Students"])):
        totalsfname = len(users["Students"][count1]["first_name"])
        totalslname = len(users["Students"][count1]["last_name"])
        length1 = totalsfname + totalslname       
        print count1 + 1, users["Students"][count1]["first_name"], users["Students"][count1]["last_name"], length1
        count1 += 1
    print "Instructors"
    for names in range(0, len(users["Instructors"])):
        totalifname = len(users["Instructors"][count2]["first_name"])
        totalilname = len(users["Instructors"][count2]["last_name"])
        length2 = totalifname + totalilname  
        totaliname = users["Instructors"][count2]["first_name"], users["Instructors"][count2]["last_name"]
        print count2 + 1, users["Instructors"][count2]["first_name"], users["Instructors"][count2]["last_name"], length2
        count2 += 1
        
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
names(users)

