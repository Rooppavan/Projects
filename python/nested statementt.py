'''age=int(input("enter a age:"))
if age>=0:
    if age<5:
        print("kid")
    elif age<15:
        print("chlid")
    elif age<30:
        print("teen")
    elif age<50:
        print("mid")
    else:
        print("old")
else:
    print("about to born")'''

age=int(input("enter a age:"))
gender=(input("enter a gender:"))
if gender=='m'or 'M':
    if age>21:
        print("major")
    else:
        print("Minor")
elif gender=='f'or'F':
    if age>18:
        print("major")
    else:
        print("minor")
else:
    print("Nothing")

         
        
        
