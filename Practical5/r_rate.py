# This step sets up the basic data
n=84
r=1.1
# The following steps use loop to repeat calculationg 5 times.
m=0
while m<5:
 a=n+n*r
 n=a
 m=m+1
print(a)
