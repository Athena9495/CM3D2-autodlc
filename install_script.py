#Run in DLC root

import os
import time
import subprocess
import pyautogui

#Mouse was located at X:850 Y:530/ X:760 Y:460 / X:750 Y:460/ X:720 Y:530 for me, on a 1366x768 laptop display.
#To find out required mouse position, fire up a console, import pyautogui, and run - pyautogui.displayMousePosition()

fp=[]

for dirname, dirnames, filenames in os.walk('.'):
     for filename in filenames:
         fp.append(os.path.join(dirname, filename))

fpath = [match for match in fp if "update.exe" in match]
del fp
u_no = len (fpath)

print "Packages to be updated: " + str(u_no)

for x in range (0,u_no):
	print "Package number: " + str (x+1)
	p = subprocess.Popen(fpath[x])
	print "Updating..."
	time.sleep(1) #Let the program come to the main view.
	pyautogui.click(850,525) #First click.
	time.sleep(1.5) #Let the secondary menu come up.
	pyautogui.click(760,455) #Second click.
	while (p.poll() is None):
		time.sleep(5) #sloppy, but should work. Suggestions for this part are welcome.
		pyautogui.click(750,445) #Third click.
		pyautogui.click(720,520) #Fourth click (exit).
	print ("Done.")

print "Updated " + str(u_no) + " packages."
