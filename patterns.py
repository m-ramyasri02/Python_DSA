#square
'''n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()'''

#right angled triangle
'''n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()'''

#inverted right angled triangle
'''n=5
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()'''

#diamond
'''n=5
for i in range(n):
    for j in range(n-i-1):
        print("-",end=" ")
    for k in range(0,2*i+1):
        print("*",end=" ")
    print()
for i in range(n-2,-1,-1):
    for j in range(n-i-1):
        print("-",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()'''

#armstrong
'''n=int(input("enter num"))
sumi=0
length=len(str(n))
temp=n
while temp>0:
    digi=temp%10
    sumi+=digi**length
    temp=temp//10
if n==sumi:
    print("armstrong")
else:
    print("not armstrong")'''

#hallow square pattern
'''row=4
col=5
for i in range(row):
    for j in range(col):
        if i==0 or i==row-1 or j==0 or j==col-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


#pascal triangle
n=5
for i in range(n):
    for j in range(n-i-1):
        print("-",end=" ")
    for k in range(2*i+1):
        print(i+1,end=" ")
    print()