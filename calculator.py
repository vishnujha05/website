
'''print("----------------------calculator---------------------------")
def addition(a,b):
    a+=b
    print("addtion of two no. is :",a)
def substraction(a,b):
    a-=b
    print("substraction :",a)
def multipication (a,b):
    a*=b
    print("multipication :", a)

def division(a,b):
    a//=b
    print("division :", a)
def modulo(a,b):
    a%=b
    print("remainder :", a)
def sq(a,b):
    a**=2
    print("square:"+ str(a),a)
    

def sqrt(a,b):
    math.sqrt(a)
    print("square root of a:"+ str(a), a)
    

print("enter your opperation :")
print("/n /t1.addition /n/t2.substration/n/t3.multipication/n/t")
ch=int(input("select your opr:"))
'''switch (ch)
 case 1 : #additon
 a= float(input("enter two no. for addition:"))
 b= float(input("enter two no. for addition:"))
 addition(a,b)
 break
  default :print("worng input")'''
 # ch= int(input("enter y"))
  cal = {
      1 : addition ,
      2 : substraction,
      3 : multipication

  }
  cal.get(ch)'''
  def switch ():{
      a=int(input("enter first no."))
      b= int(input("enter second no."))
      ch = int (input("select your operation"))
      def add ():
          result = a+b
          print(str(a)+"+" + str(b) , result)

      dict = {
          1 : add ,
          2 : mul 
      }
      dect.get(ch) ()
  }

   
    