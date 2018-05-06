def calculate_sgpa(y):
    total_marks=0
    total_number_of_subjects=0.0
    list()
    if type(y)!=list:
        y=[y]
    if not y:
        return 0
    if not y:
        return None
    for x in y:
        if x=='None':
            return None
        elif x == 'A+' or x=='A':
            total_number_of_subjects+=1
            total_marks=total_marks+4.00
        elif x=='A-':
            total_number_of_subjects+=1
            total_marks=total_marks+3.67
        elif x=='B+':
            total_number_of_subjects+=1
            total_marks=total_marks+3.33
        elif x=='B':
            total_number_of_subjects+=1
            total_marks=total_marks+3.00
        elif x=='B-':
            total_number_of_subjects+=1
            total_marks=total_marks+2.67
        elif x=='C+':
            total_number_of_subjects+=1
            total_marks=total_marks+2.33
        elif x=='C':
            total_number_of_subjects+=1
            total_marks=total_marks+2.00
        elif x=='C-':
            total_number_of_subjects+=1
            total_marks=total_marks+1.67
        elif x=='D+':
            total_number_of_subjects+=1
            total_marks=total_marks+1.33
        elif x=='D':
            total_number_of_subjects+=1
            total_marks=total_marks+1.00
        elif x=='F':
            total_number_of_subjects +=1
            total_marks=total_marks+0.00
        else:
            return None
    if total_number_of_subjects==0:
        return 0
    else:
        SGPA=total_marks/total_number_of_subjects
        return SGPA
#### End OF MARKER

### YOUR CODE FOR calculate_sgpa_weighted() FUNCTION GOES HERE ###
def calculate_sgpa_weighted(a,b):
    total_score=0
    if type(a)!=list:
        a=[a]
    if type(b)!=list:
        b=[b]
    if(len(a)!=len(b)):
        return None
    for grade in a:
        if grade=="None":
            return None
        elif grade=='A+'or grade=='A':
            total_score=total_score+4.00
        elif grade=='A-':
            total_score=total_score+3.67
        elif grade=='B+':
            total_score=total_score+3.33
        elif grade=='B':
            total_score=total_score+3.00
        elif grade=='B-':
            total_score=total_score+2.67
        elif grade=='C+':
            total_score=total_score+2.33
        elif grade=='C':
            total_score=total_score+2.00
        elif grade=='C-':
            total_score=total_score+1.67
        elif grade=='D+':
            total_score=total_score+1.33
        elif grade=='D':
            total_score=total_score+1.00
        elif grade=='F':
            total_score=total_score+0.00
        else:
            return None
    for weightage in b:
        if weightage == 'None':
            return 'None'
        elif weightage == 4:
            return 4
        else:
            weightage == 3
            return 3
        a.append (grade)
        b.append (weightage)
        SGPA=([[grade]*[b]])/b
        return SGPA

#### End OF MARKER
