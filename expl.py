"""
We are going to hit a new milestone together
We are going to make our first classes
classes are like a mini program
they're used for many things, very often objects
so to model enemies like a ton of enemies
it can also be like bullets (different projectiles)
depending on what you decide on they are also used
for encapsulating(organizing) code, reusing code, extending functionality
Smarter enemies, same enemies, different ablities
there are different paradigms: object orientated programming (OOP)
"""
import random
import time

#Starting my first class to represent an object in physics (Point mass)

class Pointmass:
    #class attrbutes
    #the intializer method always runz
    def __init__(self,mass=0,vint=0):
        self.mass=mass
        self.vint=vint
        self.momentum_init = self.mass * self.vint

    def changeinmomentum(self,v2):
        """Gives change in momentum given a second vol"""
        momentum_final= self.mass*v2
        return momentum_final - self.momentum_init

    def greeting(self):
        """
        This method just says hello
        """
        say=random.choice(["Hi","Hello","hey", "Sup"])

        return say

    def getdate(self):
        from datetime import date
        return date.today()

    def zatimer(self):
        input("Enter to start zatimer: ")
        start=time.perf_counter()
        input("Type S to stop: ")
        end=time.perf_counter()

        return end-start
