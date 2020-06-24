# 1.Generate first N number of Fibonacci numbers.Take N value from user

n=int(input("Enter the value of n:"))
num1=0
num2=1
sum=0
count=1
print("Fibonacci Series:",end=" ")
while(count<=n):
    print(sum,end=" ")
    count+=1
    num1=num2
    num2=sum
    sum=num1+num2


# 2.Display multiplication table of K.Take k value from user

K=int(input("Display multiplication table of? "))
for i in range(1,11):
    print(K,'x',i,'=',K*i)


# 3.Write a program to find greatest common divisor(GCD) or highest common factor(HCF) of given two numbers.

def gcd(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if((x%i==0) and (y%i==0)):
            gcd=i
    return gcd
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print("The G.C.D of",num1,"and",num2,"is",gcd(num1,num2))


# 4.Write a python program to count the number of even and odd numbers from a series of numbers

list=[1,2,3,4,5,6,7]
even_count,odd_count=0,0
for num in list:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print("Even numbers in the list:",even_count)
print("odd numbers in the list:",odd_count)


# 5.Write a program that prints all the numbers from 0 to 6 except 3 and 6

for x in range(6):
    if (x==3 or x==6):
        continue
    print(x,end=' ')
print("\n")