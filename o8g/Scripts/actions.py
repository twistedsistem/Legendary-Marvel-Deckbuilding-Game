import re

def setupGame(group = table, x = 0, y = 0, manual = False):
   #debugNotify(">>> setupGame(){}".format(extraASDebug())) #Debug
    mute()
    deck = shared.LoadDeck
    countAgent = 0
    countTrooper = 0
    countPlayer = 0
    countScheme = 0
    countBystander = 0
    schemeNumber = 0
    countMasterStrike = 0
    masterMindNumber = 0
    soloSchemeList = [1,3,4,5,7,8]
    allSchemeList = [1,2,3,4,5,6,7,8]
    coreHeroList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    coreVillainList = [1,2,3,4,5,6,7]
    coreHenchmenList = [1,2,3,4]
    coreMasterMindList = [1,2,3,4]
    gameVillainList = []
    gameHeroList = []
    if countPlayer == 0: countPlayer = askInteger("How many players are there?", 1)
    if schemeNumber == 0: 
        if countPlayer == 1:
            schemeIndex = rnd(0,len(soloSchemeList)-1)
            schemeNumber = soloSchemeList[schemeIndex]
        else: 
            schemeIndex = rnd(0,len(allSchemeList)-1)
            schemeNumber = allSchemeList[schemeIndex]
    if masterMindNumber == 0:
        masterMindIndex = rnd(0,len(coreMasterMindList)-1)
        masterMindNumber = coreMasterMindList[masterMindIndex]
        #notify("Mastermind Index has been set to {}.".format(masterMindNumber))
    #debugNotify("Checking Deck", 3)
    if len(deck) == 0:
        whisper ("Please load a deck first!")
        return
    # debugNotify("Placing Wounds", 3)
    globalVariableUpdate(schemeNumber,countPlayer)
    for card in deck:
        if card.CardType == 'Wound':
            card.moveToTable(210,-329) #210,-339
            card.orientation = Rot90
            continue
        elif card.CardType == 'Scheme Twist':
            if countScheme < int(getGlobalVariable('schemeTwistAmount')):
                card.moveTo(shared.Villains)
                countScheme = countScheme + 1
            continue
        elif card.CardType == 'Bystander':
            if countBystander < int(getGlobalVariable('bystanderAmount')):
                card.moveTo(shared.Villains)
                countBystander = countBystander + 1
            else:
                card.moveToTable(445,-310) #445,-310
            continue
        elif card.CardType == 'Scheme':
            if card.SetupNumber == str(schemeNumber):
                card.moveToTable(-572,-310)
            continue
        elif card.CardType == 'Mastermind':
            if card.SetupNumber == str(masterMindNumber):
                card.moveToTable(-572,-75)
                notify("{} set the Mastermind to {}. GOOD LUCK!!".format(me,card.Name))
            continue
        elif card.CardType == 'Master Strike':
            if countPlayer == 1:
                if countMasterStrike < 1:
                    card.moveTo(shared.Villains)
                    countMasterStrike = countMasterStrike + 1
            else:
                if countMasterStrike < 5:
                    card.moveTo(shared.Villains)
                    countMasterStrike = countMasterStrike + 1
            continue
        elif card.CardType == 'Mastermind Tactic':
            if card.SetupNumber == str(masterMindNumber):
                card.moveTo(shared.MasterMinds)
            continue
        elif card.Name == 'SHIELD Officer':
            card.moveToTable(-572,164)
            continue
        elif card.Name == 'SHIELD Agent':
            if countAgent < 8:
                for p in players:
                    card.moveTo(p.Deck)
                    continue
                countAgent = countAgent + 1
            continue
        elif card.Name == 'SHIELD Trooper':
            if countTrooper < 4:
                for p in players:
                    card.moveTo(p.Deck)
                    continue
                countTrooper = countTrooper + 1
            continue
    for p in players:
        p.Deck.shuffle()
        continue
    notify("Scheme Twist count {}.".format(getGlobalVariable('schemeTwistAmount')))
    notify("Bystander count {}.".format(getGlobalVariable('bystanderAmount')))
    notify("Henchmen count {}.".format(getGlobalVariable('henchmenAmount')))
    notify("Villain count {}.".format(getGlobalVariable('villainAmount')))
    notify("Hero count {}.".format(getGlobalVariable('heroAmount')))

