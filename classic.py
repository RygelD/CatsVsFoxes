#!/usr/bin/env python3
from sys import platform as _platform
from subprocess import call
from time import sleep
import math
import sys
import random

__version__ = '0.1 Beta 9.3'


class Attack:
    def __init__(self,name,damage,sdamage,helpme,other=False):
        self.damage = damage
        self.name = name
        self.sdamage = sdamage
        self.helpme = helpme
        self.other = other
        

    def attack(self,target,starget):
        if self.other != False:
            x = eval(self.other)
        xdamage = self.damage
        xsdamage = self.sdamage
        if type(xdamage) == str:
            xdamage = eval(self.damage)
        if type(xsdamage) == str:
            xsdamage = eval(self.sdamage)
        target.lives -= (xdamage - target.berry.df + starget.berry.at)
        starget.lives -= (xsdamage - target.berry.kb)
        verb = ' did '
        tverb = ' damage to '
        if xdamage == 0:
            pxdamage = 'no'
        elif xdamage < 0:
            verb = ' healed '
            tverb = ' HP for '
            pxdamage = xdamage
        else:
            pxdamage = xdamage
        werb = ' did '
        uverb = ' damage to '
        if xsdamage < 0:
            werb = ' healed '
            uverb = ' HP for '
        xprint('\nThe attack' + verb + str(sabs(pxdamage)) + tverb + target.alias,0)
        if self.sdamage != 0:
            xprint('The attack'+ werb + str(sabs(xsdamage)) + uverb + starget.name + '\n',0)
        target.lattack = xdamage
        
class Berry:
    def __init__(self,typeo):
        self.type = typeo
        self.bst = 1
        if typeo == 'att':
            self.at = self.bst
            self.df = 0
            self.kb = 0
        elif typeo == 'def':
            self.at = 0
            self.df = self.bst
            self.kb = 0
        elif typeo == 'rec':
            self.at = 0
            self.df = 0
            self.kb = self.bst
    def change(self,typeo):
        self.type = typeo
        if typeo == 'att':
            self.at = self.bst
            self.df = 0
            self.kb = 0
        elif typeo == 'def':
            self.at = 0
            self.df = self.bst
            self.kb = 0
        elif typeo == 'rec':
            self.at = 0
            self.df = 0
            self.kb = self.bst
    def inc(self):
        self.bst += 1

    def dec(self):
        self.bst -= 1
        
