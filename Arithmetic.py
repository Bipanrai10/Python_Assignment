A=int(input("Enter the value of A:-"))
B=int(input("Enter the value of B:-"))
print("Select the operator -\n \
      1.Addition\n \
      2.Subtraction\n \
      3.Multiplication\n \
      4.Divide\n ")
select=int(input("select operations from 1,2,3,4:-"))
if select==1:
    print(A,"+",B,"=",A+B)
elif select==2:
    print(A,"-",B,"=",A-B)
elif select==3:
    print(A,"*",B,"=",A*B)
elif select==4:
    print(A,"/",B,"=",A/B)
else:
    print("Eroor Occur")