def globalVariableUpdate(gameScheme,playerCount):
    notify("The Game Scheme going through the function is {} and the player count is set to {}".format(gameScheme,playerCount))
    if gameScheme == 1:
        setGlobalVariable('schemeTwistAmount','8')
        setGlobalVariable('bystanderAmount','12')
        if playerCount == 1:
            setGlobalVariable('henchmenAmount','1')
            setGlobalVariable('villainAmount','1')
        elif playerCount == 2:
            setGlobalVariable('henchmenAmount','1')
            setGlobalVariable('villainAmount','2')
        elif playerCount == 3:
            setGlobalVariable('henchmenAmount','1')
            setGlobalVariable('villainAmount','3')
        elif playerCount == 4:
            setGlobalVariable('henchmenAmount','2')
            setGlobalVariable('villainAmount','3')
        elif playerCount == 5:
            setGlobalVarialbe('henchmenAmount','2')
            setGlobalVariable('villainAmount','4')
    elif gameScheme == 2:
        #solo game can't have this scheme so not adding a playerCount 1 if
        if playerCount == 2:
            setGlobalVariable('henchmenAmount','2')
            setGlobalVariable('villainAmount','2')
            setGlobalVariable('bystanderAmount','2')
        elif playerCount == 3:
            setGlobalVariable('henchmenAmount','2')
            setGlobalVariable('villainAmount','3')
            setGlobalVariable('bystanderAmount','8')
        elif playerCount == 4:
            setGlobalVariable('henchmenAmount','3')
            setGlobalVariable('villainAmount','3')
            setGlobalVariable('bystanderAmount','8')
        elif playerCount == 5:
            setGlobalVarialbe('henchmenAmount','3')
            setGlobalVariable('villainAmount','4')
            setGlobalVariable('bystanderAmount','12')
        setGlobalVariable('schemeTwistAmount','8')
    elif gameScheme == 3:
        setGlobalVariable('schemeTwistAmount','7')
        if playerCount == 1:
            setGlobalVariable('henchmenAmount','1')
            setGlobalVariable('villainAmount','1')
            setGlobalVariable('bystanderAmount','1')
        elif playerCount == 2:
            setGlobalVariable('henchmenAmount','1')
            setGlobalVariable('villainAmount','2')
            setGlobalVariable('bystanderAmount','2')
        elif playerCount == 3:
            setGlobalVariable('henchmenAmount','1')
            setGlobalVariable('villainAmount','3')
            setGlobalVariable('bystanderAmount','8')
        elif playerCount == 4:
            setGlobalVariable('henchmenAmount','2')
            setGlobalVariable('villainAmount','3')
            setGlobalVariable('bystanderAmount','8')
        elif playerCount == 5:
            setGlobalVarialbe('henchmenAmount','2')
            setGlobalVariable('villainAmount','4')
            setGlobalVariable('bystanderAmount','12')
    elif gameScheme == 4:
        setGlobalVariable('schemeTwistAmount','5')
        if playerCount == 1:
            setGlobalVariable('henchmenAmount','1')
            setGlobalVariable('villainAmount','1')
            setGlobalVariable('bystanderAmount','18')
        elif playerCount == 2:
            setGlobalVariable('henchmenAmount','1')
            setGlobalVariable('villainAmount','2')
            setGlobalVariable('bystanderAmount','18')
        elif playerCount == 3:
            setGlobalVariable('henchmenAmount','1')
            setGlobalVariable('villainAmount','3')
            setGlobalVariable('bystanderAmount','18')
        elif playerCount == 4:
            setGlobalVariable('henchmenAmount','2')
            setGlobalVariable('villainAmount','3')
            setGlobalVariable('bystanderAmount','18')
        elif playerCount == 5:
            setGlobalVarialbe('henchmenAmount','2')
            setGlobalVariable('villainAmount','4')
            setGlobalVariable('bystanderAmount','18')
    elif gameScheme == 5:
        setGlobalVariable('schemeTwistAmount','8')
        setGlobalVariable('heroAmount','6')
        if playerCount == 1:
            setGlobalVariable('henchmenAmount','1')
            setGlobalVariable('villainAmount','1')
            setGlobalVariable('bystanderAmount','1')
        elif playerCount == 2:
            setGlobalVariable('henchmenAmount','1')
            setGlobalVariable('villainAmount','2')
            setGlobalVariable('bystanderAmount','2')
        elif playerCount == 3:
            setGlobalVariable('henchmenAmount','1')
            setGlobalVariable('villainAmount','3')
            setGlobalVariable('bystanderAmount','8')
        elif playerCount == 4:
            setGlobalVariable('henchmenAmount','2')
            setGlobalVariable('villainAmount','3')
            setGlobalVariable('bystanderAmount','8')
        elif playerCount == 5:
            setGlobalVarialbe('henchmenAmount','2')
            setGlobalVariable('villainAmount','4')
            setGlobalVariable('bystanderAmount','12')
    elif gameScheme == 6:
        #solo game can't have this scheme so not adding a playerCount 1 if
        if playerCount == 2:
            setGlobalVariable('henchmenAmount','1')
            setGlobalVariable('villainAmount','2')
            setGlobalVariable('bystanderAmount','2')
            setGlobalVariable('schemeTwistAmount','8')
            setGlobalVariable('heroAmount','4')
        elif playerCount == 3:
            setGlobalVariable('henchmenAmount','1')
            setGlobalVariable('villainAmount','3')
            setGlobalVariable('bystanderAmount','8')
            setGlobalVariable('schemeTwistAmount','8')
        elif playerCount == 4:
            setGlobalVariable('henchmenAmount','2')
            setGlobalVariable('villainAmount','3')
            setGlobalVariable('bystanderAmount','8')
            setGlobalVariable('schemeTwistAmount','5')
        elif playerCount == 5:
            me.setGlobalVarialbe('henchmenAmount','2')
            setGlobalVariable('villainAmount','4')
            setGlobalVariable('bystanderAmount','12')
            setGlobalVariable('schemeTwistAmount','5')
    elif gameScheme == 7:
        setGlobalVariable('schemeTwistAmount','8')
        if playerCount == 1:
            setGlobalVariable('henchmenAmount','1')
            setGlobalVariable('villainAmount','1')
            setGlobalVariable('bystanderAmount','1')
        elif playerCount == 2:
            setGlobalVariable('henchmenAmount','1')
            setGlobalVariable('villainAmount','2')
            setGlobalVariable('bystanderAmount','2')
        elif playerCount == 3:
            setGlobalVariable('henchmenAmount','1')
            setGlobalVariable('villainAmount','3')
            setGlobalVariable('bystanderAmount','8')
        elif playerCount == 4:
            setGlobalVariable('henchmenAmount','2')
            setGlobalVariable('villainAmount','3')
            setGlobalVariable('bystanderAmount','8')
        elif playerCount == 5:
            me.setGlobalVarialbe('henchmenAmount','2')
            setGlobalVariable('villainAmount','4')
            setGlobalVariable('bystanderAmount','12')
    elif gameScheme == 8:
        setGlobalVariable('schemeTwistAmount','8')
        if playerCount == 1:
            setGlobalVariable('henchmenAmount','1')
            setGlobalVariable('villainAmount','1')
            setGlobalVariable('bystanderAmount','1')
        elif playerCount == 2:
            setGlobalVariable('henchmenAmount','1')
            setGlobalVariable('villainAmount','2')
            setGlobalVariable('bystanderAmount','2')
        elif playerCount == 3:
            setGlobalVariable('henchmenAmount','1')
            setGlobalVariable('villainAmount','3')
            setGlobalVariable('bystanderAmount','8')
        elif playerCount == 4:
            setGlobalVariable('henchmenAmount','2')
            setGlobalVariable('villainAmount','3')
            setGlobalVariable('bystanderAmount','8')
        elif playerCount == 5:
            me.setGlobalVarialbe('henchmenAmount','2')
            setGlobalVariable('villainAmount','4')
            setGlobalVariable('bystanderAmount','12')

