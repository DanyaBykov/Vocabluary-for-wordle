"""Wordle by Danya Bykov"""

import random
import sys
import urllib.request

GREEN = '\033[92m'
YELLOW = '\033[93m'
END = '\033[0m'

def main():
    """
    This is the main function
    """
    print('This is the game called Wordle. If you want to play type |Y|')
    start_ans = str(input('>>> '))
    if start_ans in ('Y', 'y', '|Y|','|y|'):
        print('Do you want to read the rules |Y| or |N|?')
    else:
        sys.exit()
    rules_ans = str(input('>>> '))
    rules(rules_ans)
    print('Type the first word below')
    checker(randomise())

def checker(org_word:str):
    """
    This is the function that will compare the word you need to guess and input of a player.
    """
    output_word = ''
    url = 'https://raw.githubusercontent.com/DanyaBykov/Wordle_game/main/vocab.txt'
    with urllib.request.urlopen(url) as file_voc:
        voc = file_voc.read()
        voc = voc.decode('utf-8')
        voc_lst = voc.split(' ')
    for i in range(6):
        if i !=0:
            print('Type the next word')
        guess = str(input('>>> '))
        guess_u = guess.upper()
        while True:
            if guess_u not in voc_lst:
                print('The word is not in vocabluary. Please type correct word.')
                guess = str(input('>>> '))
                guess_u = guess.upper()
            else:
                break
        guess_u = guess.upper()
        count = 0
        for j in range(5):
            if org_word[j] == guess_u[j]:
                output_word += GREEN + guess_u[j] +END
                count +=1
            elif guess_u[j] in org_word:
                output_word += YELLOW + guess_u[j] +END
            else:
                output_word += guess_u[j]
        output_word += '\n'
        print(output_word)
        if count == 5:
            if i == 1:
                print('Congratulations you have won the game in 1 word.')
            else:
                print('Congratulations you have won the game in', i+1 ,'words.')
            sys.exit()
    print('You lost. The word was: '+org_word)
    sys.exit()

def rules(answer:str) -> str:
    """
    str -> str
    This function returns rules of Wordle
    """
    rule = "Here are the rules: \n\
1. You have six tries to guess the five-letter Wordle. \n\
2. Type in your guess and submit your word by hitting the “enter” key. \n\
3. The color of the letters will change after you submit your word. \n\
A yellow letter indicates that you picked the right letter but it's in the wrong spot. \n\
The green letter indicates that you picked the right letter in the correct spot. \n\
The white letter indicates that the letter you picked is not included in the word at all. \n\
4. Continue until you solve the Wordle or run out of guesses. Good luck!"
    if answer in ('Y', 'y', '|Y|','|y|'):
        print(rule)

