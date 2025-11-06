class Warrior:
    def attack(self):
        print("Warrior attacks with a sword!")

class Mage:
    def attack(self):
        print("Mage casts a fireball!")

class Archer:
    def attack(self):
        print("Archer shoots an arrow!")


warrior = Warrior()
mage = Mage()
archer = Archer()


characters = [warrior, mage, archer]

for char in characters:
    char.attack()
