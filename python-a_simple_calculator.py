import math

A = []
for i in range(3):
    A.append(input("请按照数字、符号、数字的顺序输入，每次一个，以回车结束："))
    

if A[1] == "+":
    print(float(int(A[0])+int(A[2])))
if A[1] == "-":
    print(float(int(A[0])-int(A[2])))
if A[1] == "*":
    print(float(int(A[0])*int(A[2])))
if A[1] == "/":
    print(float(int(A[0])/int(A[2])))

'''if __name__ == '__main__':
    print(A) '''
