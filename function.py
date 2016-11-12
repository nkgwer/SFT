import math

def saw(x):
	return x%math.pi
def kukei(x):
	if(x%(2*math.pi)<math.pi):
		return 1
	else:
		return -1
names=[saw,kukei]