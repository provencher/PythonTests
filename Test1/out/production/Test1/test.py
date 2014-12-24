
#Variables
f = 0;

# Basic Function
def fun1():
   print("I AM FUNCTION");


# Basic fibonacci - recursion
def fib(n):
    if (n>1):
        return (fib(n-1) + fib(n-2));
    else:
        return n;

# For Loops
for x in range (1,10):
    print (fib(x));


# While loops
#x = 1;
#while (x<10):
 #  x = x + 1;