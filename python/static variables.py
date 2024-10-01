'''class sample1:
    x=111
    def f1(self):
        self.y=222
sample1.y=765
s=sample1()
print(sample1.y)'''

class sample2:
    x=111
    def f1(self):
        self.x=222
        print(self.x)
        
sample2.y=234
s=sample2()
print(s.x,s.y,sep='\n')
s.f1()
