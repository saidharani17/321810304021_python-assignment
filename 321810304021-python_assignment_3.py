#  Take two number and check whether the sum is greater than 5,less than 5 or equal to 5


a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=a+b
if c>5:
    print("Sum is greater than 5")
elif c<5:
     print("Sum is less than 5")
else:
    print("Sum is equal to 5")
 
    
  # Take two inputs from user and check whether they are equal or not


str1=str(input("Enter the first string:"))
str2=str(input("Enter the second string:"))
if str1==str2:
    print("Yes Both strings are equal")
else:
    print("No Both strings are not equal")
    
    
  # Take three inputs from user and check:


str1=str(input("Enter first string:"))
str2=str(input("Enter second string:"))
str3=str(input("Enter third string:"))
if (str1==str2==str3):
    print("All Strings are equal")
elif (str1==str2 and (str1!=str3 or str2!=str3)):
    print("First and Second strings are equal")
elif (str1==str3 and (str1!=str2 or str3!=str2)):
    print("First and Third strings are equal")
elif (str2==str3 and (str2!=str1 or str3!=str1)):
    print("Second and Third strings are equal")
else:
     print("All strings are not equal")
     
     
  # Suppose passing marks of a subject is 35.Take input of marks from user and check whether it is greater than passing marks or not


marks=float(input("Enter marks of the student"))
if marks>=35:
    print("Student has passed in the subject")
else:
    print("Student has failed in the subject")
    
    
  # Write a python function to find max of three numbers

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a==b==c:
    print("All are equal..No Maximum number")
if (a>b and a>c):
    print("Maximum number is",a)
elif (b>c and b>a):
    print("Maximum number is",b)
else:
    print("Maximum number is",c)
