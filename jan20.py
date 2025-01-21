import os
import shutil

#create a new directory
if not os.path.isdir("test_directory"):
        os.mkdir("test_directory")

#change the current working directory to the new directory
os.chdir("test_directory")        
print("current working directory:", os.getcwd())

#create a text file in the directory
with open ("example.txt","w" )as file:
        file.write("this is  atest file")

#list files in the current directory
print("files in directory:", os.listdir)

#copy the file
shutil.copy("example.txt","copy_example.txt")

#move the copied file to a new location(remaining it in the process
shutil.move("copy_example.txt", "../moved_example.txt")

#go back to the parent directory
os.chdir("..")

#remove the test directory and its contents
shutil.rmtree("test_directory")
os.remove("moved_example.txt") #remove the moved file
print("cleanup complete!!")
                
        