def sitstand(group, x = 0, y = 0):
    isstanding = me.getGlobalVariable("standing")
    if isstanding == "1":
        notify("{} is now sitting.".format(me))
        setGlobalVariable("standing","0")
    else:
        notify("{} is now standing.".format(me))
        setGlobalVariable("standing","1")

def ssstatus(group, x = 0, y = 0):
    notify("Getting sit stand")
    for p in players:
        gv = p.getGlobalVariable("standing")
        if gv == "1":
            notify("{} is standing.".format(p))
        else:
            notify("{} is sitting.".format(p))

def becomedealer(group,x=0,y=0):
    notify("{} is now dealer.".format(me))
    setGlobalVariable("dealer",me._id)

def whosdealer(group,x=0,y=0):
    ret = getGlobalVariable("dealer")
    notify("{} dealer num".format(ret))
    ret = int(ret)
    notify("{} dealer num".format(ret))
    for p in players:
        if p._id == ret:
            notify("{} is dealer.".format(p))
            break

def rolldice(group, x = 0, y = 0):
    mute()
    n = rnd(1, 6)
    notify("{} rolls {} on a 6-sided die.".format(me, n))

def flipcoin(group, x = 0, y = 0):
    mute()
    n = rnd(1, 2)
    if n == 1:
      notify("{} flips heads.".format(me))
    else:
      notify("{} flips tails.".format(me))
	  
def listplayers(group, x = 0, y = 0):
    notify("{}".format(players))

def interrupt(group, x = 0, y = 0):
    notify('{} interrupts the game.'.format(me))

def passturn(group, x = 0, y = 0):
    notify('{} passes.'.format(me))

def tap(card, x = 0, y = 0):
  mute()
  card.orientation ^= Rot90
  if card.orientation & Rot90 == Rot90:
    notify('{} turns {} sideways'.format(me, card))
  else:
    notify('{} turns {} upright'.format(me, card))

