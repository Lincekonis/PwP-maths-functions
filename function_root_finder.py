

def Test(x):
    return 2*x-2
   
def Test1(x):
    return 2*x**2+3*x

def Test2(x):
    return x**4+3*x**3-7*x**2+1

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
'''
The function works like the Newton-Raphson method, but does not need the derivative. 
Instead it takes an input ε > 0. it loops iters times and should return the suggested value of x if f(x)
is within tol of zero, and None otherwise.
'''
def nr_numeric(f, epsilon, start, iters, tol):
# This function looks for a root of a function
    x = start
    for i in range(int(iters)):
        x=x-f(x)/((f(x+epsilon)-f(x))/epsilon)
        
        if f(x)<=tol:
            return x
            
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
'''
The bisection method of root finding works as follows. The input is two values a and b, with a < b,
such that one of {f(a),f(b)} is positive and the other is negative. Each iteration, either a or b is
replaced with the midpoint (a + b)/2 so that, after replacement, we still have one positive and one negative
value in {f (a), f (b)}
'''
def bisect(f, a, b, iters, tol):
# This function looks for a root of a function
    if f(a) == 0:                       # checks if a user guessed a root
        return a
    if f(b) == 0:
        return b   

    if f(a) > 0:                        # checks if a function is decreasing
        for i in range(int(iters)):
            c = (a+b)/2
            if f(c) > 0:                # if mid-point is positive, 'a' value is replaced
                a=c
            elif f(c) < 0:              # if mid-point is negative, 'b' value is replaced
                b=c
                
    if f(b) > 0:                        # checks if a function is increasing
        for i in range(int(iters)):
            c = (a+b)/2
            if f(c) > 0:                # if mid-point is positive, 'b' value is replaced 
                b=c
            elif f(c) < 0:              # if mid-point is negative, 'a' value is replaced
                a=c
   
    if abs(f(a))<tol:                   # checks if a new function (y value) value is in -
        print( a )                       #   range of tolerance, if True x value will be returned
    elif abs(f(b))<tol:
        print( b )
    
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
'''
To use the bisection method, we need two numbers a and b such that f (a) and f (b) have different signs. 
Then, as long as f is continuous, f must have a root x between a and b.
'''   
def sign_pairs(f, low, high, k):
# This function looks for boundries where are roots. Answer is more precise when k<100
    numbers = [low + x*((high-low)/(k+1)) for x in range(k+2)]  # makes a list of evenly spaced numbers
    for i in range(k+1):                                        # from numbers[0] & numbers[0+1] to numbers[k+1] & numbers[k+2]
        if f(numbers[i])*f(numbers[i+1])<0:                     
            number_list=[numbers[i],numbers[i+1]]
            return(number_list)
            #return(numbers[i])
            #return(numbers[i+1])        
            
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
'''
should first use the function sign_pairs to generate a list of pairs of numbers,
then apply bisect to each pair, and should return a list of roots of f .
'''          
def multiple_bisect(f, low, high, k, iters, tol):
    sign_pairs(f, low, high, k)
    for i in range(k-2):
        high=number_list[i]
        low=number_list[i+1]
        bisect(f, high, low, iters, tol)
    