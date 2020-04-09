# program 4.37 page-161
#1+1/2+1/3+......+1/n
n=int(input("enter no. of sequence"))
s=0
i=1
while(i<=n):
#for i in range (0,n+1,2):
    a= (i**2)
    s+=a
print("1+1/2+1/3+......+1/n wher n is-" + str(n) + " :" , s)
'''str_day=int(input("enter the day of moths(1-7) : "))
noday=int(input("enter total day in month"))
print("sun mon tues wed thurs fri sat")
print("---------------------------------------------------")
for i in range (str_day-1):
    print(end="     ")
i=str_day-1
for j in range(1,noday+1):
    if(i>6):
        print(" ")
        i=1
    else:
        i+=1
    print(str(j) +"   " , end=" ")'''
