# how to define a class
# how to create an object

class Person:
    def __init__(self, name, age, dob, gender):
        self.name = name
        self.age = age
        self.dateofbirth = dob
        self.gender = gender
        self.currentyear = 2023
    
    def checkDob(self):
        value = self.currentyear - self.dateofbirth
        if(value == 0):
            return True
        else:
            return False
    def correctAge(self):
        value = self.currentyear - self.dateofbirth
        self.age = value
    

shayanObj = Person("Shayan", 14, 2008, "Male")
aliObj = Person("Ali", 23,2001,"Male")

# print(shayanObj.checkDob())

people = [shayanObj, aliObj]


class Player:
    def __init__(self, userName, ammo,health):
        self.username = userName
        self.ammo = ammo
        self.health = health
        self.position = [90,56,98]


    def fire(self):
        self.ammo -= 1
        # Logic showing the muzzle flash
        # Recoil
        # If you bullet hits the enemy then remove the enemy from the map

    def moveUp(self):
        self.position[2] += 1

    def moveDown(self):
        self.position[2] -= 1
    
    def moveHigh(self):
        self.position[1] += 1


player_shayan = Player("shayanX123", 50,100)

# pick up the event from the user keyboard and map the methods to that event

print(player_shayan.position)

player_shayan.moveUp()

print(player_shayan.position)
