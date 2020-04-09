''''try:

print("there r 9 move trial only to know the valid no. can assumed")
count = 0
for i in range (0,9):
    trial = int(input("try you best"))
    if(trial>100):
        print("congrat! you r your assumption is grater then 100")
        count = 1+count
        break
    else:
        print("oho you r worng attempt! please try again sir")
        count = 1+count
        continue
print("your best attemp is :"+str(count))
ch = int(input("do you want to continue for press 1"))
}while ch==1 :
except Exception as e :
    print(e)
print("this is important")'''
'''try:
print("hi i am vishnu jha your frand")
#except Exception as e :
   # print(e)

print("hi")'''
'''matrix = [[2,4,5],
          [5,6,0],
           [15,56,7]]
print("your first matrix is :")
for  i in  matrix :
   print(i)
matrix2 = [[3,5,7],
           [7,5,34],
           [67,65,76]]
print("your secound matrix is :")
for i in matrix2 :
    print(i)

result = [[0,0,0],  
          [0,0,0],
          [0,0,0]]
for i in range (len(matrix)) :
     for j in range (len(matrix2)) :
         for k in range (len(matrix2)) :
             result[i][j]+=matrix[i][k]*matrix2[k][j]
print("your multipicatoin of two matrix is :")
for i in result :
    print(i)'''
    #matrix prograram

'''mat = []
mat2 = []
result = [[0,0,0], 
          [0,0,0],
          [0,0,0]]
n=3
m=3
for i in range (0,n):
 mat.append([])
print(mat)
for i in range(0,n):
    for j in range (0,m):
        mat[i].append(j)
        mat[i][j]=0
for i in range(0,n):
    for j in range(0,m):
        print("matrix["+str(i+1)+"]["+str(j+1)+"] :")
        mat[i] [j] = int(input())

print(mat)
for i in range (0,n):
    mat2.append([])
for i in range(0,n):
    for j in range (0,m):
        mat2[i].append(j)
        mat2[i][j]=0
for i in range(0,n):
    for j in range(0,m):
        print("matrix2["+str(i+1)+"]["+str(j+1)+"] :")
        mat2[i] [j] = int(input())
for i in range (len(mat)):
    for j in range (len(mat2)):
        for k in range (len(mat2)):
            result[i][j]+=mat[i][k]*mat2[k][j]
print(mat2)
print("multipiication of two matrix is :" )
for i in result :
    print(i)'''

#print(mat2)
'''def fact (n):
    if n==1:
        return 1
    else :
        return n * fact(n-1)
num= int(input("enter no. for factorial :"))
result=fact(num)
print(result)  '''
'''def febnoic (n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else :
        return febnoic(n-2) + febnoic(n-1)
        
num= int(input("enter no. for fabnoiic series :"))
result=febnoic(num)
print(result) '''

#lamda funtion
'''add = lambda x,y : x+y
print(add(9,6))''' 
student={}
numn =int(input())
for i in range(numn):
    print(i)