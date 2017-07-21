#import itertools
import random


    
print ("                                    WELCOME TO NIM GAME......!!! \n INSTRUCTIONS :\n Each player needs to select one pile and pick up some number of objects .")
print(" Player who picks up the last object from all piles wins the game \n")

n1 = random.randint(1,31)
n2 = random.randint(1,31)
n3 = random.randint(1,31)
fill1 = 0 
fill2 = 0 
c1 = 0
c2 = 0 
c3 = 0
chance = 0

print("Number of objects in pile 1 ", n1)
print("Number of objects in pile 2 " ,n2)
print("Number of objects in pile 3 " ,n3)


def foo(a1, a2, a3):

 p1 = list(map(int,list(str(bin(a1)))[2:]))
 p2 = list(map(int,list(str(bin(a2)))[2:]))
 p3 = list(map(int,list(str(bin(a3)))[2:]))
#print(p1)
#print(p2)
#print(p3)

 def checklen(l,p):
    
   if(not l == 5):
      for i in range (0,5-l):
         p.insert(0,0)

 checklen(len(p1),p1)
 checklen(len(p2),p2)
 checklen(len(p3),p3)
 #print(p1)
 #print(p2)
 #print(p3)


 
    
 sumofd =[]
 sum1 =[]
 check = True
 pick = -1
        
 for i in range (0,5):
            sumofd.append(p1[i]+p2[i]+p3[i]);
            if not sumofd[i]%2 == 0:
                if(p1[i] == 1 and check):
                 p1[i] = 0
                 pick = 1
                 check = False
                elif(p2[i] == 1 and check):
                 p2[i] = 0
                 pick= 2
                 check = False
                elif(p3[i] == 1 and check):
                 p3[i] = 0
                 check = False
                elif(pick ==1):
                 if(sumofd[i] == 3):
                    p1[i] = 0 
                 elif(p1[i] == 1):
                    p1[i] = 0
                 else :
                    p1[i] = 1
                elif(pick ==2):
                 if(sumofd[i] == 3):
                    p2[i] = 0 
                 elif(p2[i] == 1):
                    p2[i] = 0
                 else :
                    p2[i] = 1
                else:
                 if(sumofd[i] == 3):
                    p3[i] = 0 
                 elif(p3[i] == 1):
                    p3[i] = 0
                 else :
                    p3[i] = 1
                    
            sum1.append(p1[i]+p2[i]+p3[i])    
                    
                
                
                
                
 #print(sumofd)
 print("\n")
 #print(p1)
 #print(p2)
 #print(p3)
 #print(sum1)        
                
        #remove
    
 if pick == 1:
        global n1
        remove = int("".join(map(str,p1)),2)
        print("the computer removes ",(n1-remove),"objects from pile 1\n")
        n1 = remove
        
 elif pick == 2:
        global n2
        remove = int("".join(map(str,p2)),2)
        print("the computer removes ",(n2-remove),"objects from pile 2\n")
        n2 = remove
        
 else :
        global n3
        remove = int("".join(map(str,p3)),2)
        print("the computer removes ",(n3-remove),"objects from pile 3\n")
        n3 = remove  
        
 print("Number of objects in pile 1 :",n1)    
 print("Number of objects in pile 2 :",n2)    
 print("Number of objects in pile 3 :",n3)
 print(" ") 
             
 return n1 ,n2 ,n3 
 
                             
def user( b1 , b2 , b3 ):   
 a = int(input("Enter the pile :"))
 
 b = int(input("Enter number of objects  to be removed :"))
 
# print(a)
 #print(type(a))
 global n1 
 global n2 
 global n3
 
 if (a == 1 ):
    if(n1 != 0 and b <= n1):
        n1= n1-b
        print("You removed ",b,"objects from pile 1")
        print(" ")
    else : 
        print ("The pile is empty....choose another pile...!!")
        user(n1 , n2 , n3)
        
 elif (a == 2 ):
     if(n2 != 0 and b <= n2):
        n2= n2-b
        print("You removed ",b,"objects from pile 2")
        print(" ")
     else :
         print("The pile is empty....choose another pile...!! ")
         user(n1 , n2 , n3)
       
 elif (a == 3):
     if(n3 != 0 and b <= n3):
        n3 = n3 - b
        print("You removed ",b,"objects from pile 3")
        print(" ")
     else :
         print ("The pile is empty....choose another pile...!! ")
         user(n1 , n2 , n3 )
 else :
        print("Invalid input..! Select from the 3 piles..!")
    
 print("Number of objects in pile 1 :",n1)    
 print("Number of objects in pile 2 :",n2)    
 print("Number of objects in pile 3 :",n3)
 print(" ")
      
 return n1,n2,n3      
 
 

