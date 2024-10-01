oldbal=int(input("enter a old bal amount;"))
ttype=input("enter a type:")
tamt=int(input("enter a tamt amount:"))
lst=['w','W','d','D']
if ttype in lst[0:2:1]:
    if tamt>oldbal:
        print("ins.fund:")
    elif tamt==oldbal:
        print("plz maintain min bal:")
    else:
        cbal=oldbal-tamt
        print("Current bal is:", cbal)
elif ttype in lst[2:4:1]:
    if tamt>=50000:
        print("Req PAN details")
    else:
        cbal=oldbal+tamt
        print("Current bal is:", cbal)

else:
    print("Invalid input")
    
        
