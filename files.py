'''import sys
f=open("text.txt",'a')
item=f.write("the text by vishnu.\n")
r=f.read()
print(r)
# print(item)
f.close()'''
n=int(input())
for i in range(1,n):
    c=char(i)
    print(c*i,end="")