def flip(card, x = 0, y = 0):
    mute()
    if card.isFaceUp == True:
      notify("{} flips {} face down.".format(me, card))
      card.isFaceUp = False
    else:
      card.isFaceUp = True
      notify("{} flips {} face up.".format(me, card))

def discard(card, x = 0, y = 0):
  mute()
  src = card.group
  fromText = " from the table" if src == table else " from their " + src.name
  card.moveTo(shared.Discard)
  notify("{} discards {}{}.".format(me, card, fromText))

def highlightcard(card, x = 0, y = 0):
  mute()
  if card.highlight == "#ff0000":
    card.highlight = None
    notify('{} removes highlight from {}'.format(me, card))
  else:
    card.highlight = "#ff0000"
    notify('{} highlights {}'.format(me, card))

def draw(group, x = 0, y = 0):
    if len(shared.LoadDeck) == 0: return
    mute()
    shared.LoadDeck[0].moveTo(me.hand)
    notify("{} draws a card.".format(me))

def drawMany(group, count = None):
    if len(shared.LoadDeck) == 0: return
    mute()
    if count == None: count = askInteger("Draw how many cards?", 7)
    for c in shared.LoadDeck.top(count): c.moveTo(me.hand)
    notify("{} draws {} cards.".format(me, count))

def dealMany(group, count=None):
    dealerid = int(getGlobalVariable("dealer"))
    if me._id != dealerid:
        whisper("You are not the dealer player.")
        return
    if len(shared.LoadDeck) == 0: return
    mute()
    if count == None: count = askInteger("Deal how many cards?", 5)
    for num in range(count):
        for p in players:
            standing = int(p.getGlobalVariable("standing"))
            if standing == 0:
                notify("Dealing {} a card.".format(p))
                for c in shared.LoadDeck.top(1): c.moveTo(p.hand)

def dealManyToTable(group, x = 0, y = 0, count=None):
    dealerid = int(getGlobalVariable("dealer"))
    if me._id != dealerid:
        whisper("You are not the dealer player.")
        return
    if len(shared.LoadDeck) == 0: return
    mute()
    if count == None: count = askInteger("Deal how many cards to table?", 5)
    for c in shared.LoadDeck.top(count): 
        c.moveTo(table)
    notify("Dealing {} cards to table.".format(count))

def dealManyToTableDown(group,x = 0, y = 0, count=None):
    dealerid = int(getGlobalVariable("dealer"))
    if me._id != dealerid:
        whisper("You are not the dealer player.")
        return
    if len(shared.LoadDeck) == 0: return
    mute()
    if count == None: count = askInteger("Deal how many cards to table face down?", 5)
    for c in shared.LoadDeck.top(count): 
        c.moveTo(table)
        c.isFaceUp = False
    notify("Dealing {} cards to table face down.".format(count))

def drawManyDown(group, count = None):
    if len(shared.LoadDeck) == 0: return
    mute()
    if count == None: count = askInteger("Draw how many cards?", 7)
    for c in shared.LoadDeck.top(count):
        c.moveTo(me.hand)
        c.isFaceUp = False
    notify("{} draws {} cards face down.".format(me, count))

def mill(group, count = None):
    if len(shared.LoadDeck) == 0: return
    mute()
    if count == None: count = askInteger("Mill how many cards?", 1)
    for c in shared.LoadDeck.top(count): c.moveTo(shared.Discard)
    notify("{} mills the top {} cards from the Deck.".format(me, count))

def shuffle(group, x = 0, y = 0):
   mute()
   shared.LoadDeck.shuffle()
   if me.isActivePlayer:
     notify("{} shuffled the deck.".format(me))
   else:
     whisper("You are not the active player.")
def shuffleIntoDeck(group, x = 0, y = 0):
    mute()
    for c in group: c.moveTo(shared.LoadDeck)
    shared.LoadDeck.shuffle()
    notify("{} shuffled the discard pile into the deck.".format(me))

StandardMarker = ("Marker", "40bba10f-82e5-4f7e-986b-e9c850524f88")

def addanymarker(cards, x = 0, y = 0):
    mute()
    marker, quantity = askMarker()
    if quantity == 0: return
    for card in cards:
      card.markers[marker] += quantity
      notify("{} adds {} {} counters to {}.".format(me, quantity, marker[0], card))

def addmarker(card, x = 0, y = 0):
    mute()
    card.markers[StandardMarker] += 1
    notify("{} adds a marker to {}.".format(me, card))

def removemarker(card, x = 0, y = 0):
    mute()
    card.markers[StandardMarker] -= 1
    notify("{} removes a marker from {}.".format(me, card))
