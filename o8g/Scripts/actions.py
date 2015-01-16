import re

gameScheme = []
gameMastermind = []
gameVillainList = []
gameHeroList = []
gameHenchmenList = []
gamePlayers = []
schemeID = ''
mastermindID = ''
stCount = 0
stNxt2S = 0
stNxt2MM = 0
bystanderCount = 0

def setupGame(group = table, x = 0, y = 0, manual = False):
    #function to setup that game to be ready to be played
    #----------------------TODO----------------------
    #   - allow for a manual setup of the game
    #
    #
    #------------------------------------------------
    #Grabing the global variables so that we can write to them inside of the function
    mute()
    #Setting a deck variable to save repetition
    deck = shared.LoadDeck
    #Checking to make sure that a deck has been loaded and if the setup has already been ran.
    if len(deck) == 0:
        whisper ("Please load a deck first!")
        return
    elif getGlobalVariable('doneSetup') == 'True':
        whisper ("The game has already been setup.  If you would like to setup again please reset the game and run the setup again.")
        return
    adventureBuild('automated')
    buildDeck(shared.Villains,gameVillainList,'Villain',0)
    buildDeck(shared.Villains,gameHenchmenList,'Henchman Villain',gameSetupRule[str(len(players))]['henchmen']['cardCount'])
    buildDeck(group=shared.Villains,checkList=['Scheme Twist'],checkType='Scheme Twist',countMax=gameSetupRule[str(len(players))][gameScheme[0]]['schemeTwist'])
    buildDeck(group=shared.Villains,checkList=['Bystander'],checkType='Bystander',countMax=(gameSetupRule[str(len(players))]['bystander'] + gameSetupRule[str(len(players))][gameScheme[0]]['bystander']))
    buildDeck(group=shared.Villains,checkList=['Master Strike'],checkType='Master Strike',countMax=gameSetupRule[str(len(players))]['masterStrike'])
    buildDeck(shared.MasterMinds,gameMastermind,'Mastermind Tactic',0)
    buildDeck(shared.Heroes,gameHeroList,'Hero',0)
    createTableCards()
    setupPlayers()
    shuffle(shared.MasterMinds)
    shuffle(shared.Heroes)
    if gameScheme[0] == 'Secret Invasion of the Skrull Shapeshifters':
        for c in shared.Heroes.top(12): c.moveTo(shared.Villains)
    shuffle(shared.Villains)
    fillHQ()
    setGlobalVariable('doneSetup','True')
    #firstSetup = True
    notify('The scheme is:  {}'.format(gameScheme))
    notify('The mastermind is:  {}'.format(gameMastermind))
    notify('The villains are:  {}'.format(gameVillainList))
    notify('The heroes are:  {}'.format(gameHeroList))
    notify('The henchmen are:  {}'.format(gameHenchmenList))

def getPosition(card,x=0,y=0):
    t = getPlayers()
    notify("This cards position is {}".format(card.position))
    notify("The player count is {}.".format(len(t)))

def getOwnerandController(card,x=0,y=0):
    notify("This cards owner is {} and is controlled by {}".format(card.owner,card.controller))
    notify("The card name is {}".format(card.Name))

def buildDeck(group,checkList,checkType,countMax):
    mute()
    for i in range(len(checkList)):
        n = 0
        for card in shared.LoadDeck:
            if card.CardType == checkType:
                if card.HeroOrVillianName == checkList[i]:
                    if countMax > 0:
                        if n < countMax:
                            card.moveTo(group)
                            n = n + 1
                    else:
                        card.moveTo(group)

def adventureBuild(sType):
    global gameScheme,gameMastermind,gameVillainList,gameHeroList,gameHenchmenList
    pCount = len(players)
    hcount = gameSetupRule[str(pCount)]['heroes']
    #setting the scheme for the game.
    if pCount == 1:
        gameScheme = rndAddx(soloSchemeList,gameScheme,1)
        if gameScheme[0] == 'Secret Invasion of the Skrull Shapeshifters':
            gameMastermind.append('Dr. Doom')
    else:
        gameScheme = rndAddx(allSchemeList,gameScheme,1)
    #setting the mastermind for the game.
    if len(gameMastermind) < 1:
        gameMastermind.append(coreMasterMindList[rnd(0,len(coreMasterMindList)-1)])
    #setting Villain list based on Scheme and Mastermind
    if gameScheme[0] == 'Secret Invasion of the Skrull Shapeshifters':
        gameVillainList.append('Skrulls')
    if gameMastermind[0] == 'Dr. Doom':
        gameHenchmenList.append('Doombot Legion')
    elif gameMastermind[0] == 'Loki':
        gameVillainList.append('Enemies of Asgard')
    elif gameMastermind[0] == 'Magneto':
        gameVillainList.append('Brotherhood')
    elif gameMastermind[0] == 'Red Skull':
        gameVillainList.append('Hydra')
    if len(gameVillainList) < gameSetupRule[str(pCount)]['villains']:
        gameVillainList = rndAddx(coreVillainList,gameVillainList,(gameSetupRule[str(pCount)]['villains'] - len(gameVillainList)))
    #setting Henchmen Villain based on the number of players
    if len(gameHenchmenList) < gameSetupRule[str(pCount)]['henchmen']['groupCount']:
        gameHenchmenList = rndAddx(coreHenchmenList,gameHenchmenList,(gameSetupRule[str(pCount)]['henchmen']['groupCount'] - len(gameHenchmenList)))
    if gameScheme[0] == 'Negative Zone Prison Breakout':
        gameHenchmenList = rndAddx(coreHenchmenList,gameHenchmenList,1)
    #setting Hero list based on number of players
    gameHeroList = rndAddx(coreHeroList,gameHeroList,gameSetupRule[str(pCount)]['heroes'])
    if gameScheme[0] == 'Super Hero Civil War':
        if pCount == 2:
            gameHeroList.pop()
            gameHeroList.pop()
    elif gameScheme[0] == 'Secret Invasion of the Skrull Shapeshifters':
        gameHeroList = rndAddx(coreHeroList,gameHeroList,1)

