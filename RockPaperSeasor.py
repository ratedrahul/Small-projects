import random
import time
star = '*'
space = ' '
star * 25
star * 25
print(space * 10, 'Welcome to Rock Paper Seasor Game ')
star * 25
star * 25
A_Point = 0
B_point = 0
liss = ['Rock','Paper','Scissor']
print('A turn:\nRock Paper Scissor \n\nEnter:\n ')
while A_Point != 15  or B_point != 15:
	A_turn = input()
	# A = input('1st Player: ')
	# print('Second Player will be Computer:')

	x = random.choice(liss)
	print('...............'+x)
	all_input = [A_turn,x]
	time.sleep(3)
	if 'Rock' and 'Paper' in all_input:
		if A_turn == 'Paper':
			A_Point+=5
		else:
			B_point+=5
	if 'Paper' and "Scissor" in all_input:
		if A_turn == "Scissor":
			A_Point+=5
		else:
			B_point+=5
if A_Point>B_point:
	print('Bingo\n')
	print('A is clear winner here with points',A_Point)
else:
	print('Bingo\n')
	print('Mr. Computer is winner here with points ',B_point)
	print()

	time.sleep(2)

	# if A_turn == 'Rock' and x =='Paper':
	


# print(x)
# print()
# print(A, 'pick -- ', A_turn)
# print(B, 'pick -- ', B_turn)
