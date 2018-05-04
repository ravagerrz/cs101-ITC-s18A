## IMPORTS GO HERE

## END OF IMPORTS


### YOUR CODE FOR cumulative_marks() FUNCTION GOES HERE ###
def cumulative_marks(marks):
    if marks == None:
        return None
    marks = (list(tuples) for tuples in marks)   
    lst1 = []

    for k in marks:
        var = k[0]
        b = var.replace(var[0],'')
        a = b.replace(b[2:],'P-'+ b[2:])
        var2 = (k[2:])
        
        lst3 = []

        for j in var2:
            if j == None:
                continue
            elif j == 'A':
                continue
            else:
                lst3.append(j)
    
        sum1 = sum(lst3)
        lst2 = k[0:2]
        lst2[0]=a
        lst2.append(sum1)
        lst1.append(tuple((lst2)))
        
        
    return lst1


#### End OF MARKER

if __name__ == '__main__':
    results = [
        ('p101111', 'Muhammad Amin', 64, 78.5, 89, 25, 99),
        ('p101112', 'Tehseen Khan', 14, 28.5, 83, 76),
        ('p101113', 'Tauqeer Ali', 87, None, 1.6)
    ]

#    print cumulative_marks(results)
    # output: [('10P-1111', 'Muhammad Amin', 355.5), ('10P-1112', 'Tehseen Khan', 201.5), ('10P-1113', 'Tauqeer Ali', 88.6)]

