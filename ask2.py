import itertools
def gin(x):
  c=1
  while(x>0):
    a=x%10
    c=c*a
    x=x/10
    return c
for i in itertools.count(1):
  if i % sum(int(b) for b in str(i))==0:
    if i<=1000:
      print i
    else:
     break
  m=gin(i)
  if m!=0:
   if i<=1000:
    if i%m==0:
     print i  
  