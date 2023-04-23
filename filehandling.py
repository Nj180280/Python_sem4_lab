'''#read file 
f=open("demofile.txt","rt")
# print(f.read())
# print(f.readline())
print(f.read(5))
f.close() 

#write file
f=open("demofile.txt","w")
f.write("this is more content added")
f.close() 
f=open("demofile.txt","rt")
print(f.read())
f.close() 
#create file
f=open("myfile.txt","x")
f.close()

#delete file 
import os 
if os.path.exists("myfile.txt"): 
    os.remove("myfile.txt")
else:
    print("file not found")
#to delete folder 
#os.rmdir("foldername")'''