class Animal:
    def __init__(self,name,attacks):
        self.name = name
        self.attacks = attacks
        self.lives = 50
        self.lattack = 0
        self.berry = Berry('def')
        self.alias = name
        self.changed = 0
        self.msg = ''
        self.helpon = True
        #self.tag = ''
        #self.ck()
    def attack(self,attack_number,target):
        print(self.name +' attacks!')
        z = self.attacks[attack_number]
        z.attack(target,self)
    #def ck(self):
     #   if self.name == 'Bingley':
      #      self.attacks = [s1,s2,s3,s4,s5]
        #elif self.name == 'Reegul-man'
         #   self.attacks = [s6,s7,s8,s9,s10]
    def get_attack(self,target):
        xprint(self.name + "'s Turn!",0)
        xprint('\nYou have ' + str(self.lives) + ' HP ('+target.alias+' did ' + str(self.lattack) + ' damage to you last turn.)',0)
        xprint(target.alias + ' has ' + str(target.lives) + ' HP left.\n\n',0)
        print('Your attacks: ')
        a = 1
        valid = []
        for i in self.attacks:
            if self.helpon:
                ending =  ': ' + i.helpme
            else:
                ending = ''
            print(' [' + str(a) + '] ' + i.name  + ending)
            valid.append(str(a))
            a += 1
        sleep(1)
        print('\n')
        while True:
            z = input('Choose your attack: ').lower()
            print('\n')
            #print('\n')
            if z in valid:
                self.attack(int(z)-1,target)
                break
            elif z == '':
                pass
            elif z == 'help':
                a = 1
                for i in self.attacks:
                    print(' [' + str(a) + '] ' + i.name + ': ' + i.helpme)
                    a += 1
            elif z == 'guide':
                print('''
GUIDE

Functions:

    alias - Change opponent's alias
    name  - Change your name
    get name - Returns your name surounded in '| '' |'
    get alias - Returns your alias surounded in '| '' |'
    get oname - Returns your opponent's name surounded in '| '' |'
    get oalias - Returns your opponent's alias surrounded in '| '' |'
    help - Tells you all your moves.
    mail - Prints and deletes any message sent by your enemy
    send - Sends a message to your enemy.
    berry - Changes the type of your berry. (offensive boost, defencive boost, recoil diminishing)
    helpon - Makes the game automaticlly display help
    helpoff - Stops the game from automaticly displaying help
    quit - Early exit
       
''')
            elif z == 'name':
                self.name = input('Enter new name: ')
                print('Name changed.')
                if self.changed == 0:
                    if input('Your oponent has not changed your alias. Change alias to new name? (y/other):') == 'y':
                        self.alias = self.name
                        print('Alias changed.')
            elif z == 'mail':
                print('Messages to you:\n' + self.msg)
                self.msg = ''
            elif z == 'send':
                send = input('Send message to opponent:\n')
                target.msg = send
            elif z == 'alias':
                a = input('Enter opponent\'s alias: ')
                if len(a) < 50:
                    target.alias = a
                    print('Opponent\'s alias changed.')
                    target.changed = 1
                else:
                    print('Alias too long, try again.')
           # elif z == 'tag':
           #     self.tag = input('Tag: ')
        #    elif z == 'dev alias' and self.tag == '-d' or self.tag == '-c':
          #      self.changed = 0
          #      print('Alias unlocked.')
            elif z == 'reset alias':
                target.alias = target.name
                print('Enemy\'s alias reverted.')
            elif z == 'get alias':
                print('| '+self.alias+' |')
            elif z == 'get name':
                print('| '+self.name+' |')
            elif z == 'get oname':
                print('| '+target.name+' |')
            elif z == 'get oalias':
                print('| '+target.alias+' |')
            elif z == 'quit':
                Clear()
                victory(target.name)
                sleep(2)
                Clear()
                sys.exit()
            elif z == 'helpon':
                self.helpon = True
                print('Help turned on.')
            elif z == 'helpoff':
                self.helpon = False
                print('Help turned off.')
            elif z == 'berry':
                x = input('Berry type - +attack/+defence/-recoil (att,def,rec): ')
                if x in ['att','def','rec']:
                    self.berry.change(x)
                    print('Berry changed.')
                else:
                    print('Input not reconised.')
                          
                
            else:
                print('Invalid option. Try again. (Note: Enter the number of your attack or \'help\' for a description of each attack or \'guide\' for more.')
            
    def turn(self,target,start=0):
        Clear()
        for j in range(3):
            xprint('Opponent\'s turn in '+str(3 - j) +' seconds',0,'-')
            sleep(1)
            Clear()
        Clear()
        a101 = input(self.name+'\'s turn. Type \'turn\' and press <Enter> to continue. ').lower()
        while a101 != 'turn':
            Clear()
            a101 = input(self.name+'\'s turn. Type \'turn\' and press <Enter> to continue. ').lower()
        Clear()
        self.get_attack(target)
        sleep(5)
def getTerminalSize():
    import os
    env = os.environ
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
        '1234'))
        except:
            return
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))
    return int(cr[1]), int(cr[0])

def sabs(value):
    try:
        return abs(value)
    except:
        return value        
a1 = Attack('Tackle',10,0,'Does 10 damage to your opponent')
a2 = Attack('Clean',0,-10,'Heals 10 HP')
a3 = Attack('Bite',15,5,'Does 15 damage to your opponent and 5 to you.')
a4 = Attack('Hiss',5,-5,'Does 5 damage and heals 5 HP')
a5 = Attack('Burrow','random.choice([-5,5,15])',0,'Either heals 5 of your opponent\'s HP or does 5 or 15 damage')
a6 = Attack('Tail Swipe','10+math.ceil(random.random()*2)',1,'Does from 10 to 12 damage to your opponent and 1 damage to you.')
a7 = Attack('Nap',0,'random.choice([-10,-5,5])','Either heals 10 HP, 5 HP or does you 5 damage')
a8 = Attack('Retaliate','starget.lattack','math.ceil(target.lattack * 1.5)','Does the same amount of damage your enemy did to you, but does 1.5 tiimes the amount of damage you did to your enemy last turn to yourself.')
a9 = Attack('Desperate Hit','random.randint(0,15)',0,'Does a random amount of damage to your opponent between 0 and 15')
a10 = Attack('Desperate Lick',0,'random.randint(0,10)*-1','Heals a random amount of HP between 0 and 10')
a11 = Attack('Grow Berry',0,0,'Increases your berry\'s power by 1','starget.berry.inc()')
a12 = Attack('Lucky Hit','random.randint(1,6)*2',0,'Rolls a dice, and multiplies the result by 2')
a13 = Attack('Double Hit','random.randint(1,6) + random.randint(1,6)',0,'Rolls two dice and adds them together')
a14 = Attack('Repeated Hit','(random.randint(1,6) + random.randint(1,6)+random.randint(1,6) + random.randint(1,6)) / 2',0,'Rolls four dice and divides the sum by 2')
a15 = Attack('Shrihk Berry',0,0,'Shrinks your opponent\'s berry power by 1','target.berry.dec()')
#s1 = Attack('Floppy Ears!',15,0,'','print(\'FLOP FLOP FLOP!!!\')')
#s2 = Attack('WAGGY TAIL!',0,-20,'','print(\'THUMP THUMP THUMP!!!\')')
#s3 = Attack('LLLIIICCCKKKYYY TTTTOOOOUUUNNNGGGEEE!',10,-10,'','print(\'SLUUUURP SLUUURP SLUUURP!!!\')')
#s4 = Attack('Sniffy NOSE!','random.choice[0,0,0,50]',0,'')
#s5 = Attack('Take a nap...',0,0,'')

