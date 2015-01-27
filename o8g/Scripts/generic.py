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
  pList = eval(getGlobalVariable('playerList'))
  if pList.index(me.name) == (len(pList) - 1):
    nextPlayer = pList[0]
  else:
    nextPlayer = pList[pList.index(me.name) + 1]
  for p in players:
    if p.name == nextPlayer:
      players[players.index(p)].setActivePlayer()

def rndAddx(pList,fList,rangeNumber):
   for i in range(rangeNumber):
      added = False
      while added != True:
         aObject = pList[rnd(0,len(pList)-1)]
         if aObject not in fList:
            fList.append(aObject)
            added = True
   return fList

def updatePlayerList():
  mute()
  update()
  pList = eval(getGlobalVariable('playerList'))
  for p in players:
    if p.name not in pList:
      pList.append(p.name)
  setGlobalVariable('playerList',str(pList))  

def shuffle(group): 
   group.shuffle()
     
def shuffleIntoDeck(group, x = 0, y = 0):
    mute()
    for c in group: c.moveTo(me.Deck)
    me.Deck.shuffle()
    notify("{} shuffled the discard pile into the deck.".format(me))

def listOfDupIndex(seq,item):
  start_at = -1
  locs = []
  while True:
    try:
      loc = seq.index(item,start_at+1)
    except ValueError:
      break
    else:
      locs.append(loc)
      start_at = loc
  return locs