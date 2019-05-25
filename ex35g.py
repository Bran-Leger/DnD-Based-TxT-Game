from sys import exit
import random

# Dice rolls and randomizers
def d20(bonus):
    for x in range(1):
        print(random.randint(1, 20) + bonus)

def d8(bonus):
    for x in range(1):
        print(random.randint(1, 8) + bonus)

# Player Character's Stats
stats = {
    'vit': 10,
    'str_score': 0,
    'dex_score': 0,
    'cha_score': 0,
    'int_score': 0,
    "ac": 10,
    'init': 20,
    "atckbonus": 0,
    'atck': 0

}
name = None

def health_bar():
    health = stats['vit']
    print(health * '\u2661')

class Role(object):



    def __init__(self, Class):
        self.Class = Class

    def class_choice(self):
        if self.Class == 'Barbarian':
            print("You chose Barbarian")
            stats['str_score'] = 5
            stats['vit'] += 10
            stats['ac'] += 5

        elif self.Class == 'Rogue':
            print("You chose Rogue")
            stats['dex_score'] += 5
            stats['ac'] += 3
            stats['init'] += 5

class Encounter():

    def __init__(self, monster, vit, ac, d, init):
        self.monster = monster
        self.vit = vit
        self.ac = ac
        self.d = d
        self.init = init
        self.alive = True

    def fightscene(self):
        if self.monster == 'Goblin':
            print("The stubby Goblin appears to want to throw hands")
            print('You ready yourself for combat.')

        while self.alive == True:

            if self.vit <= 0:
                print("With a finishing blow you deal a fatal wound, killing the {} where it stands.".format(self.monster))
                self.alive == False
                break

            elif self.vit >= 1:
                if initiative(self.init) == "monstart":
                    print(f'The {self.monster} strikes with blinding speed and swings at you first.')

                elif initiative(self.init) == 'pcstart':
                    print(f'You quickly draw your blade and get the first swing on the {self.monster}.')

def combat():
    combatphrases = {
    'monhitpc': 'The vile creature slashes your chest. With the taste of blood in your mouth you ready yourself for the next attack.',
    'monmisspc': 'The creature thrusts its blade, but it finds no purchase. You deftly dodge out the way.',
    'pchitmon': "You swing your sword and it finds purchase in the creature's belly. But the monster still stands. You flick the blood off and stand firm.",
    'pcmissmon': "You strike at the creature but it ducks out the way. It cackles as you ready your sword again."
                }
    if initiative(self.init) == "monstart":
        print(f'The {self.monster} strikes with blinding speed and swings at you first.')

    elif initiative(self.init) == 'pcstart':
        print(f'You quickly draw your blade and get the first swing on the {self.monster}.')


def pcattacksmon():
    atck_roll = d20(stats['atck'])
    print('Hit the monster with "attack".')
    x = input("> ")
    if x == 'attack':
        if atck_roll >= monac:
            print(combatphrases['pchitmon'])
            monvit - d8(str_score)
        elif atck_roll < monac:
            print(combatphrases['pcmissmon'])
    else:
        print("Quick hit the monster!")







def initiative(moninit):
    if moninit <= stats['init']:
        return 'monstart'
    elif moninit >= stats['init']:
        return 'pcstart'
    else:
        return 'pcstart'



Goblin = 'Goblin', 7, 8, random.randint(1, 3)

def pcdamage(d):
    for x in range(1):
        print(random.randint(d + 1))

def gobdamage(d):
    pass


def goblinfight():
    print('Fight a goblin')
    gob_vit = 7
    gob_ac = 8
    goc_d = damage(3)
    gob_init = d20(0)
    if gob_init >= stats['init']:
        print('The goblin goes first.')



class Monster():
    def __init__(self, type, vit, ac, d):
        self.type = type
        self.vit = vit
        self.ac = ac
        self.d = d






def freedom(reason):
    print(reason,  "Nice work.")