setb = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13]
def getn(n):
    t = []
    for i in range(n):
        x = random.choice(setb)
        while x in t:
            x = random.choice(setb)
        t.append(x)
    return t
def Clear(): 
    tmp = call('clear',shell=True)
def xprint(stuff,st=0.05,fill=' '):
    columns = getTerminalSize()[0]
    c = ''
    for i in stuff:
        if i != '\n':
            c += i
        else:
            sleep(st)
            print(c.center(columns,fill))
            c = ''
    if c != '':
        sleep(0.05)
        print(c.center(columns,fill))
def start():
    xprint('Cats vs Foxes\n2019 Rygel Dagenais\nversion '+__version__+'\n',0)
    xprint('''
 CCCC   AAA   TTTTT   SSS     V   V   SSS 
CC     A   A    T    S   S    V   V  S   S
C      A   A    T    S        V   V  S    
C      AAAAA    T     SSS     V   V   SSS 
C      A   A    T        S     V V       S
CC     A   A    T    S   S     V V   S   S
 CCCC  A   A    T     SSS       V     SSS 

FFFFF   OOO   X   X  EEEEE   SSS 
F      O   O   X X   E      S   S
F      O   O   X X   E      S    
FFF    O   O    X    EEEE    SSS 
F      O   O   X X   E          S
F      O   O   X X   E      S   S
F       OOO   X   X  EEEEE   SSS 
 ____________________________________________ 
|  ____                      ___       ___   |
| |    \       |            /   \     /   \  |
| |    |      _|_          |     |         | |
| |____/   _   |            \___/|      --<  |
| |     \ / \  |  / \|           |         | |
| |     | ---  | |   |           | ..      | |
| |_____/ \__  |  \_/|      \____/ .. \___/  |
|____________________________________________|
''')
def rstart(mode=1):
    for i in range(3):
        print('Game starting in '+str(3-i)+' second(s).')
        sleep(1)
        if mode == 0:
            Clear()
            start()
            print('Player 1\'s name: ' + zz)
            print('Player 2\'s name: ' + zy)
if len(sys.argv) == 2: 
    rstart(sys.argv[1])
else:
    rstart()


class SinglePlayerFight:
    def __init__(self,pp,pp2):
        trig = False
        pp.turn(pp2,start=1)
        pp.helpon = False
        pp2.turn(pp)
        pp2.helpon = False
        while trig == False:            
            if pp2.lives <= 0:
                victory(pp.name)
                trig == True
                break
            elif pp.lives <= 0:
                victory(pp2.name)
                trig == True
                break
            pp.turn(pp2)
            if pp.lives <= 0:
                victory(pp2.name)
                trig == True
                break
            elif pp2.lives <= 0:
                victory(pp.name)
                trig == True
                break
            pp2.turn(pp)
def victory(winner):
    Clear()
    columns = getTerminalSize()[0]
    print(' WINNER '.center(columns,'*'))
    print('\n')
    winnertext = winner + ' wins!'
    print(winnertext.center(columns,' '))
    print('\n\n')
    print('Congratulations!'.center(columns,(' ')))
    print('\n\n\n\n')

def start_game():
    Clear()
    global setb
    start()
    zz = input('Player 1\'s name: ')
    zy = input('Player 2\'s name: ')
    while zy == zz:
        print('That username is already taken by Player 1.')
        zy = input('Player 2\'s name: ')
    p1 = Animal(zz,getn(6))
    p2 = Animal(zy,getn(6))
    Clear()
    a = SinglePlayerFight(p1,p2)  
    
    
while True:
    start_game()
    time.sleep(7)

        

'''
Changelog version 0.1.9.3:
    Bug fixes
Changelog version 0.1.9.2:
    Removed easter eggs and tags (temp.)
    Changed looks of some menus and opening screen
    Cleaned up code
    Lots of new attacks
    Moved most titles to the centre of the screen

'''



