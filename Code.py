import sys
import random
from collections import deque

class go_fish:
  def __init__(self,n_players):
    self.n_players = n_players
    for i in range(1,14):
      for j in range(1,3):
        deck.append(i)
    random.shuffle(deck)

  def distribute_cards(self):
    if self.n_players>2:
      print("only a max of 2 players are allowed")
    elif self.n_players <=1 :
      print("players should be more than 1")
    else:
      for i in range(1,self.n_players+1):
        each_player_list =deque()#stack
        player.append(each_player_list)
        for j in range(1,8):
          if deck:
            each_player_list.append(deck.popleft()) 
      return player

  def transfer(self,which_player,choose_card,current_player):
    while len(deck)!=0:
    
      if (choose_card not in player[which_player-1]) :
        add_card=deck.popleft()
        print("Go Fish")
        print('Card added from Deck: ',add_card)
        current_player.append(add_card)
        print(f'Adding Deck card to player{which_player}: {player}')
        play.check(player)
        break      
      else:
        temp=deque()
        print('It\'s a Match')
        while player[which_player-1]:
          i=player[which_player-1].pop()
          if i!=choose_card:
            temp.append(i)         
          else:
            current_player.append(i)
        else:
          for i in range(1,len(temp)+1):
            player[which_player-1].append(temp.pop())
          print(f'Adding Deck card to player{which_player}: {player}')
          play.check(player)
      return 0
    

  def check(self,player):    
    for player_list in player:     
      for i in range(1,14):
        c=0
        for j in player_list:
          if j == i:
            c=c+1
        if c==2:
          for x in range(2):
            player_list.remove(i)
          scores[player.index(player_list)]+=1
    print('scores: ',scores)
    while len(deck)==0:
      print("Can't draw a card. You have Empty Deck!")
      break

#Main
deck =deque() 
player=deque() 
n_players=int(input('Please enter no.of players: '))
scores=[0 for i in range(n_players)]
play=go_fish(n_players)
print(play.distribute_cards())
while True:
  i=0
  while(i<=n_players) and len(deck)!=0:
    current_player=player[i]
    print()
    print(f'Current player{i+1}')
    print()
    choose_card=int(input("Choose the card you want to ask other player: "))    
    if choose_card in range(1,14):
      while True:
        which_player=int(input("which player do u want to ask? "))
        if which_player != i+1:
          if which_player in range(1,n_players+1):
            x=play.transfer(which_player,choose_card,current_player)
            if x==0:              
              break
            else:
              if i==n_players-1:
                i=0
                break
              else:
                i+=1
                break
          else:
            print("Please choose the player properly, i.e, with in the players list")
            continue
        else:
          print("Please choose the player that is not you")
          continue
    else:
      print("Please choose the valid card btw 1 to 13")
      break
