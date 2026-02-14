import math
import time
hw="Hello, World "
t=0
i=0
p=24
k=20
c=[196,202,208,214,220,226,190,154,118,82,46,47,48,49,50,51,45,39,33,27,21,57,93,129,165,201,200,199,198,197]
while(True):
	print("\033[H",end="")
	for i in range(k):
		a=round(p*math.sin(i*0.3+t/12)*math.sin(i*0.02+t/150))
		print(' '*(p+a),f'\033[38;5;{c[(i-t//7)%30]}m',hw[i%len(hw)],' '*(p-a))
	time.sleep(1/60)
	t+=1
