#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/9 8:46
# @Author : ma.fei
# @File : lesson07.py.py
# @Software: PyCharm

import math

# 计算表达式值

# 1.已知,a=10,b=4,求（a+b)/(a-b)的值
a=10
b=4
y=(a+b)/(a-b)
print('(a+b)/(a-b)=',y)


# 2.已知 x=3,求 x**2+2*x+1的值
x=3
y=x**2+2*x+1
print('x**2+2*x+1=',y)


# 3.求 y=x**2+3*x+2的两个根
a=1
b=3
c=2
x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
print('x1=',x1)
print('x2=',x2)