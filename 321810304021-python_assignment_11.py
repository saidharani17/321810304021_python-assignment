#1.to sum all elements in list
sum = 0
list = [5,6,7,72,89]
for ele in list: 
    sum = sum+ ele
print("Sum of all elements in given list: ", sum) 
##2.tomultiply all elements
product=1
list=[3,5,4,6]
for i in list:
	product=product*i
print("multiplication of items in a list:",product)
##3.max and min from list
list=[34,5,6,12,78]
a=max(list)
b=min(list)
print("max number in a list:",a)
print("min number in a list:",b)
##4.remove duplicates from list
a = [10,20,30,20,10,50,60,40,80,50,40]
dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
print(dup_items)
##5.to check list is empty or not
list=input("enter elements of a list:")
for i in list:
	if i==0:
		print("list is empty")
	else:
		print("list is not empty")

##6.to copy a list
oldlist=[1,2,3,4,5]
newlist=oldlist
print("oldlist:",oldlist)
print("newlist:",newlist)
##7.to remove 0th and 4thelement
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4)]
print(color)

##8to remove elments in even
list = [4,5,6,7,8,1,2,3]
print("Original list:",list)
for i  in list:
	if(i%2 == 0):
	    list.remove(i)
print ("list after removing EVEN numbers:",list)
##9program to shuffle and print specified list:

import random 
list= [1, 4, 5, 6, 3]
print ("The original list is : ",list) 
random.shuffle(list) 
print ("The shuffled list is : " ,list) 

##10
##8to remove elments in even
list = [4,5,6,7,8,1,2,3]
print("Original list:",list)
for i  in list:
	if(i%2 == 0):
	    list.remove(i)
print ("list after removing EVEN numbers:",list)
##program to shuffle and print specified list:

import random 
list= [1, 4, 5, 6, 3]
print ("The original list is : ",list) 
random.shuffle(list) 
print ("The shuffled list is : " ,list) 
##difference in elements in a list
list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 30, 60, 70]
print ("List1:", list1)
print("List2:", list2)
print("Difference elements:")
print ((set(list1) - set (list2)) )
