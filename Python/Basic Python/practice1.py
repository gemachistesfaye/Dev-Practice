print("hello")
print(1+2)
print(9-5)
print(((1 + 3) * (9 - 2) / 2) ** 2)
#b
ab =2+4
print(ab)
ab=100
print(ab)
ab=ab+80
print(ab)
#print(hours_per_day)
def main(input):
    output=input*5
    return output
new1=main(20)
new2=main(0)
print(new1)
print(new2)
integer=6 
y=10.1
print(integer)
print(type(integer))
float=12.1
print(float)
print(type(float))
round1=round(22/7,5)
print(round1)
round2=round(2.34567896573223352, 2)
print(round2)
boolean1=False
print(boolean1)
print(type(boolean1))
boolean2=True
print(boolean2)
print(type(boolean2))
boolean3=2>7
print(boolean3)
boolean4=2<7
print(boolean4)
boolean5=not boolean4
print(boolean5)
string1="Hello, I'm beginning learn Python"
print(string1)
print(type(string1))
print(len(string1))
string2="2"
print(string2)
print(type(string2))
string3="Gemachis" + "Tesfaye"
print(string3)
string4="Python " *5
print(string4)
print("      ")
print(4==4)
print(3>4)
print(3<4)
variable1=20
variable2=21
print(variable1==variable1)
print(variable1>variable2)
print(variable1<variable2)
print(variable1!=variable2)
print(variable1<=variable2)
print(variable1>=variable2)

print("      ")

## "if"  statemmnets
def result(res):
    message="Pass!🎉🎉"
    if res<50:
        message="Fail!⚡"
    return message
print(" Begin if statement")
print(result(90)) # print Pass!🎉🎉
print(result(44)) # print Fail!⚡
print(result(50)) # print Pass!🎉🎉

print("      ")

## "if....else" statements

def result1(res):
    if res>=50:
        mess="Pass!🎉🎉"
    else:
        mess="Fail!⚡"   
    return mess   
print(" Next is if...else statement")
print(result1(1))  # print Fail!⚡
print(result1(73)) # print Pass!🎉🎉

print("      ")


## "if ... elif ... else" statements

def grade(grd):
    if grd>=90:
        message="A+"
    elif grd>=85:
        message="A" 
    elif grd>=80:
        message="A-"  
    elif grd>=75:
        message="B+"     
    elif grd>=70:
        message="B"  
    elif grd>=65:
        message="B-"   
    elif grd>=60:
        message="C+"   
    elif grd>=55:
        message="C"    
    elif grd>=50:
        message="C+" 
    elif grd>=40:
        message="D"   
    else:
        message="F⚡"  
    if grd > 100 or grd < 1:
        return "Invalid input ⚠️ Grade must be between 1 and 100"    

    return message     

print("  Next is if...elif...else statement")   
print(grade(99))   ##print A+
print(grade(86))    ##print   A
print(grade(80))        ##print A-
print(grade(79.999999))    ##print  B+
print(grade(73.7))         ##print  B
print(grade(68.9))         ##print  B-
print(grade(60))         ##print  C+
print(grade(56))         ##print   C
print(grade(50.00000001))     ##print C-
print(grade(44))             ##print  D
print(grade(23))            ##print   F⚡
print(grade(-10))        ##print   Invalid input ⚠️ Grade must be between 1 and 100
print(grade(101))        ##print    Invalid input ⚠️ Grade must be between 1 and 100
print(grade(0))            ##print    Invalid input ⚠️ Grade must be between 1 and 100

print("      ")

name=["gemachis","tesfaye","daagim","geexuu","simalee","sisaay","bonsa","tilahun",]
print(type(name))
print(name)
print(len(name))
print("first-index",name[0])
print("second-index",name[1])
print("third-index",name[2])
print("fourth-index",name[3])
print("fifith-index",name[4])
print("sixth-index",name[5])
print("seventh-index",name[6])
print("eighteth index",name[7])
print("from first to fourth",name[:4])
print("final three", name[-3:])
name.append("feenet")
print(name)
name.remove("bonsa")
print(name)
score=[10,50,30,90,87,63,27,17]
print("the length",len(score))
print("the minimums is ",min(score))
print("the maximum is ",max(score))
print("total score is ",sum(score))
print("average of score",sum(score)/len(score))

print(max(2,4,6,2,8,5,3))
print(min(2,4,6,2,8,5,3))
print(sum([2,4,6,2,8,5,3]))
print(len([2,4,6,2,8,5,3])) 
