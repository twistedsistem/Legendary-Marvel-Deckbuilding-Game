def grabCardControl(card, player = me):
   if card.group != table: notify("Cannot grab card control while in a pile.")
   else:
      if card.controller != player: 
         if card.controller != me: remoteCall(card.controller,'passCardControl',[card,player])
         else: passCardControl(card,player) 
   
def passCardControl(card,player):
   mute()
   update()
   if card.controller != player: card.setController(player)

def setGroupController(group,player):
   mute()
   update()
   if group.controller != player: group.setController(player)

def passTurn():
   mute()
   update()
   if int(getGlobalVariable('activePlayer')) == len(players):
      nextPlayer = 1
   else:
      nextPlayer = int(getGlobalVariable('activePlayer'))
   index = nextPlayer - 1
   players[index].setActivePlayer()

def rndAddx(pList,fList,rangeNumber):
   for i in range(rangeNumber):
      added = False
      while added != True:
         aObject = pList[rnd(0,len(pList)-1)]
         if aObject not in fList:
            fList.append(aObject)
            added = True
   return fList

def shuffle(group): 
   group.shuffle()
     
def shuffleIntoDeck(group, x = 0, y = 0):
    mute()
    for c in group: c.moveTo(me.Deck)
    me.Deck.shuffle()
    notify("{} shuffled the discard pile into the deck.".format(me))