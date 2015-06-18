from sympy import *
range_first=0   #range
range_last=1
theta=Symbol('theta')
k=Symbol('k')
beforeP = 1
posORnega = 0
count = 0

while True:
    count+=1
    print
    print "Negative:0   Positive:1 please input number:"
    posORnega = input()
    print "Before Production = ",beforeP
    if posORnega == 1:
        thetaT = theta
    elif posORnega == 0:
        thetaT = 1-theta
    
    eq = Eq(1,k*integrate(beforeP*thetaT, (theta, range_first, range_last)))
    print eq
    solList=solve(eq, k)
    print "k =",solList[0]
    result = solList[0]*beforeP*thetaT
    print "pi( theta| D",count,") = ", result
    print "After Production ",thetaT," = ",integrate(result*thetaT,(theta,range_first, range_last))
    beforeP = result

    
    
'''
#Second
print
print "Second"
beforeP = result #upload
print beforeP
eq = Eq(1,k*integrate(beforeP*theta,(theta,range_first, range_last)))
print eq
solL=solve(eq, k)
print "k =",solve(eq, k)
result = solL[0]*beforeP*theta
print "pi(theta|D2) = ", result

print integrate(result*theta,(theta,range_first, range_last))
'''
