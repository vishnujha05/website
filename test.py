'''a=int(input("enter no."))
#b=int(input("enter no."))
if a>75 :
    print("a is greter than 75",a)
elif a>= 60 & a<75 :
        print("a llies btweeen 60 to 75",a)
elif a>= 50 & a<60 :
        print("a llies btweeen 50 to 60",a)

elif a>= 40 & a<50 :
        print("a llies btweeen 40 to 50",a)

else:
    print("a is less than 40",a)'''


'''if a%2 ==0:
    print("a is even no.",a)
else:
    print('a is odd no.',b)
if a>b :
   print("a is greater than b by :",a-b)
else:
   print("b is greater than a by :",b-a)
    
temp=a
a=b
b=temp
print("a and b is =",a,b) '''
#args&kwags
'''def name (name,age,**adrs):
    print(name)
    print(age)
    for i in  adrs:
    print((i))'''

'''lst=[2,4,6,7,]
kwags={'vishnu':'boy','sivangi':"girl","vishnu":"pizza","ram":"aam"}
#lst2=list(map(lambda x:x*x ,lst))
lst2=2
name(lst2,"vishnu",**kwags)
for i,j in kwags.items():
    print(i,":",j)'''
#enumerate
lst=['2','4',6,8,9]
for index,value in enumerate(lst):
    if index != 2:
       print(value,end="  ") 
       print(index)
       #random module
'''import random as rd   
lst=[1,2,3,4,5,6]
lst=list(map(lambda x: x*2 ,lst))
choice=rd.choice(lst)
print(choice)
num=rd.random(0,15)
print(num)'''
#game---->>>> [snake,water,gun]------------
'''num=10
us=0
com=0
draw=0
while(num>0):
    import random as rd
    game=["water","snake","gun"]
    print("plz select any one of three by there index")
    for index,value in enumerate(game):
        print(index,":",end=' ')
        print(value)
    i=int(input("plz select from above index cartain:"))
    print("you are selected :",game[i])
    comp=rd.choice(game)
    if i==0:
        if comp==game[0]:
            print("computer choice is:"+str(comp))
            print("oho draw this time plz try again...")  
            draw+=1
        elif comp== game[1]:
            print("computer choice is:"+str(comp))
            print("oho you lose plz try again...")
            com=com+1
        elif comp== game[2]:
            print("computer choice is:"+str(comp))
            print("congratulation you won")
            us+=1
    elif i==1:
        if comp==game[0]:
            print("computer choice is:"+str(comp))
            print("congratulation you won")
            us+=1
           
        elif comp== game[1]:
            print("computer choice is:"+str(comp))
            print("oho draw this time plz try again...")
            draw+=1
            
        elif comp== game[2]:
            print("computer choice is:"+str(comp))
            print("lose this time plzz try again")
            com+=1 
    elif i==2:
        if comp==game[0]:
            print("computer choice is:"+str(comp))
            print("oho you lose this time plz try again")
            com+=1
           
        elif comp== game[1]:
            print("computer choice is:"+str(comp)) 
            print("congratulation you won this time ")
            us+=1
        elif comp== game[2]:
            print("computer choice is:"+str(comp))
            print("oho draw this time ")
            draw+=1
    else:
        print("plz select any from index")  

    print("score of user is :"+str(us))
    print("score of computer is :"+str(com))
    print("draw game:"+str(draw))
    num-=1
    print("total tail left:"+str(num)+"out of 10")'''

