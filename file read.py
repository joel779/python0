##file=open("filename.txt","r")
##print("first line:")
##print(file.readline())
##print("Second line:")
##print(file.readline())
##print("rest of file:")
##print(file.read())
##print("blank line:")
##print(file.readline())
##file.close()
##
##file=open("filename.txt","r")
##print("first line:")
##print(file.readline())
##file.seek(0)
##print("first line again:")
##print(file.readline())
##file.seek(25,0)
##print("from the 25th character...")
##print(file.read())
##file.close()
##
##file=open("teams2.txt","r")
##print("First line:")
##print(file.readline())
##print("Second line:")
##print(file.readline())
##print("Rest of the teams:")
##print(file.read())
##file.close()

##file=open("teams2.txt","r") ##
##file.readline()
##file.readline()
##print("Third team: ")
##print(file.readline())
##file.seek(0)
##file.readline()
##file.readline()
##print("Third team:")
##print(file.readline())
##file.close()

##file=open("teams2.txt","r")##select character 
##file.readline()
##file.readline()
##file.read(5)
##print("Second character: ")
##print(file.read(2))
##file.close()

##file=open("teams2.txt","r")
##edit=""
##file.readline()
##edit=edit+file.readline()
##file=open("teams2.txt","w")
##file.write(edit)
##file.close()
##
##file=open("teams2.txt","a")
##newline= "Blackburn \n"
##file.write(newline)
##newline="Man City \n"
##file.write(newline)
##file.close()

f=open("teams2.txt","r")
lines=f.readlines()
f.close()
f=open("teams2.txt","w")
for line in lines:
    if line!="Burnley"+"\n":
        f.write(line)
f.close()


