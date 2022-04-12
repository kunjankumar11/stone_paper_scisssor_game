import random

def play():
	turns=3
	Upoints=0
	Cpoints=0
	while turns>0:
		user=input("What's your choice? 'r'for rock,'p'for paper,'s'for scissor\n")
		computer=random.choice(['r','p','s'])
	
	
		if is_win(user,computer):
			Upoints=Upoints+1
			print('your score in this round is =1 ')
		else:
			Cpoints=Cpoints+1
			print('your score in this round is =0 ')
		turns=turns-1
	
	print('your total score is = ',Upoints)
	
	if Cpoints>Upoints:
		return 'Ulost'
	elif Upoints>Cpoints:
		return 'you won'
	else:
		return 'it\'s a tie'
	
def is_win(player,opponent):
	if(player=='r' and opponent=='s')or(player=='p' and opponent=='r')or(player=='s' and opponent=='p'):
		return True
print(play())
	
