dict = {
	'Hello':'Hello', 
	'Nice to meet you':'Nice to meet you, too',
	'Which fruit do you like best':'I like apple very much',
	'How old are you':'20 years old',
	'You are handsome': 'Thank you'
}

flag = 'c'
work = True

print 'Hi, my name is Python.'
print 'Do you want to chat with me?'
while flag == 'c' or 't':
	flag = raw_input('You can choose to chat with me(c) or train me(t), or let me leave(l)?(c/t/l)  ')
	if flag == 't':
		question = raw_input('please type in question: ')
		answer = raw_input('please type in answer: ')
		dict[str(question)] = str(answer)
		print 'success!'
		print 'Now I can answer %d questions!' % len(dict)
		continue
	elif flag == 'c':
		if len(dict) == 0:
			print 'I cannot answer any question now, please train me first!'
			continue
		chat_word = raw_input('Thank you for talking with me, what do you want to say to me?: ')
		for key in sorted(dict.keys()):
			if str(chat_word) == key:
				work = True
				print dict[key]
				break
			else:
				work = False
			if work == False:
				print 'sorry, I cannot answer this question.'
				work = True
	elif flag == 'l':
			print 'Fine, see you next time!'
			break
	else:
			print 'please type in your choice.'
			continue

