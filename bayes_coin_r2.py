#-*- coding:utf-8 -*-#
from sympy import *
theta=Symbol('theta')
k=Symbol('k')
beforeP = 1         #事前分布の平均
headORtail = 0    #表か裏か
count = 0

while True:
    count+=1
    print
    print "Negative:0   Positive:1 please input a number:"
    headORtail = input()
    print "Before Distribution theta mean= ",beforeP
    if headORtail == 1:
        thetaT = theta
    elif headORtail == 0:
        thetaT = 1-theta
    
    #1=k(尤度(thetaT)*事前分布(beforeP)
    eq = Eq(1,k*integrate(beforeP*thetaT, (theta, 0, 1)))       #規格化の条件でkを求める
    print eq
    print "k =",solve(eq, k)
    result = solve(eq, k)[0]*beforeP*thetaT
    print "pi( theta| D",count,") = ", result
    if headORtail == 1:
        print "After Distribution theta mean = ",integrate(result*thetaT,(theta,0, 1))
    elif headORtail == 0:
        print "After Distribution theta mean = ",1-integrate(result*thetaT,(theta,0, 1))
    beforeP = result
    plot(result,(theta,-2.0,2.0),axis_center='center')
