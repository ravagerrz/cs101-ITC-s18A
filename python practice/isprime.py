def isprme1(x):
    if x<2:
        return False
    if x == 2:
        return True


    for i in range(2,x):
        if x%i == 0:
            return False
    return True
# here I;m gonna write a code for factors so,,
def output_prime_factors(given_no):
    given_no=round(given_no)
    y=0
    while given_no>y:
        y+=1
        if given_no%y==0 and isprme1(y)==True:
            print y
