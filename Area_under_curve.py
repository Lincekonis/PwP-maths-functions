#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 14:18:44 2022

@author: second
"""
import math
import matplotlib.pyplot as plt

def testf(x):
    return x**2+2

def eulerf(t):
    return 2*t
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
'''
The function takes as input a function g of one argument, two floats a and b, and an
integer n. It returns a float which estimates the integral g(t)dt by a
calculating the area of n (evenly spaced) trapeziums.
'''   
def trapez_integ(g, a, b, n):
    A = 0                                    
    h = b - a
    interval = h / n
    for i in range(int(n)):
        h = (a+interval + i * interval) -  (a + i * interval)
        partial_area = h*((g(a + i * interval) + (g(a+interval + i * interval)))/2)
        A = A + partial_area
    return A
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
'''
Suppose we are given an autonomous ODE f′(t) = g(t) and an initial value f (a). 
This function uses the equation f (b) = (intrgral of) b f′(t) dt + f(a) and a
the trapez_integ function to return a float which is an estimate of f(b).
'''
def trapez_ode(g, a, fa, b, n):
    trapezode = trapez_integ(g,a,b,n)
    print(trapezode)
    fb = trapezode + fa
    return fb
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
'''
Not finished
'''
def euler(g, a, fa, b, steps):
    fti_list = []
    h = (b-a)/steps
    fti = fa
    fti_list.append(round(fti,2))
    for i in range(steps):
        ti=fa+h*i
        fti = fti + h * g(ti,fti)
        fti_list.append((ti,round(fti,2)))
        plt.plot(fti,ti)
    plt.xlabel('time')
    plt.ylabel('y(t)')
    plt.show()
    return fti_list
