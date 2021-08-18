with open("file1.txt", "r+") as myfile:
    print (myfile.read())
    myfile.write("I am fine. ")
myfile.close()

