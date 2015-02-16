from __future__ import print_function
import random

COLORS = ["yellow", "red", "black", "blue"]


class Enemy(object):
    def __init__(self,hitpoints):
        self.color = COLORS[random.randint(0,len(COLORS)-1)]
        self.hitpoints = None
        
    def __str__(self):
       return("OH NO! You have run into a %s, %s, %d: Prepare for battle!")% (self.color, self.__class__.__name__,   self.hitpoints)
       
    def battleseq(self):
        aor = raw_input("What do you want to do? Fight(F) or Run(R)?")
        
        if aor == "f":
            print ("well")
       
        elif aor == "r":
            print ("You idiot. You can't run from a dragon! The dragon has engulfed you in flames.")
            
        else: 
            print ("That's an invalid key. The dragon was mad that you can't follow directions and has engulfed you in flames.")
        
        
class Dragon(Enemy):
    def __init__(self, hitpoints=100):
         super(Dragon, self).__init__(hitpoints)
         self.hitpoints = hitpoints
        
    

        


#DUNGEON MAP, made with a list of tuples. I didn't know any other way =/
map = [(0, 0), (1, 0), (2, 0), (3,0),
         (0, 1), (1, 1), (2, 1), (3,1),
         (0, 2), (1, 2), (2, 2), (3,2),
         (0, 3), (1, 3), (2, 3), (3,3)]

                
                    
         
# This function sets the exit and starting location and the random spot for the monster.
def location():
  monster = map[11]
  door = map[0]
  player = map[15] 
  # if monster, door, or start are the same, do it again

  if monster == door or monster == player:
    return location()

  return monster, door, player

# function for moving the player
def move_player(player, move):
  # get the player's current location
  x, y = player  
 

  if move == 'LEFT':
    x -= 1
  
  elif move == 'RIGHT':
    x += 1
  
  elif move == 'UP':
    y -= 1

  elif move == 'DOWN':
    y += 1
  return x, y


def get_moves(player):
  moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
  # player = (x, y)
  if player[0] == 0:
    moves.remove('LEFT')
  if player[0] == 3:
    moves.remove('RIGHT')
  if player[1] == 0:
    moves.remove('UP')
  if player[1] == 3:
    moves.remove('DOWN')

  return moves

def draw_map(player):
  print(' _ _ _ _') 
  tile = '|{}'

  for index, cell in enumerate(map):
    if index in [0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14]:
      if cell == player:
        print(tile.format('X'), end='')
      else:
        print(tile.format('_'), end='')
    else:
      if cell == player:
        print(tile.format('X|'))
      else:
        print(tile.format('_|'))

monster, door, player = location()

print ("""
       After a heavy night of drinking, you have ended up in a mysterious dungeon. 
       Try to reach the end of the dungeon without killing yourself. Type in 'SHOWMAP'
       to see the location of yourself in the dungeon at any time. 'X' marks your
       current location. Your valid moves are only 'UP', 'DOWN', 'RIGHT', and 'LEFT'. 
       Choose Wisely. 
       """)

while True:
  moves = get_moves(player)
 

  print("You can move {}".format(moves)) 
  print("Enter QUIT to quit")

  move = raw_input("> ")
  move = move.upper()

  if move == "SHOWMAP":
    draw_map(player)
    continue

  if move == 'QUIT':
    break

  if move in moves:  
    player = move_player(player, move)
  else:
    print(" Err. You're running into a wall there. ")
    continue

  if player == door:
    print("WINNA, WINNA")
    break
  
  elif player == monster:
    big_boss = Dragon() #big_boss is an instance of the dragon class 
    print (big_boss)
    big_boss.battleseq() 
   
    
    