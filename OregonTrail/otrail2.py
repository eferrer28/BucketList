import random

class Food(object):
    pass

class Bullets(object):
    pass
    
class Wheel(object):
    pass
    
#makes our player class which carries our name and our money
class Player(object):
    def __init__(self, name):
        self.name = name
        self.money = 1000
        self.health = 100
        self.minmoney = 0
        self.max_health = 100
        self.items = {"food": 1, "bullets": 1}

    def recover_health(self, amount):
	    if self.health + amount > self.max_health:
	        self.health = self.max_health
	    else:
	        self.health += amount

playername = raw_input("Please type in your name \n")
p1 = Player(playername)
print ("Good luck on your journey to Oregon, " + p1.name)

class Wagon(object):
    def __init__(self):
        self.distance_traveled = 0
        self.endgame = 2300
        self.weight = 0 
        self.max_weight = 2500
        
w1 = Wagon() #instance of wagon class 


class Store(object):
    store_inventory = {"food": [1, 1], "bullets": [5, 10]} #values represent, weight per unit and cost

    def barter(self):
        purchase = raw_input("What do you want to buy today? \n").lower()
        if purchase in s1.store_inventory.keys(): #searches the keys of the store dictionary
            qty = int(raw_input("How much %s you looking to buy today?" %purchase)) 
            price = s1.store_inventory.get(purchase)[1]     
            p1.money = p1.money - qty * price
            if purchase in p1.items.keys() and p1.money > p1.minmoney: 
                p1.items[purchase] += qty #adds the #of units purchased to our player inventory(items)
                print str(qty) + " units of " + purchase + " have been added to your inventory."
                print ("Okay that's gonna cost you" + str(qty * price) + " dollars. You still have %s" %p1.money)
                decision = raw_input("Do you still want to shop? Y/N \n").upper()
                if  decision == "Y":
                    return self.barter()
                if decision == "N":
                    return main()
                else:
                    print "That's not a valid option"
            else:
                    print "Sorry, you can't afford that"
            
        else: 
            print "We don't carry that."
            return self.barter()
     
s1 = Store()    

def show():
    print "Your wagon can store up to" + str(w1.max_weight - w1.weight) + " more pounds of weight"
        
    
def indians():
    p1.health -= 5
    print "Oh no! You have run into a group of Indians. You were a hit by arrow in your butt while running away"
    

def river():
    decision = raw_input("Oh no! We have hit a river. Should we try floating accros or pay 30 for a ferry crossing? \n")
    if decision == "f":
        p1.money -=30
        print "We have made it accross the river safely. But we now have only" + str(p1.money) + "dollars remaining"
        
def illness():
    p1.health -=20
    print "Oh no! You have contracted the measles. You can continue moving forward but maybe some rest will do you good."
 
    
def hunt():
    p1.items["food"] +=25
    print "Lets go hunting"
    
    
    

    print p1.items
        
trouble = [indians, river, illness] #add weather 

#runs the game
def main():
    while w1.distance_traveled < 2300:
        decision = raw_input("What would you like to do? Check [S]tatus. [T]ravel west? [H]unt? [B]arter? [R]est? \n").upper()
        if decision == "S":
            print "So far you have travelled " + str(w1.distance_traveled) + " miles. Only "+ str(w1.endgame - w1.distance_traveled) + " miles remain."
            print p1.health
            for keys, values in p1.items.items():
                print "You have have %s unit(s) of %s" %(values, keys)
        if decision == "T":
           if p1.items["food"] <= 40:
            print "We are critically low on food. We need to hunting."
           p1.items["food"] -= 40
           w1.distance_traveled += 40
           if w1.distance_traveled % 400 == 0 and w1.distance_traveled > 0:
               random.choice(trouble)() #draws from random list of events
           if w1.distance_traveled == 1160:
               print "You have made it to Independence Rock! Just past the halfway point! Enjoy the view!"
           else: 
               print "You made it without incurring any attacks"
        if decision == "H":
            hunt()
        if decision == "B":
            print ("Welcome! Check out my endless supply of items!")
            for x,y in s1.store_inventory.items():
                print x,y 
            s1.barter()
        if decision == "R":
            p1.recover_health(2)
            print ("You have decided to rest for the day and heal some health. Your health is now ") + str(p1.health)
    else: 
        print "You have made it to Oregon. Woohoo!"
main()

