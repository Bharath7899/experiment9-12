f=open("C:\24FFMCA048\python\demo.txt","r")
print("The filepointer is at byte:",f.tell())
content=f.read();
print("After reading the filepointer is at:",f.tell())
