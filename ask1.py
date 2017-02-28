import math
a=raw_input("dwse mia lista me  5 toulaxiston thetikous akeraious")
a=eval(a)
a.remove(max(a))
a.remove(min(a))
a.remove(max(a))
a.remove(min(a))
def mo(b):
	mhkos=len(b)
	sum1=sum(b)
	mo=sum1*1.0/mhkos
	return mo
c=mo(a)	
def tuapok(b):
    mhkos1=len(b)
    sum2=0
    mo1=mo(b)
    for i in range(mhkos1):
    	sum2 +=(b[i]-mo1)**2
    ta=sum2*1.0/mhkos1
    return math.sqrt(ta)
result=tuapok(a) 
print(result)






	
		


