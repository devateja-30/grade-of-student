#program to print grade obtained by a student
math=eval(input("enter marks obtained in maths"))
chem=eval(input("enter marks obtained in chemistry"))
phy=eval(input("enter marks obtained in physics"))
ph=eval(input("enter marks obtained in python"))
eng=eval(input("enter marks obtained in english"))
p=((math+chem+phy+ph+eng)/500)*100
print("total percentage obtained by the student=",p)
if(p>=90):
 print("you got 'A+' grade")
if((p>=80) and (p<90)):
 print("you got 'A' grade")
if((p>=70) and (p<80)):
 print("you got 'B' grade")
if((p>=60) and (p<70)):
 print("you got 'C' grade")
if((p>=50) and (p<60)):
 print("you got 'D' grade")
if(p<50):
 print("you failed")
