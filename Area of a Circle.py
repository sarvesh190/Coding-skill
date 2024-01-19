def findArea(r):
    PI = 3.142
    return PI * (r*r);
 
print("Area is %.6f" % findArea(5));

9)Python Program to Find the Factorial of a Number
solu:-def factorial(n):
     
    return 1 if (n==1 or n==0) else n * factorial(n - 1) 

num = 5
print("Factorial of",num,"is",factorial(num))