def randomise() -> str:
    """
    This is the function that will give the random word from a list
    """
    list_of_words = ['ABBEY','ABOUT','ABOVE','ABYSS','ACRID','ACUTE','ADMIT','ADOBE','ADOPT',
                     'ADORE','AGAIN','AGILE','AGONY','AGREE','AHEAD','ALBUM','ALIEN','ALIKE',
                     'ALLOW','ALONE','ALOUD','ALPHA','ALTAR','ALTER','AMBER','ANGEL','ANGER',
                     'ANGRY','ANODE','ANTIC','APPLE','APPLY','APRON','APTLY','ARBOR','ARGUE',
                     'AROMA','ASIDE','ASKEW','ASSET','ATONE','AUDIO','AUDIT','AWAIT','AWAKE',
                     'AWFUL','AXIOM','AZURE','BADGE','BADLY','BAGEL','BAKER','BARGE','BASIC',
                     'BATHE','BEACH','BEAST','BEEFY','BEGIN','BEING','BELLY','BELOW','BENCH',
                     'BERET','BIOME','BIRCH','BIRTH','BLACK','BLAME','BLAND','BLEED','BLEEP',
                     'BLOWN','BLUFF','BLUSH','BOOST','BOOZE','BRAID','BRAKE','BRAVE','BREAD',
                     'BREAK','BRIAR','BRING','BROKE','BROOM','BRUSH','BUGGY','BULLY','BUNCH',
                     'CACAO','CACHE','CANNY','CANOE','CARAT','CARGO','CARRY','CAROL','CATCH',
                     'CATER','CHAMP','CHANT','CHARM','CHART','CHEAT','CHEEK','CHEST','CHIEF',
                     'CHILL','CHOIR','CHOKE','CHUNK','CIGAR','CIVIC','CLASS','CLEAN','CLEAR',
                     'CLERK','CLICK','CLING','CLOCK','CLOSE','CLOTH','CLOWN','COACH','COAST',
                     'COCOA','COLON','COMET','COMMA','CORNY','COULD','COUNT','COWER','CRAMP',
                     'CRANE','CRANK','CRAVE','CRAZY','CREDO','CRIME','CRIMP','CROAK','CROSS',
                     'CRUMB','CRUST','CURLY','DANCE','DEATH','DEBUG','DENIM','DEPOT','DEPTH',
                     'DIGIT','DINER','DISCO','DODGE','DONOR','DONUT','DOUBT','DOZEN','DRAIN',
                     'DREAM','DRINK','DRIVE','DROLL','DUTCH','DWARF','EARTH','EJECT','ELDER',
                     'EMAIL','EMPTY','ENEMA','ENJOY','ENTER','EPOXY','EQUAL','ERODE','ERROR',
                     'ESSAY','ETHIC','EVADE','EVERY','EXACT','EXCEL','EXIST','EXTRA','FAULT',
                     'FAVOR','FEAST','FERRY','FEWER','FIELD','FIFTY','FIRST','FISHY','FIXER',
                     'FJORD','FLAIR','FLASK','FLESH','FLICK','FLIRT','FLOAT','FLOOD','FLOOR',
                     'FLORA','FLOSS','FLUFF','FLYER','FOCUS','FOGGY','FORTH','FOUND','FRAME',
                     'FRANK','FRESH','FRONT','FROST','FROZE','GAMER','GAMMA','GAUZE','GECKO',
                     'GHOUL','GIANT','GIRTH','GLASS','GLOOM','GLORY','GLOVE','GOLEM','GONER',
                     'GOOSE','GRADE','GRAND','GRATE','GREAT','GREET','GRIEF','GROUP','GRAVE',
                     'GUARD','GUEST','HAIRY','HAPPY','HATCH','HATER','HEART','HEIST','HELLO',
                     'HINGE','HOBBY','HOMER','HORSE','HOTEL','HOUND','HUMAN','HUMID','HUMOR',
                     'HURRY','HUTCH','HYPER','IGLOO','INDEX','INERT','INPUT','INTER','IONIC',
                     'IRONY','ITCHY','IVORY','JAZZY','JOKER','JUDGE','KARMA','KAYAK','KEBAB',
                     'KHAKI','KIOSK','KNEEL','KNOCK','KOALA','LABEL','LABOR','LATTE','LEAFY',
                     'LEAVE','LEMON','LIGHT','LIVER','LOGIC','LOSER','LOVER','LOYAL','LUCKY',
                     'LUNAR','LYING','MADAM','MAGIC','MAGMA','MAIZE','MAJOR','MANLY','MAPLE',
                     'MARCH','MARRY','MAYBE','MEDAL','MERRY','METAL','METRO','MIMIC','MODEL',
                     'MOIST','MONEY','MONTH','MOOSE','MOTOR','MOTTO','MOUNT','MOUSE','MOVIE',
                     'MUSIC','NAIVE','NANNY','NASTY','NEEDY','NIGHT','NINTH','NYMPH','OCEAN',
                     'OLDER','OLIVE','ONION','OPERA','OTHER','PANEL','PANIC','PAPER','PARTY',
                     'PATTY','PAUSE','PEACE','PEACH','PERKY','PHASE','PHOTO','PICKY','PILOT',
                     'PINKY','PIXIE','PLANT','PLATE','PLAZA','POINT','POKER','POLKA','POUND',
                     'POWER','PRICK','PRIDE','PRIME','PRIMO','PRINT','PRIZE','PROXY','PURGE',
                     'QUEST','QUICK','QUIET','QUOTE','RADIO','RAINY','RAMEN','RANCH','RANGE',
                     'RATIO','REACT','REBUS','RECAP','RENEW','REPAY','RETRO','REVEL','RHINO',
                     'RHYME','RIGHT','RIVAL','ROBIN','ROBOT','ROCKY','RODEO','ROGUE','ROOMY',
                     'ROUGE','ROUND','ROYAL','RUSTY','SAINT','SALAD','SALSA','SCARE','SCARF',
                     'SCOUT','SCRUB','SEDAN','SERVE','SEVER','SHAKE','SHALL','SHAME','SHARD',
                     'SHINE','SHOWN','SKILL','SKIMP','SKIRT','SLEEK','SLOTH','SMART','SMASH',
                     'SMILE','SNACK','SNAIL','SNAKY','SNEAK','SOGGY','SOLAR','SOLVE','SONIC',
                     'SOUND','SPACE','SPELL','SPEND','SPICE','SPICY','SPIKE','SPOKE','SPRAY',
                     'SQUAD','SQUAT','STAFF','STAGE','STAIR','STAND','START','STEED','STICK',
                     'STINK','STOCK','STONE','STOOL','STORE','STORY','STOVE','STRAP','STRAW',
                     'STUDY','STYLE','SUGAR','SURER','SWEAT','SWEEP','SWEET','SWIRL','SYRUP',
                     'TASTE','TASTY','TEASE','THEIR','THEME','THERE','THIEF','THIRD','THOSE',
                     'THUMB','TIGER','TIPSY','TODAY','TONIC','TORSO','TOTEM','TOUGH','TOXIC',
                     'TRACE','TRAIN','TRASH','TREAT','TREND','TROLL','TRUTH','TWICE','ULTRA',
                     'UNDER','UNFIT','UNIFY','UNITE','UNTIE','UNZIP','UPSET','USAGE','USING',
                     'USUAL','VAGUE','VALID','VENOM','VIRAL','VODKA','VOICE','WACKY','WASTE',
                     'WATCH','WHACK','WHALE','WHEEL','WHERE','WHILE','WHOOP','WINDY','WOKEN',
                     'WORLD','WORRY','WORSE','WRITE','WRONG','WROTE','YACHT','YOUTH','ZESTY']
    rand = random.choice(list_of_words)
    return rand

if __name__ == "__main__":
    main()
