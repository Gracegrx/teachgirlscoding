#!/usr/bin/env python
#coding:utf-8

print "I am a %s and my height is %d cm!" %('girl', 170)

list = ['apple', 'iphone', 2016, 2017]
print list
del list[2]
print list

tup1 = (1,2,3)
tup2 = ('apple',)
tup3 = tup1+tup2
print tup3

dict = {'name': 'grace', 'sex': 'female', 'hobby': 
'code'}
print dict['name']
dict['school'] = 'u of t'
print dict
del dict['sex']
print dict
print dict.keys()
print dict.values()
#delete all items in dict
dict.clear()
#delete the dictionary
del dict
num = 0
while(num<10):
	num += 1
	if num%2 > 0:
		continue
	print num
print '---------'
num = 0
while 1:
	print num
	num += 1
	if num>5:
		break

