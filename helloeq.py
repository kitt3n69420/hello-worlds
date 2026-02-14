import time
import math
import random
hw="HELLO,WORLD!"
dec=0.08
bh=10
bb=2
br=0.09
w=60
h=25
i=0
j=0
cc=0
n=0
t=0
o=4
p=0.36
mline=""
def getCol():
	l=0
	while(l<12 or l>20):
		r=random.randint(0,5)
		g=random.randint(0,5)
		b=random.randint(0,5)
		l=g*4+r*2+b
	return r*36+g*6+b+16
def calcCol(c:int,d:int):
	m=c-16
	r=m//36
	g=m//6%6
	b=m%6
	r*=d
	g*=d
	b*=d
	r=5 if r>5 else (0 if r<0 else r)
	g=5 if g>5 else (0 if g<0 else g)
	b=5 if b>5 else (0 if b<0 else b)
	return 16+36*int(r)+6*int(g)+int(b)
cl=[118 for _ in range(w)]
bl=[0]*w
print("\033[?25l")
while(True):
	print("\033[H",end="")
	for i in range(w): # make next frame
		bl[i]=0 if random.random()<br*math.fabs(1-math.sin(math.fmod(t*p,0.7853981634)))else bl[i]+dec
	for i in range(o,h+o): # render frame
		mline=""
		for j in range(w):
			n=(i/bh-bl[j])
			n=0 if n<0 else bb-n
			cc=calcCol(cl[j],n)
			mline+="\033[38;5;"+str(cc)+"m"+hw[j%len(hw)]
		print(mline)
	time.sleep(1/60)
	t+=1
