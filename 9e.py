f=open("C:\24FFMCA048\python\demo.txt","r")
data=f.read()
lw=data.split()
d={}
for word in lw:
    if word not in d:
        d[word]=1
    else:
        d[word]=d[word]+1
print(d)        
