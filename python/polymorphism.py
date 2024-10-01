#method overloading

'''class a:
    def sum(self,a,b):
        return a+b
    def sum(self,a,b,c=1):
        return a+b+c
obj=a()
print(obj.sum(1,2,5))'''

#method overriding

'''class a:
    def display(self):
        print("this is class a")
class b(a):
    def display(self):
        print("this is class b")
        super().display()
obj=b()
obj.display()'''
