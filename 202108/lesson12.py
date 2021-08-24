#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/24 8:38
# @Author : ma.fei
# @File : lesson12.py
# @Software: PyCharm

# 字符串连接
s1 = "How are you ?"
s2 = "Fine,thank you, and you ?"
print(s1+' '+s2)

# 输出复复字符串,或字符
s3 ="apple "
print(s3*10)
print('q'*20)

# 输出重复字符: jlust(从字符左边填充一样的字符
s3="*"
print(s3.ljust(10,s3))
print('^'+s3.ljust(10,s3)+"@")

# 输出重复字符: rjust从字符右边填充相同的字符
s4="#"
print(s4.rjust(10,s4))
print('^'+s4.rjust(10,s4)+"@")
print()

# 输出左倒三角形
s1='★'
print(s1.ljust(5,s1))
print(s1.ljust(4,s1))
print(s1.ljust(3,s1))
print(s1.ljust(2,s1))
print(s1.ljust(1,s1))
print()

# 输出右倒三角形
s1='*'
s2=' '
print(s1*5)
print(s2*1+s1*4)
print(s2*2+s1*3)
print(s2*3+s1*2)
print(s2*4+s1*1)

# 输出心图案
s1='★'
print(s1.rjust(9))
print(s1.rjust(7)+s1*3)
print(s1.rjust(5)+s1*5)
print(s1.rjust(3)+s1*7)
print()

# 作业：输出星形三角形
s1='★'
print(s1.rjust(1))
print(s1.rjust(2,s1))
print(s1.rjust(3,s1))
print(s1.rjust(4,s1))
print(s1.rjust(5,s1))


