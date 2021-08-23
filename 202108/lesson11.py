#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/23 9:06
# @Author : ma.fei
# @File : lesson11.py
# @Software: PyCharm


# 定义字符串
s = "What are you doing ? Are you ready ?"

# 截取字符串，获取单词you,第一个数字表示从哪个位置开始截取，第二个数字表示到哪个位置结束，不包括最后一个位置的字符
# 字符串从左到右位置是从0,1,2,3...计数的
# print() 可以不用输入
print(s[9:12])

# 截字单词ready,字符串最后一个位置是-1,倒着数依次是-2,-3...
print(s[-7:-2:])
