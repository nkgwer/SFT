import math

def ceiling(x,p=0):
	if (p==-1):
		#starting point of the period
		return -1*math.pi
	if (p==1):
		#ending point of the period
		return 1*math.pi
	return math.ceil(5*(x%math.pi))/5

def square(x,p=0):
	if (p==-1):
		return -1*math.pi
	if (p==1):
		return 1*math.pi
	if(x%(2*math.pi)<math.pi):
		return 1
	else:
		return -1
def expwave(x,p=0):
	if (p==-1):
		return -1*math.pi
	if (p==1):
		return 1*math.pi
	if(x%(2*math.pi)<math.pi):
		return math.exp(x%math.pi)
	else:
		return -1*math.exp(x%math.pi)


names=[square,expwave,ceiling]