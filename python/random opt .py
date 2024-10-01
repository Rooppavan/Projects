'''import random

for i in range(0,10):
    print(random.randint(1111,9999))'''


'''import random
def otp():
    for i in range(0,10):
        print(random.randint(1111,9999))
otp()'''


import random
import string
def otp(size):
    generate=''.join([random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits)for i in range(size)])
    return generate
password=otp(10)
print(password)
                      
    
    

     
