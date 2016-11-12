#Slow Fourier Transform
from tqdm import tqdm
from function import*
import numpy as np
import matplotlib.pyplot as plt
steps=100000
def integrate(func,trig,sp,ep,steps,n):
	sum=0.0
	ix=sp
	dx=(ep-sp)*1.0/steps
	for i in range(steps):
		sum+=func(ix)*trig(math.pi*2.0*n*ix/(ep-sp))*dx
		ix+=dx
	return sum*2.0/(ep-sp)
def periodDetect(func):
	print "Detecting the period of the function"
	try:
		return [func(0,-1),func(0,1)],1
	except:
		return None,-1
def main():
	for num,func in enumerate(names):
		print num, func.__name__
	while(True):
		try:
			func_num=input("Enter the # of the function ")
			if(0<=func_num and func_num<len(names)):
				break
		except:
			print "failed"
	func=names[func_num]
	period,ret=periodDetect(func)
	if(ret==1):
		print "Detected period"
		sp=period[0]
		ep=period[1]
		if (sp>=ep):
			print "period was not valid"
			ret=-1
	if(ret==-1):
		print "Could not detect the period"
		while(True):
			try:
				sp=float(input("please enter the starting point of the period "))
				ep=float(input("please enter the ending point of the period "))
				if(ep>sp):
					break
				print "failed"
			except:
				print "failed"

	coslist=[]
	sinlist=[]
	f = open('SFT.txt', 'w')
	f.write("cos\n")
	while (True):
		try:
			terms=input("Enter the # of terms ")
			if(terms>0):
				break
		except:
			print"failed"

	for i in tqdm(range(terms)):
		ret=integrate(func,math.cos,sp,ep,steps,i)
		coslist.append(ret)
		f.write(str(ret))
		f.write("\n")
	f.write("sin\n")
	for i in tqdm(range(terms)):
		ret=integrate(func,math.sin,sp,ep,steps,i)
		sinlist.append(ret)
		f.write(str(ret))
		f.write("\n")

	a0=coslist[0]
	sinlist[0]=0.0
	coslist[0]=0.0

	f.close()
	funcv = np.vectorize(func)
	original=funcv(np.linspace(sp-ep,ep-sp,1000))
	plt.plot(np.linspace(sp-ep,ep-sp,1000),original)
	sum=np.ones(1000)*a0/2.0
	for num,coefficient in enumerate(coslist):
		sum+=coefficient*np.cos(2.0*math.pi*num*np.linspace(sp-ep,ep-sp,1000)/(ep-sp))
	for num,coefficient in enumerate(sinlist):
		sum+=coefficient*np.sin(2.0*math.pi*num*np.linspace(sp-ep,ep-sp,1000)/(ep-sp))
	plt.plot(np.linspace(sp-ep,ep-sp,1000),sum)
	#plt.axis([sp-ep,ep-sp, 1.2*min(original), 1.2*max(original)])
	plt.savefig("graph.jpg", dpi=400)
	print "Finished"

if __name__ == '__main__': 
	main()
