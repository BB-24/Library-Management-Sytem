import pickle
import sys

def create():
    print("TO CREATE A NEW FILE.....")
    print(" ")
    o=open("data.dat","wb")
    c=input("To enter records enter 'y':")
    rec=[]
    while c=="y" or c=="Y":
        print("_"*78)
        a=int(input("Enter Book number:"))
        b=input("Enter Book's name:")
        c=input("Enter Status:")
        d=input("Enter Borrower's name:")
        print("_"*78)
        r=[a,b,c,d]
        rec.append(r)
        c=input("Enter 'y' to add more records:")
    pickle.dump(rec,o)
    o.close()
    

def display():
    print("TO SEE THE ENTIRE DATA.....")
    o=open("data.dat","rb")
    f=pickle.load(o)
    print("[Book's number , Book's name , Status , Borrower's name]")
    print("_"*78)
    for i in f:
        print(i)
    o.close()
    print("_"*78)

def display_borrowers():
    print("TO SEE THE BORROWER'S NAME LIST.....")
    o=open("data.dat","rb")
    print("BORROWER'S NAME")
    print("_"*78)
    f=pickle.load(o)
    for i in f:
        if i[3]!="-":
            print(i[3])
    o.close()
    print("_"*78)
    
def search():
    print("TO SEARCH THROUGH DATA.....")
    c=int(input("Enter the Book's number:"))
    o=open("data.dat","rb")
    print("_"*78)
    f=pickle.load(o)
    r=0
    for i in f:
        if c==i[0]:
            r=1
            print(" ")
            print("Book number:",i[0])
            print("Book's name:",i[1])
            print("Status:",i[2])
            print("Borrower's name:",i[3])
    if r==0:
        print("RECORD NOT FOUND")
    o.close()
    print("_"*78)
    


def append():
    print("TO ADD MORE RECORDS....")
    o=open("data.dat","rb")
    rec=pickle.load(o)
    o.close() 
    f=open("data.dat","wb")
    
    c=input("To enter records enter 'y':")
    while c=="y" or c=="Y":
        print("_"*78)
        a=int(input("Enter Book number:"))
        b=input("Enter Book's name:")
        c=input("Enter Status:")
        d=input("Enter Borrower's name:")
        print("_"*78)
        r=[a,b,c,d]
        rec.append(r)
        c=input("Enter 'y' to add more records:")
    pickle.dump(rec,f)
    f.close()
    


def delete():
    print("TO DELETE A RECORD.....")
    n=int(input("Enter the Book's number:"))
    o=open("data.dat","rb+")
    rec=[]
    stu=pickle.load(o)
    y=0
    for i in stu:
        s=i[0]
        if s!=n:
            rec.append(i)
            y=1
        if y==0:
            print("record not found")
    o.seek(0)
    pickle.dump(rec,o)
    o.close()
    

def update():
    print("TO BORROW/RETURN A BOOK.....")
    f=open("data.dat","rb+")
    rec=pickle.load(f)
    y=0
    n=int(input("Enter the Book's number:"))
    for i in rec:
        s=i[0]
        if s==n:
            print("RECORD FOUND")
            i[2]=input("update status:")
            i[3]=input("update borrower's name:")
            y=1
            print("RECORD UPDATED")
    if y==0:
        print("RECORD NOT FOUND")
    f.seek(0)
    pickle.dump(rec,f)
    f.close()
    
                


print("_"*78)
print(" ")
print(" ")
print("~"*15,"WELCOME TO LIBRARY MANAGEMENT SYSTEM","~"*15)
print(" ")
print(" ")
print("_"*78)
print(" ")
print(" ")
print("ENTER 1 TO CREATE A NEW FILE")
print(" ")
print("ENTER 2 TO DISPLAY ALL THE REACORDS")
print(" ")
print("ENTER 3 TO ADD NEW RECORDS")
print(" ")
print("ENTER 4 TO SEARCH A RECORD")
print(" ")
print("ENTER 5 TO BORROW/RETURN A BOOK")
print(" ")
print("ENTER 6 TO DELETE A RECORD")
print(" ")
print("ENTER 7 TO DISPLAY THE BORROWER'S LIST")
print(" ")
print("ENTER 8 TO EXIT THE SOFTWARE")
print(" ")
print("_"*78)

ch=int(input("Enter choice:"))
print(" ")
print("_"*78)


if ch<=7:
    while ch<=7:
        if  ch==1:
            print("Creating a new file will erase all your previous data")
            c=input("To affirm your choice enter 'y':")
            if c=="y" or c=="Y":
                create()
                
            else:
                break
        elif ch==2:
            display()
            
        elif ch==3:
            append()
            
        elif ch==4:
            search()
           
        elif ch==5:
            update()
            
        elif ch==6:
            delete()
            
        else:
            display_borrowers()
            
        print(" ")
        print("ENTER 1 TO CREATE A NEW FILE")
        print(" ")
        print("ENTER 2 TO DISPLAY ALL THE RECORDS")
        print(" ")
        print("ENTER 3 TO ADD NEW RECORDS")
        print(" ")
        print("ENTER 4 TO SEARCH A RECORD")
        print(" ")
        print("ENTER 5 TO BORROW/RETURN A BOOK")
        print(" ")
        print("ENTER 6 TO DELETE A RECORD")
        print(" ")
        print("ENTER 7 TO DISPLAY THE BORROWER'S LIST")
        print(" ")
        print("ENTER 8 TO EXIT THE SOFTWARE")
        print(" ")
        print("_"*78)
        ch=int(input("Enter choice:"))
else:
    sys.exit()
print("END")