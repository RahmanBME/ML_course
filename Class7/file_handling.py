#open function is used to open a file
#how read a file."r" - Read - Default value. Opens a file for reading, error if the file does not exist
y=open("text.text",'r')
print(y.read())

y=open("index.html",'r')
print(y.read())

#"a" - Append - Opens a file for appending, creates the file if it does not exist
y=open("text.text",'a')
print(y.write(" my home district is naogaon, sapahar to be more exact"))

#"w" - Write - Opens a file for writing, creates the file if it does not exist
y=open("text.text",'w')
print(y.write(" my home district is naogaon, sapahar to be more exact"))


#creation of a file."x" - Create - Creates the specified file, returns an error if the file exists

f = open("myfile.txt", "x")



