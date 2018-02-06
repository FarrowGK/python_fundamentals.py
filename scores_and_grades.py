def scores_and_grades(score):
    if score >= 90:
        print "Score", score, " Your grade is an A"
    elif score >= 80:
        print "Score", score, " Your grade is a B"
    elif score >= 70:
        print "Score", score, " Your grade is a C"
    elif score >= 60:
        print "Score", score, " Your grade is a D"
    else:
        print "Study Harder"

import random
score = random.randint(0, 100)
scores_and_grades(score)





