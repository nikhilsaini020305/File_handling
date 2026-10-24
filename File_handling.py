from pathlib import Path
import os
def readfileandfolder():
   path = Path(".")

   items = list(path.rglob("*"))
   for i,item in enumerate(items):
        print(f"{i+1}:{item}")
        
def createfile():
    try:
        readfileandfolder()
        name=input("Please tell your file name :- ")
        p=Path(name)
        if not p.exists():
            with open(p,"w")as fs:
                data=input("What you want to write in this file :- ")
                fs.write(data)
            print("File Created Successful")
        else:
            print("File Created Successfully")
    except Exception as err:
        print(f"An error occured as {err}")

def readfile():
    try:
        readfileandfolder()
        name=input("Please tell your file name :- ")
        p=Path(name)
        if p.exists() and p.is_file:
            with open(p,'r')as fs:
                data=fs.read()
                print(data) 
            print("Read successfully")
        else:
            print("the file doesnot exist")
    except Exception as err:
        print(f"An error occured as {err}")

def updatefile():
    try:
        readfileandfolder()
        name=input("tell which file you want to update :- ")
        p=Path(name)
        if p.exists()and p.is_file:
            print("Press 1 for changing the name for your file :- ")
            print("Press 2 for overwritng the data for your file :- ")
            print("Press 3 for appending some content in your file :- ")
            res=int(input("Tell your response :-"))
            if res==1:
                name2=input("Tell your new file name :- ")
                p2=Path(name2)
                p.rename(p2)
            if res==2:
                with open(p,'w')as fs:
                    data=input("Tell what you want to write this is over the data")
                    fs.write(data)
            if res==3:
                with open (p,'a')as fs:
                    data=input('tell what you want to append :- ')
                    fs.write(""+data)
    except Exception as err:
        print(f"An error occured as {err}")

def deletfile():
    try:
        readfileandfolder()
        name=input("which file you want to delete :- ")
        p=Path(name)
        if p.exists()and p.is_file():
            os.remove(name)
            print("File remove successfully")
        else:
            print("No such file exist")
    except Exception as err:
        print(f"An error occured as {err}")
    

print("Press 1 for Creating a file ")
print("Press 2 for Reading a file ")
print("Press 3 for Updating a file ")
print("Press 4 for Deletion a file ")

check=int(input("Please tell your response :- "))
if check==1:
    createfile()
if check==2:
    readfile()
if check==3:
    updatefile()
if check==4:
    deletfile()