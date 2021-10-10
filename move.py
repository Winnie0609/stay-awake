import pyautogui
import random
import sys
import time

errorMsg = """Please key in a valid number.
try: python move.py 3
"""

def checkInput():
	if len(sys.argv) > 1 :
		input = sys.argv[1]
	else:
		input = 3

	try:
		num = int(input)
		move(num)
	except ValueError:
		print(errorMsg)

def move(num):
	timeRange = num * 30

	for i in range(timeRange):
		print(i)
		randomIntX = random.randint(1, 1910) 	#screen resolution
		randomIntY = random.randint(1, 1070)
		x = randomIntX
		y = randomIntY

		print(x, y)
		pyautogui.moveTo(x, y, duration = 0.3)
		time.sleep(2)

checkInput()