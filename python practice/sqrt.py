def sqrt(x , guess=0.0):
    if x<0.00000:
        return None
    
    if good_enough(guess ,x):
        return guess
    else:
        new_guess = improve_guess(guess ,x)
        return sqrt(x ,new_guess)

		
def good_enough(guess,x):
    if abs(float(guess * guess - x)) < 0.00001:
        return True
    else:
        return False

#### End OF MARKER

#### YOUR CODE FOR average() FUNCTION GOES HERE ####
def average(guess ,x):
    A = (abs(guess + x)/2.00000)
    return A
