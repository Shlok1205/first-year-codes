class Omnitrix:
    def transform(self):
        print("Transforming into an alien!")

class Ben(Omnitrix):
    def fight(self):
        print("Ben uses alien powers to fight villains.")

# Usage
ben = Ben()
ben.transform()  # Inherited from Omnitrix
ben.fight()      # Ben's own action

# ----------------------------------------------------------------------------------

class Heatblast:
    def fire_attack(self):
        print("Using fire attack!")

class FourArms:
    def super_strength(self):
        print("Using super strength!")

class Ben(Heatblast, FourArms):
    def hero_move(self):
        print("Combining powers to defeat enemies!")

# Usage
ben = Ben()
ben.fire_attack()    # From Heatblast
ben.super_strength() # From FourArms
ben.hero_move()      # Ben's own heroic move

# ----------------------------------------------------------------------------------

class Alien:
    def __init__(self, name):
        self.name = name

    def use_power(self):
        print(f"{self.name}: Power activated!")

class Ben(Alien):
    def use_power(self):
        print("Ben: It's hero time!")

class XLR8(Alien):
    def use_power(self):
        print("XLR8: Speeding into action!")

class FourArms(Alien):
    def use_power(self):
        print("FourArms: Ready to fight!")

# Usage
Ben = Ben("Ben")
Ben.use_power()  

xlr8 = XLR8("XLR8")
xlr8.use_power()      

four_arms = FourArms("FourArms")
four_arms.use_power()  
