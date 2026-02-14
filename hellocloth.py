import math
import time
hw="HELLOWORLD"
t=0
i=0
j=0
p=29
k=25
a=0
c=[196,202,208,214,220,226,190,154,118,82,46,47,48,49,50,51,45,39,33,27,21,57,93,129,165,201,200,199,198,197]
print("\033[?25l")
mystr=[" "]*(p*2+2)
while(True):
	print("\033[H",end="")
	for i in range(p*2+2):
		mystr[i]=" "
	for i in range(k):
		pa=a
		a=round(p*math.sin(i*0.45+t/12)*math.sin(i*0.04+t/150))
		if i==0:
			pa=a
		for j in range((a if pa>a else pa),(pa if pa>a else a)):
			mystr[p+j+1]=f'\033[38;5;{c[(i-t//7)%30]}m{hw[(i-1)%len(hw)]}'
		print(''.join(mystr))
	time.sleep(1/60)
	t+=1