def second(a1 , a2 , a3):
 
  global n1 
  global n2 
  global n3
  
  global chance
  global fill1
  global fill2
  #print("In second part of the game ")
  a = int(input("enter the pile :"))
  if(a ==1):
   if(n1 == n2):
        fill1 = 1
        fill2 = 2
        
   elif(n1 == n3):
        fill1 = 1
        fill2 = 3
        
        
  if(a ==2):
   if(n2 == n1):
        fill1 = 2
        fill2 = 1
      
        
   elif(n2 == n3):
        fill1 = 2
        fill2 = 3
        
        
  if(a ==3):
   if(n3 == n1):
        fill1 = 3
        fill2 = 1
   elif(n3 == n2):
        fill1 = 3
        fill2 = 2

    
  b = int(input("enter number of objects  to be removed :"))
  
 
  if (a == 1):
    if(n1 != 0 and b <= n1):
        n1= n1-b
        print("You removed ",b,"objects from pile 1")
        print(" ")
        
    else : 
        print ("The pile is empty....choose another pile...!!")
        #second(n1 , n2 , n3)
        
        
  elif (a == 2):
     if(n2 != 0 and b <= n2):
        n2= n2-b
        print("You removed ",b,"objects from pile 2")
        print(" ")
        
     else :
         print("The pile is empty....choose another pile...!!")
         #second(n1 , n2 , n3)
         
       
  elif (a == 3):
     if(n3 != 0 and b <= n3):
        n3 = n3 - b
        print("You removed ",b,"objects from pile 3")
        print(" ")
     else :
         print ("The pile is empty....choose another pile...!!")
         #second(n1 , n2 , n3 )
         
  else :
        print("invalid input")
    
  print("Number of objects in pile 1 :",n1)    
  print("Number of objects in pile 2 :",n2)    
  print("Number of objects in pile 3 :",n3)
  print(" ")
  

  if(a ==1):
    if (fill2 == 2 and b<= n2):
      print("the computer removes ",b,"objects from pile 2")
      n2 = n2 - b 
    elif(fill2 ==3 and b<=n3):
      print("the computer removes ",b,"objects from pile 3")
      n3 = n3 - b
      
  if(a ==2):
   if (fill2 == 1 and b<=n1):
      print("the computer removes ",b,"objects from pile 1")
      n1 = n1 - b
   elif(fill2 ==3 and b <=n3):
      print("the computer removes ",b,"objects from pile 3")
      n3 = n3 - b
      
  if(a == 3):
   if (fill2 == 1 and b <= n1):
      print("the computer removes ",b,"objects from pile 1")
      n1 = n1 - b
   elif(fill2 ==2 and b <=n2):
      print("the computer removes ",b,"objects from pile 2")
      n2 = n2 - b
    
  print("Number of objects in pile 1 :",n1)    
  print("Number of objects in pile 2 :",n2)    
  print("Number of objects in pile 3 :",n3)
  print(" ")
  
  return n1, n2 , n3 
 
 
   
 
 
    
def cond(n1 , n2 , n3):
    if(n1 == n2 and n3 == 0 ):
        return False
    elif(n1 == n3 and n2 == 0 ):
        return False
    elif(n2 == n3 and n1 == 0 ):
        return False
    elif(n1 == n2 == n3 == 0):
        return False
    else : return True
    
    
def wincond (n1 , n2 , n3):
    if(n1 ==0 and n2 == 0 and n3 ==0 ):
      print(" ")
      print("You lost the game :(......!!! ")
      return False
    else:
        return True
    

while(cond(n1 ,n2 ,n3)):
  foo(n1 , n2 , n3)
  if(cond(n1 ,n2 ,n3)): 
    user(n1 ,n2 ,n3) 
  else :   chance = 1
  
  

    
    
while(not(cond(n1 , n2 , n3)) and wincond(n1 , n2 , n3)):
  
       #print("in while looop")
       if (chance == 1):
       # print("i am in one")
        second(n1 , n2 , n3)
          
       elif(chance == 0):
       # print(" i am in two ")
        foo(n1 ,n2 , n3)
        user(n1 , n2 , n3)
        
       #else : second(n1 , n2 , n3)
 
    
 
 
 
 
 
 
 
 