# Write line to file
exmp2 = 'Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")
    

# Read file

with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())
    
with open(exmp2, 'w') as writefile :
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")
    writefile.write("This is line C")
    
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())
    
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
print(Lines)

with open(exmp2, 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)
        
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())
    
    
with open('Example2.txt', 'w') as writefile:
    writefile.write("Overwrite\n")
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
    
# Write a new line to text file

with open(exmp2, 'a') as testwritefile:
    testwritefile.write("\nThis is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")    
    
# Verify if the new line is in the text file

with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
    
    
with open('Example2.txt', 'a+') as testwritefile:
    testwritefile.write("This is line E\n") # Writing in the file
    print(testwritefile.read()) # Reading from the same file 
    
    

with open('Example2.txt', 'a+') as testwritefile:
    #print("Initial Location: {}".format(testwritefile.tell()))
    print(f"Initial Location: {testwritefile.tell()}")
    
    data = testwritefile.read()
    if (not data):  #empty strings return false in python
            print('Read nothing') 
    else: 
            print(data)
            
    testwritefile.seek(0,0) # move 0 bytes from beginning.
    
    print(f"\nNew Location : {testwritefile.tell()}")
    data = testwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print(f"Location after read: {testwritefile.tell()}" )


with open('Example2.txt', 'r+') as testwritefile:
    data = testwritefile.readlines()
    testwritefile.seek(0,0) #write at beginning of file
   
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("finished\n")
    #Uncomment the line below
    testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())
    
    
    
# Copy file to another

with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)
                
# Verify if the copy is successfully executed

with open('Example3.txt','r') as testwritefile:
    print(testwritefile.read())