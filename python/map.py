'''lst=[1,2,3,4,5]
def sq(x):
    s=x*x
    return s
m=map(sq,lst)
print(m)
sq_lst=list(m)
print("The square of list",sq_lst)'''


'''lst=[1,2,9,8,7]
m=map(lambda x:x*x,lst)
sq_lst=list(m)
print("The square of numbers:",sq_lst)'''

'''tup={1,2,3,4,5}
def sq(x):
    s=x+x
    return s
m=map(sq,tup)
print(m)
sq_tup=tuple(m)
print("the square of tuple",sq_tup)'''



#filter
lst=[1,2,3,4,5]
def even(s):
    if s%2==0:
        return s
    else:
        pass
m=list(filter(even,lst))
print(m)
