'''x=int(input("enter a number:"))
y=int(input("enter a number:"))
try:
    print(x/y)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
finally:
    print("executed")'''


'''for i in range(5):
    if i==4:
        break
    print(i)
else:
    print("executed")'''

#value error
'''try:
    a=int(input("enter a number:"))
    print(a)
except ValueError as e:
    print(e)
else:
    print("executed")
'''

#to throw an exception
'''a=int(input("enter a number:"))
if a<0:
    raise Exception("number should be positive")
else:
    print(a)'''


#keep asking valid integer input from user
#if not valid integer then throw an exception and ask again until user enters valid integer
'''while True:
    try:
        a=int(input("enter a number:"))
        print(a)
        break
    except ValueError as e:
        print(e)'''
 

#handle index errror while accessing list elements
'''try:
    list=[1,2,3,4,5]
    print(list[3])
except IndexError as e:
    print(e)
'''