# 1.Generate first N number of Fibonacci numbers.Take N value from user.

n=int(input("Enter the number:"))
def printFibonacciNumbers(n):
    f1=0
    f2=1
    if(n<1):
        return
    for x in range(0,n):
        print(f2,end=" ")
        next=f1+f2
        f1=f2
        f2=next
printFibonacciNumbers(n)


# 2.Take 10 integers from keyboard using loop and print average value on screen.

n=input("enter any numbers:")
num=n.split()
print("\n")
print("enter all numbers",num)
sum=0
for i in num:
    sum+=int(i)
print("sum of numbers",sum)
avg=sum/len(num)
print(avg)


# 3.Print the following patterns using loop

def star(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print("\r")
n=4
star(n)


# 4.Write a program to find the length of the string "refrigerator" without using len() function.

a="refrigerator"
count=0
for i in a:
    count=count+1
print(count)


# 5.Write a python program to count the number of characters in a string.

def char_frequency(str1):
    dict={}
    for n in str1:
        keys=dict.keys()
        if n in keys:
            dict[n]+=1
        else:
            dict[n]=1
    return dict
print(char_frequency('tejaswini'))   


#6.Write python script that takes input from the user and displays that input back in upper and lower cases.

user_input=input("Python?")
print("Python is:",user_input.upper())
print("Python is:",user_input.lower())


# 7.Write a python program to count occurrences of a substring in a string.

string="Python is awesome, isn't it?"
substring="is"
count=string.count(substring)
print("The count is:",count)