def setupPlayers():
    for p in players:
        #remoteCall(p,'buildDeck',[me.Deck,['SHIELD Agent'],'Hero',8])
        #remoteCall(p,'buildDeck',[me.Deck,['SHIELD Trooper'],'Hero',4])
        buildDeck(group=p.Deck,checkList=['SHIELD Agent'],checkType='Hero',countMax=8)
        buildDeck(group=p.Deck,checkList=['SHIELD Trooper'],checkType='Hero',countMax=4)
        remoteCall(p,'shuffle',[p.Deck])
        notify('{} is Player {}'.format(p.name,players.index(p) + 1))
        continue

def createTableCards():
    for card in shared.LoadDeck:
        if card.CardType == 'Wound':
            card.moveToTable(210,-329) #210,-339
            card.orientation = Rot90
            continue
        elif card.CardType == 'Bystander':
            card.moveToTable(445,-310) #445,-310
            continue
        elif card.Name == 'SHIELD Officer':
            card.moveToTable(-572,164)
            continue
        elif card.Name in gameScheme:
            card.moveToTable(-572,-310)
            continue
        elif card.Name in gameMastermind:
            card.moveToTable(-572,-75)
            continue
        continue

def fillHQ():
    hqArray = eval(getGlobalVariable('hqHeroes'))
    for i in range(5):
        if hqArray[i] == 'Empty':
            shared.Heroes.addViewer(me)
            mvCard = shared.Heroes[0]
            hqArray[i] = mvCard.name
            mvCard.moveToTable(staticPositions['HQ'][str(i+1)]['x'],staticPositions['HQ'][str(i+1)]['y'])
            shared.Heroes.removeViewer(me)
    setGlobalVariable('hqHeroes',str(hqArray))

def buyCard(card, x = 0, y = 0):
    hqArray = eval(getGlobalVariable('hqHeroes'))
    if card.CardType == 'Hero' or card.CardType == 'Wound':
        if me.RP < int(card.Cost):
            notify("{} does not have enough Recruit points to purchase {}.".format(me,card.Name))
        else:
            if card.name in hqArray:
                hqArray.insert(hqArray.index(card.Name),'Empty')
                card.moveTo(me.Discard)
                me.RP = me.RP - int(card.Cost)
                setGlobalVariable('hqHeroes',str(hqArray))
                fillHQ()
            else:
                card.moveTo(me.Discard)
    else:
        notify("You cannot buy this card as it is not a Hero")

def goToStartTurn(group, x=0,y=0):
    mute()
    if getGlobalVariable('endofTurn') != 'False' and turnNumber() > 0:
        whisper("Please have the previous player end their turn first.")
        return
    if getGlobalVariable('doneSetup') != 'True':
        whisper ("Please perform the game setup first (Ctrl+Shift+S)")
        return
    if turnNumber() == 0 and players.index(me) == 0:
        me.setActivePlayer()
    if not me.isActivePlayer and turnNumber() > 0:
        if not confirm("You opponent does not seem to have finished their turn properly with F12 yet. Continue?"): return
        else: me.setActivePlayer()
    tableCards = (card for card in table if (card.CardType == 'Hero' or card.CardType == 'Wound' or card.CardType == 'Bystander' or card.CardType == 'Villain' or card.CardType == 'Henchmen Villain') and card.controller != me)
    for card in tableCards: remoteCall(card.controller,'passCardControl',[card,me]) 
    remoteCall(shared.Villains.controller,'setGroupController',[shared.Villains,me])
    remoteCall(shared.MasterMinds.controller,'setGroupController',[shared.MasterMinds,me])
    remoteCall(shared.Heroes.controller,'setGroupController',[shared.Heroes,me])
    setGlobalVariable('enofTurn','True')
    setGlobalVariable('activePlayer',str(players.index(me)))
    whisper ("You have started your turn")

def goToEndTurn(group, x = 0, y = 0):
    mute()
    if getGlobalVariable('doneSetup') != 'True':
      whisper ("Please perform the game setup first (Ctrl+Shift+S)")
      return
    if me.RP > 0:
        if not confirm("You have not spent all your recruit points for this turn, are you sure you want to declare end of turn"): return
    elif me.AP > 0:
        if not confirm("You have not spent all your attack points for this turn, are you sure you want to declare end of turn"): return
    setGlobalVariable('endofTurn','False')
    myCards = [card for card in table if card.controller == me and card.owner == me] + [card for card in me.hand]
    for card in myCards:
        card.moveTo(me.Discard)
    whisper ("You have ended your turn")
    passTurn()

def draw(group, x = 0, y = 0):
    if len(shared.LoadDeck) == 0: return
    mute()
    shared.LoadDeck[0].moveTo(me.hand)
    notify("{} draws a card.".format(me))

def drawMany(group, count = None):
    if len(shared.LoadDeck) == 0: return
    mute()
    if count == None: count = askInteger("Draw how many cards?", 6)
    for c in group.top(count): c.moveTo(me.hand)
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
    if len(group) == 0: return
    mute()
    if count == None: count = askInteger("Deal how many cards to table?", 5)
    for c in group.top(count): 
        c.moveToTable(x,y)

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
