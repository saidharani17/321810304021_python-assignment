#1.Program to read an entire text file

file= open("myfile.txt","w") 
L = ["Mango\n","Apple\n","Banana \n"]  
file.write("Fruits\n") 
file.writelines(L) 
file.close() 
file = open("myfile.txt","r")  
print("Output of Read function is ")
print (file.read())
	

#2.program to read first n lines of a file

def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
file_read_from_head('test.txt',2)

#3.Program to append text to a file and display the text

file=open('myfile2.txt','w')
L2=["Hi\n","Hello\n","Gitam\n"]
file.writelines(L2)
file.close()
file=open('myfile2.txt','r')
print('Before appending the text:')
print(file.read())
file=open('myfile2.txt','a')
file.write('Good morning')
file.close()
file=open('myfile2.txt','r')
print('After appending the text:')
print(file.read())


#4.program to read last n lines of a file

def LastNLines(f,n)
with open(f) as file:
	print('Last' ,n,"lines from file:",f)
	for line in(file.read lines( ) [-n:]):
		print(line, end=' ')
		name= input("enter the file name:")
		n=int(input("no of last lines to read:"))
		try:
			LastNLines(name,n)
        except:
        	print("file error.....")
        	
        	
#5.program to read a file line by line store it into a variable

def file_read(fname):
        with open (fname, "r") as myfile:
                data=myfile.readlines()
                print(data)
file_read('test.txt')


#6.program to read a file line by line to store it into a list

def file_read(fname):
        with open(fname) as f:
                #Content_list is the list that contains the read lines.     
                content_list = f.readlines()
                print(content_list)

file_read(\'test.txt\')
