drive = input('Can u drive?: ')
if drive != 'yes' and drive != 'no':
	print('Please Insert ( yes / no )')
	raise SystemExit
	
age = input('Your Age:')
age = int(age)
if drive == 'yes':
	if age >= 18:
		print('U pass the test.')
	else:
		print('Why u can drive? U are under aged!')
elif drive == 'no':
	if age >= 18:
		print('Why dont u go to get a license?')
	else:
		print('Nevermind, u can get a license after 17 years old.')