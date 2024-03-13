#SAD(System analysis and design)
SAD=int(input("Enter the SAD Marks:-"))

#DSA(Data Structure and Algorithm )
DSA=int(input("Enter thr DSA Marks:-"))

#WEB(Web Technology)
WEB=int(input("Enter the WEB Marks:-"))

#Mathematic
MATH=int(input("Enter the marks of Math:-"))

#Oops in java
OOPS=int(input("Enter the marks of OOps java:-"))

Total=SAD+DSA+WEB+MATH+OOPS
Percentage=Total/5
print("Percentage=",Percentage,"%")

if Percentage>80:
    print("Grade=A+")
elif Percentage>=70 and Percentage<=79:
    print("Grade=A")
elif Percentage>=60 and Percentage<=69:
    print("Grade=A-")
elif Percentage>=50 and Percentage<=59:
    print("Grade=B")
elif Percentage>=40 and Percentage<=49:
    print("Grade=B-")
elif Percentage<40:
    print("Fail")
else:
    print("You enter the marks wrong")