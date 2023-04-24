# Coin-Game
This is a simulation of the "coin game" that shows how a mathematical concept called "game theory" works.

Here are the rules:
-You and your opponent each decide whether to insert a coin.
-If both of you insert a coin, you both get 2 points.
-If neither of you inserts a coin, nothing happens.
-If one player inserts a coin and the other doesn't, the player who doesn't insert a coin gets 3 points, and the other player loses 1 point.

The main question is how much each player trusts the other to make the best decision for both.

============================

Update 0.5 - A minor update:

#Bug Fixes:

  -Sometimes the oponent didn't choose anything, and nothing appeared on the screen, that happened due to a minor mistake on line 83.
  
  -Randomly the game neven ended due to a logical mistake when I write the turn system.
  
#Oponents:

  -Now the game randomly chooses an "oponent" to play against you:
  
    .The Cooperative: who always inserts the coin;
    
    .The Thief: who never inserts the coin;
    
    .The Chaotic: who plays randomly.
 
============================ 

Update 1.0 - New oponents:

#Now we have three new oponents:

  -The Copycat: who copies your last decision;
  
  -The Rancorous: who starts out cooperative but becomes a thief if you don't insert the coin once;
  
  -The Detective: who follows a specific pattern of insert/not insert decisions in the first four turns, then acts like a thief or copycat depending on your behavior.
