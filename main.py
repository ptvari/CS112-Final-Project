"""
I can run any program here
but the main point is to run my class
"""
import random

from expl import Pointmass as ptm

masses=[]

print("I admire my partner")

#Calling my class(I need to change that name)
#for classes we dont call it call but instantiate
for x in range(10):
    v=random.randint(0,67)
    m=random.randint(0,1)
    #instantiate
    masses.append(ptm(mass=m,vint=v))

#checking all da greeting on my 10 masses
for m in masses:print(m.greeting(),"Mass",m.mass,"Vol", m.vint,m.getdate())
print("i wanna know the date dude")
#making a freshhhh instantiation
fresh=ptm()
print("intial momentum: ", fresh.momentum_init)
int(input("Tell me how much fresh speeded up to: "))