def prologue():
    global name
    print("""This is my first attempt at a choose-your-own-adventure style
game. This is a game of choices and chance. Certain decisions and actions
will either aid your journey or haunt you. Choose wisely and play to your attributes.\n\n
******PROLOGUE******\n\n
You awake from a dream. You feel motion and see different shades and hues of grey but
you can't seem to make out what's in front of you. Your eyes are being covered by something.
You try and struggle but your hands and feet are bound. You would be worried about the situation
but your mind seems to focus on your past whereabouts and decisions.


!?.................You can't remember anything.


You decide to start with the basics to jog your memory.

Try and recall your name.""")
    name = input("> ")
    print(f"'{name}...Ya...{name} is my name.'\n\n")
    print("You've got your name down, but you're still hazy about the details of your life. \nWhat was your role in society? What were your skills, attributes, and flaws?")
    print("\n\nChoose your class\n\n**********Barbarian: Born on a battlefield to a corpse and taken in by a traveling band of mercenaries, your life was embroiled in unending combat. The only way you survived such adversity was by forsaking your humanity and releasing unbridled primal rage, ripping apart all who lay in your path. The torrent of relentless punishment from the countless battles you've endured has left you with monsterous strength, an inhuman tolerance to torment, and an unquenchable lust for blood. Your muscles ripple like the waves as you shatter arrows with your bare chest. Armor would only impede your \n\nPROS: High Strength, Decent AC, High Vitality, Half Damage from all sources\n\nCONS: No Armor, Lower Intelligence\n\n")
    print("**********Rogue: Born poor and on the streets, you scraped a living together by stealing what you could. With age you moved onto stealing big-ticket items. This got the attention of the local Thieves Guild, and they decided to take you under their wing. Through their guidance you learned how to hide your presence by sticking to the shadows, how to pick various locks of every complexity from simple doors and windows to intricate safes and vaults, and sharpening your agility on your feet and in battle. ")

    class_select = input("> ")

    Role(class_select).class_choice()

    print(stats['str_score'])
    print(f"Alright {name}, here's how your story starts.")

    start()

def start():
    print("""You abruptly wake up in a cold, dark, dungeon.
You have no memory of how you got here, but you hear something coming.
You are appear to be in a holding cell. What do you do?""")
    print("1.   Lou Ferrigno the bars")
    print("2.   Try and pick the lock with some metal scraps lying around")
    print("3.   Accept your fate")
    health_bar()
    d20(stats['init'])
    choice = input("> ")

    if choice == "1":
        print("""You flex your suddenly rippling pair of biceps
and to your astonishment the bars bend enough for you to slip through!\n""")
        stats['str_score'] += 1
        stage_2()

    elif choice == "2":
        print("You pick the lock with suddenly deft fingers. You slip out none the wiser.")
        stats['dex_score'] += 1
        stage_2()

    elif choice == "3":
        death()
    else:
        print("Huh? Let's try this again.")
        start()

def stage_2():
    print("The noises get louder beyond the corner wall. You prepare for an encounter.\n")
    print("The adrenaline surges through your body as you decide your next move.\n\n")
    print("1.   Ready yourself to strike whatever comes into view.")
    print("2.   Dive behind some boxes and try to sneak past it.")
    print("3.   Try and reason with your captors.")

    choice = input("> ")

    if choice == "1" and stats['str_score'] >= 1:
        print("""A goblin turns the corner and walks right into you.
Before he can react you grind him into a pulp with unrelenting fury.""")
        stats['str_score'] += 1
        exit(0)

    elif choice == "1" and stats['str_score'] < 1:
        print("""A goblin turns the corner and walks right into you.
You try your best to pummel him but you aren't strong enough.""")
        dead("The goblin stabs you to death.")

    elif choice == "2" and stats['dex_score'] >= 1:
        print("""You blend behind the boxes like a shadow.
A goblin turns the corner and walks right by you, unaware of your presence.""")
        stats['dex_score'] += 1
        exit(0)

    elif choice == "2" and stats['dex_score'] < 1:
        print("""A goblin turns the corner and sees your foot slipping out behind the boxes.
You weren't as stealthy as you thought.""")
        dead("The goblin stabs you to death.")

    else:
        print("A foolish decision. A goblin turns the corner and stabs you before you can do anything.")
        dead("")

def dead(reason):
        print(reason, "Try again.")
        exit(0)

prologue()
