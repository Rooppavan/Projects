#keyword aruguments
'''def myfun(name,age,city,/):
    print("name is:",name)
    print("age is :",age)
    print("city is:",city)
myfun("pavan",22,"hyderabad")'''

#default parameter feature
'''def myadd(x=10,y=20,z=30):
    s=x+y+z
    print("the sum is:",s)
myadd(x=20,y=55,z=60)
myadd()
myadd(z=50)'''

#varags
'''def myadd(*x):
    print("type of x:",type(x))
    print("data of x:",x)
    print("-"*30)
myadd(10,20)
myadd(10,20,30,40,50)
myadd()'''

#kwargs 
import time
def mystudent(**x):
    for item in x.items():
        time.sleep(1)
        k,d=item
        print(k,d,sep='^^^')
mystudent(sno=101)
        
