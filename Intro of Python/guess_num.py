import random
answer = int(random.uniform(1,10))
number = int(input('guess number:'))

if number == answer:
	print("good guess!")
while number!= answer:
	if number > answer:
		print ('this number is bigger than the answer')
		number = int(input('try again:'))
	if number < answer:
		print ('this number is smaller than the answer')
		number = int(input('try again:'))
	if number == answer:
		print('bingo!')
		break;