# This step determines the first 2 terms of the fibonacci sequence.
a=1
b=1
print(a)
print(b)
# This step means we're going from the third term to the thirteenth term.
n=3
while n<14:
# This step implements that each term is the sum of the previous two terms. 
 c=a+b
 print(c)
# These two steps could find the two terms before each term. 
 a=b
 b=c
 n=n+1


