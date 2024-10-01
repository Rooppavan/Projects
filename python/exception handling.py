
'''def div(x,y):
    try:
        res=x/y
        print("your answer is",res)
    except ZeroDivisionError:
        print("soory")

div(3,0)'''


x=int(input("enter a number"))
y=int(input("enter a number"))
try:
    res=x/y
    print(res)
except ZeroDivisionError:
    print("sorry")
       
