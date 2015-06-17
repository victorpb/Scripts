#UTF-8
import os
import commands
from datetime import datetime, time, timedelta


now = datetime.now()



control_pomo = now.hour + 25 
control_break = now.hour + 5
print control_pomo
if (control_pomo / 60) < 0:
	pomo= time(now.hour, now.minute + 25 , now.second)

else:
	pomo= time(now.hour + 1, (now.minute + control_pomo) % 60  , now.second)

if (control_break) / 60 < 0:
	pomo_break= time(now.hour, now.minute + 5 , now.second)
else:
	pomo_break= time(now.hour + 1, (now.minute + control_break) % 60  , now.second)


def pomodoro(pomo, pomo_break, iterator = 0) :
	start = raw_input("You want to start the break? Yes ou No")
	
	if start.lower() == "yes":
		print "Pomodoro Iniciado termina as " + str(pomo)
		while True:
			now = datetime.now()
			
			control = time(now.hour, now.minute , now.second)
			if control != pomo:
				pass
				#fixme - print countdown				 
				
			else:
				iterator +=1
				os.system("gnome-screensaver-command -l")
				pomodoro_break(pomo, pomo_break, iterator)
	else:
		print "End pomodoro"

def pomodoro_break(pomo, pomo_break, iterator=0):
	start = raw_input("You want to start the break? Yes ou No ")
	if start.lower() == "yes":
		print "Break started it ends the" + str(pomo_break)
		while True:
			now = datetime.now()

			control = time(now.hour, now.minute , now.second)
			if control != x:
				pass
				#fixme - print countdown

			else:
				os.system("gnome-screensaver-command -l")
				pomodoro(pomo, pomo_break, iterator)
	elif start.lower() == "no":
		pomodoro(pomo, pomo_break)
	else:
		pomodoro_break(pomo, pomodoro_break) 

pomodoro(pomo, pomo_break)

