from sympy import *
range_first=0   #range
range_last=1
theta=Symbol('theta')
k=Symbol('k')
priorD = 1 #prior probability
posORnega = 0
count = 0

while True:
    count+=1
    print
    print "Negative:0   Positive:1 please input a number=>"
    posORnega = input()
    print "Prior Distribution = ",priorD
    if posORnega == 1:
        thetaT = theta
    elif posORnega == 0:
        thetaT = 1-theta
    
    eq = Eq(1,k*integrate(priorD*thetaT, (theta, range_first, range_last)))
    print eq
    solList=solve(eq, k)
    print "k =",solList[0]
    result = solList[0]*priorD*thetaT
    print "Posterior Distribution pi( theta| D",count,") = ", result
    print "Mean ",thetaT," = ",integrate(result*thetaT,(theta,range_first, range_last))
    priorD = result