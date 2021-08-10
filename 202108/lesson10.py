#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/10 9:06
# @Author : ma.fei
# @File : lesson10.py
# @Software: PyCharm

# 学习字符串常用操作
# 什么是字符串？ 双引号，单引号，三引号引住的任何字符都是字符串

# 定义字符串
s = "What are you doing ? Are you ready ?"

# 计算字符串长度，空格也算一个字符
print('字符串s的长度=',len(s))

# 将字符串中字母小写转大写
print('字符串字母小写转大写=',s.upper())

# 将字符串中字母大写转小写
print('字符串字母大写转小写=',s.lower())

# 统计某个单词出现的次数
print('统计单词you 出现次数=',s.count('you'))