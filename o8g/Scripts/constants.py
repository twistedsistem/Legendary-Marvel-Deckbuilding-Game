coreHeroList = ['Black Widow','Captain America','Cyclops','Deadpool','Emma Frost','Gambit','Hawkeye','Hulk','Iron Man','Nick Fury','Rogue','Spider-Man','Storm','Thor','Wolverine']
coreVillainList = ['Brotherhood','Enemies of Asgard','Hydra','Masters of Evil','Radiation','Skrulls','Spider Foes']
coreHenchmenList = ['Doombot Legion','Hand Ninjas','Savage Land Mutants','Sentinel']
coreMasterMindList = ['Dr. Doom','Loki','Magneto','Red Skull']
soloSchemeList = ['Midtown Bank Robbery','Portals to the Dark Dimension',"Replace Earth's Leaders with Killbots",'Secret Invasion of the Skrull Shapeshifters','The Legacy Virus','Unleash the Power of the Cosmic Cube']
allSchemeList  = ['Midtown Bank Robbery','Negative Zone Prison Breakout','Portals to the Dark Dimension',"Replace Earth's Leaders with Killbots",'Secret Invasion of the Skrull Shapeshifters','Super Hero Civil War','The Legacy Virus','Unleash the Power of the Cosmic Cube']

staticPositions = { # A dictionary which holds the static coordinates for specific table placement.
	'HQ':{# Hero HQ positions with 1 being the right most hero
			'1':{'x':256,'y':164},
			'2':{'x':98,'y':164},
			'3':{'x':-60,'y':164},
			'4':{'x':-218,'y':164},
			'5':{'x':-376,'y':164}
		},
	'CS':{# CityScape positions
			'sewers':{'x':256,'y':-76},
			'bank':{'x':98,'y':-76},
			'rooftops':{'x':-60,'y':-76},
			'streets':{'x':-218,'y':-76},
			'bridge':{'x':-376,'y':-76}
		}
	}

gameSetupRule = { # A dictionary which holds how many different heroes, villains, henchmen groups along with how many bystander and masterstrike cards that should be placed in the Villains Deck
	'1':{
			'heroes':3,
			'villains':1,
			'henchmen':{'groupCount':1,'cardCount':3},#the henchmen key a nested dictionary which holds how many henchmen groups and how many cards of each group should be added to the Villain Deck
			'bystander':1,
			'masterStrike':1,
			'Midtown Bank Robbery':{'schemeTwist':8,'bystander':11},
			'Negative Zone Prison Breakout':{'schemeTwist':0,'bystander':0},
			'Portals to the Dark Dimension':{'schemeTwist':7,'bystander':0},
			"Replace Earth's Leaders with Killbots":{'schemeTwist':5,'bystander':17},
			'Secret Invasion of the Skrull Shapeshifters':{'schemeTwist':8,'bystander':0},
			'Super Hero Civil War':{'schemeTwist':0,'bystander':0},
			'The Legacy Virus':{'schemeTwist':8,'bystander':0},
			'Unleash the Power of the Cosmic Cube':{'schemeTwist':8,'bystander':0}
		},
	'2':{
			'heroes':5,
			'villains':2,
			'henchmen':{'groupCount':1,'cardCount':10},#the henchmen key a nested dictionary which holds how many henchmen groups and how many cards of each group should be added to the Villain Deck
			'bystander':2,
			'masterStrike':5,
			'Midtown Bank Robbery':{'schemeTwist':8,'bystander':10},
			'Negative Zone Prison Breakout':{'schemeTwist':8,'bystander':0},
			'Portals to the Dark Dimension':{'schemeTwist':7,'bystander':0},
			"Replace Earth's Leaders with Killbots":{'schemeTwist':5,'bystander':16},
			'Secret Invasion of the Skrull Shapeshifters':{'schemeTwist':8,'bystander':0},
			'Super Hero Civil War':{'schemeTwist':8,'bystander':0},
			'The Legacy Virus':{'schemeTwist':8,'bystander':0},
			'Unleash the Power of the Cosmic Cube':{'schemeTwist':8,'bystander':0}
		},
	'3':{
			'heroes':5,
			'villains':3,
			'henchmen':{'groupCount':1,'cardCount':10},#the henchmen key a nested dictionary which holds how many henchmen groups and how many cards of each group should be added to the Villain Deck
			'bystander':8,
			'masterStrike':5,
			'Midtown Bank Robbery':{'schemeTwist':8,'bystander':4},
			'Negative Zone Prison Breakout':{'schemeTwist':8,'bystander':0},
			'Portals to the Dark Dimension':{'schemeTwist':7,'bystander':0},
			"Replace Earth's Leaders with Killbots":{'schemeTwist':5,'bystander':10},
			'Secret Invasion of the Skrull Shapeshifters':{'schemeTwist':8,'bystander':0},
			'Super Hero Civil War':{'schemeTwist':8,'bystander':0},
			'The Legacy Virus':{'schemeTwist':8,'bystander':0},
			'Unleash the Power of the Cosmic Cube':{'schemeTwist':8,'bystander':0}
		},
	'4':{
			'heroes':5,
			'villains':3,
			'henchmen':{'groupCount':2,'cardCount':10},#the henchmen key a nested dictionary which holds how many henchmen groups and how many cards of each group should be added to the Villain Deck
			'bystander':8,
			'masterStrike':5,
			'Midtown Bank Robbery':{'schemeTwist':8,'bystander':4},
			'Negative Zone Prison Breakout':{'schemeTwist':8,'bystander':0},
			'Portals to the Dark Dimension':{'schemeTwist':7,'bystander':0},
			"Replace Earth's Leaders with Killbots":{'schemeTwist':5,'bystander':10},
			'Secret Invasion of the Skrull Shapeshifters':{'schemeTwist':8,'bystander':0},
			'Super Hero Civil War':{'schemeTwist':5,'bystander':0},
			'The Legacy Virus':{'schemeTwist':8,'bystander':0},
			'Unleash the Power of the Cosmic Cube':{'schemeTwist':8,'bystander':0}
		},
	'5':{
			'heroes':6,
			'villains':4,
			'henchmen':{'groupCount':2,'cardCount':10},#the henchmen key a nested dictionary which holds how many henchmen groups and how many cards of each group should be added to the Villain Deck
			'bystander':12,
			'masterStrike':5,
			'Midtown Bank Robbery':{'schemeTwist':8,'bystander':0},
			'Negative Zone Prison Breakout':{'schemeTwist':8,'bystander':0},
			'Portals to the Dark Dimension':{'schemeTwist':7,'bystander':0},
			"Replace Earth's Leaders with Killbots":{'schemeTwist':5,'bystander':6},
			'Secret Invasion of the Skrull Shapeshifters':{'schemeTwist':8,'bystander':0},
			'Super Hero Civil War':{'schemeTwist':5,'bystander':0},
			'The Legacy Virus':{'schemeTwist':8,'bystander':0},
			'Unleash the Power of the Cosmic Cube':{'schemeTwist':8,'bystander':0}
		}
}