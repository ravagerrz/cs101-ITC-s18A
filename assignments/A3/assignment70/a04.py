## IMPORTS GO HERE if required

## END OF IMPORTS 


#### YOUR CODE FOR uniqueEntries GOES HERE ####
def uniqueEntries (n):
    lst1 = []
    lst2=[]
    for i in n:
        if i not in lst1:
            lst1.append(i)
        else:
            lst2.append(i)
    return lst1 ,lst2
        


#### End OF MARKER ----uniqueEntries



if __name__ == '__main__':
    uniqueEntries([12,24,35,24,88,120,155,88,120,155])
