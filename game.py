import random
import shelve
import sys

death = ''
class Postac:
    def __init__(self):
        self.r = ''
        self.lvl = 1
        self.dmg = 0
        self.life = 0
        self.si = 0
        self.int = 0
        self.wit = 0
        self.zre = 0
        self.unik = 0
        self.exp = 0
        self.bron = {'n': '', 'd': 0}
        self.zbroja = {'n': '', 'o': 0}
        self.tarcza = {'n': '', 'o': 0}
        self.mana = 0
        self.czary = []
    def stworz(self, rasa, si=0, inte=0, wit=0, zre=0, unik=0):
        global bohater
        Postac.__init__(bohater)
        self.r = rasa
        self.si = si
        self.int = inte
        self.wit = wit
        self.zre = zre
        self.unik = unik
        self.mana = 5*inte
        self.czary.append({'n': 'Kula ognia', 'o': 6*inte, 'km': 5})
    def rasa(self):
        a = input('''Wybierz rasę swojej postaci:
Elf - Mag posiadający wysoką inteligencję oraz duże możliwości uniku. Najlepiej włada katalizatorem zaklęć.
Krasnolud - Wojownik o dużej sile i witalnośći. Najlepiej włada mieczem.
Człowiek - Strzelec o wysokeij zręczności i mistrzowskich zdolnościach uniku. Najlepiej włada łukiem.
''')
        if a[0] in ('e', 'E'):
            self.stworz('Elf', 0, 5, 3, 1, 2)
        elif a[0] in ('K', 'k'):
            self.stworz('Krasnolud', 5, 0, 4, 0, 1)
        elif a[0] in ('C', 'c'):
            self.stworz('Człowiek', 1, 1, 4, 6, 3)
    def zbroja(self, n, o):
        self.zbroja['n'] = n
        self.zbroja['o'] = o
    def bron(self, n, d):
        self.bron['n'] = n
        self.bron['d'] = d
    def tarcza(self, n, o):
        self.tarcza['n'] = n
        self.tarcza['o'] = o
    def showStats(self):
        print('''
Poziom: {0}
Ilość doświadczenia: {1}
Rasa: {2}
Siła: {3}
Witalność: {4}
Zręczność: {5}
Inteligencja: {6}
Unik: {15}
Obrażenia: {7}
Życie: {8}
Mana: {16}
Broń: {9} o obrażeniach {10}
Zbroja: {11} o obronie {12}
Tarcza: {13} o obronie {14}
    '''.format(self.lvl, self.exp, self.r, self.si, self.wit, self.zre, self.int, self.dmg, self.life, self.bron['n'],
               self.bron['d'], self.zbroja['n'], self.zbroja['o'], self.tarcza['n'], self.tarcza['o'], self.unik, self.mana))
    def update(self):
        self.life = (self.lvl * 50) + (self.wit * 10) + (2.5 * (self.tarcza['o'] + self.zbroja['o']))
        self.mana = 5*self.int
        if self.r == 'Elf':
            if self.bron['n'] == 'katalizator zaklęć':
                self.dmg = self.int * 5 + self.lvl * 2 + self.bron['d'] * 1.5
            else:
                self.dmg = self.int * 5 + self.lvl * 2 + self.bron['d'] * 0.5
        elif self.r == 'Człowiek':
            if self.bron['n'] == 'łuk':
                self.dmg = self.zre * 5 + self.lvl * 2 + self.bron['d'] * 1.5
            else:
                self.dmg = self.zre * 5 + self.lvl * 2 + self.bron['d'] * 0.5
        else:
            if self.bron['n'] == 'miecz':
                self.dmg = self.si * 5 + self.lvl * 2 + self.bron['d'] * 1.5
            else:
                self.dmg = self.si * 5 + self.lvl * 2 + self.bron['d'] * 0.5
    def lvl_up(self):
        if self.exp > self.lvl * 1500:
            self.lvl += 1
            print('Gratulacje udało Ci się zdobyć poziom:', bohater.lvl)
            stat = input('''Wybierz jaką statystykę chcesz rozwinąć o 1 punkt:
Witalność: {0}
Zręczność: {1}
Inteligencja: {2}
Siła: {3}
Unik: {4}
'''.format(self.wit, self.zre, self.int, self.si, self.unik))
            if stat[0] in ('S', 's'):
                self.si += 1
            elif stat[0] in ('Z', 'z'):
                self.zre += 1
            elif stat[0] in ('I', 'i'):
                self.int += 1
            elif stat[0] in ('W', 'w'):
                self.wit += 1
    def dodaj_zaklecie(self):
        if self.lvl == 4:
            bohater.czary.append({'n': 'Leczenie', 'o': bohater.life/6, 'km': 2})
bohater = Postac()
class Przeciwnik:
    def __init__(self):
        self.life = random.randint(80, (bohater.lvl*20+100))
        self.dmg = random.randint(10, (bohater.lvl*10+20))
        self.exp = random.randint(50, (bohater.lvl*10 + 100))
        self.rodzaj = random.choice(['orka', 'ogra', 'pająka', 'szkieleta'])
    def walka(self):
        global death
        obr = bohater.dmg
        while (self.life > 0 and bohater.life > 0):
            stan = input('''Co chcesz zrobić:
    1. Atakować?
    2. Użyć magii? ''')
            if stan in ('1', 'a', 'A'):
                #print('Życie przeciwnika {0}'.format(self.life))
                #print('Twoje życie {0}'.format(bohater.life))
                a = random.randint(1, (1000/bohater.unik))
                if a % 3 == 0:
                    print('Życie {0} wynosi {1}'.format(self.rodzaj,self.life))
                    self.life -= bohater.dmg
                    #bohater.life -= prze1.dmg
                    print('Udało Ci się uniknąć ataku przeciwnika.')
                else:
                    print('Życie {0} wynosi {1}'.format(self.rodzaj, self.life))
                    self.life -= bohater.dmg
                    bohater.life -= self.dmg
                    print('Twoje życie {0} oraz mana {1}'.format(bohater.life, bohater.mana))
                if self.life < 0:
                    print('Pokonałeś przeciwnika, zyskujesz {0} doświadczenia'.format(self.exp))
                    bohater.exp += self.exp
                    #prze1.brak()
                    #przeciwnik1 = {'life': 0, 'dmg': 0, 'exp': 0}
                    break
                elif bohater.life <= 0:
                    print('''
UMARŁEŚ!
    ''')
                    death = 'dead'
                    break
                else:
                    continue
            elif stan in ('2', 'u', 'U'):
                print('Dostępne czary:')
                licz = 1
                for czar in bohater.czary:
                    print(licz, '. ', czar['n'], ', obrażenia: ', czar['o'], ', koszt many: ', czar['km'], sep='')
                    licz+=1
                czar = int(input('Wybierz numer czaru, który chcesz użyć: '))
                czar-=1
                a = random.randint(1, (1000 / bohater.unik))
                if bohater.czary[czar]['n'][0:1] in ('L', 'l'):
                    print('Użyłeś zaklęcia leczącego. Twoje życie zwiększyło się o {0}'.format(bohater.czary[czar]['o']))
                    bohater.life += bohater.czary[czar]['o']
                    bohater.mana -= bohater.czary[czar]['km']
                    print('Twoje życie {0} oraz mana {1}'.format(bohater.life, bohater.mana))
                else:
                    if a % 3 == 0 and a % 2 == 0 and a % 5 == 0:
                        print('Masz pecha i źle użyłeś zaklęcia. Zadałeś sobie {0} obrażeń'.format(bohater.czary[czar]['o']))
                        bohater.life -= bohater.czary[czar]['o']
                        print('Twoje życie {0} oraz mana {1}'.format(bohater.life, bohater.mana))
                    if a % 3 == 0:
                        print('Życie {0} wynosi {1}'.format(self.rodzaj, self.life))
                        self.life -= bohater.czary[czar]['o']
                        bohater.mana -= bohater.czary[czar]['km']
                        # bohater.life -= prze1.dmg
                        print('Udało Ci się uniknąć ataku przeciwnika.')
                    else:
                        print('Życie {0} wynosi {1}'.format(self.rodzaj, self.life))
                        self.life -= bohater.czary[czar]['o']
                        bohater.mana -= bohater.czary[czar]['km']
                        bohater.life -= self.dmg
                        print('Twoje życie {0} oraz mana {1}'.format(bohater.life, bohater.mana))
                    if self.life < 0:
                        print('Pokonałeś przeciwnika, zyskujesz {0} doświadczenia'.format(self.exp))
                        bohater.exp += self.exp
                        # prze1.brak()
                        # przeciwnik1 = {'life': 0, 'dmg': 0, 'exp': 0}
                        break
                    elif bohater.life <= 0:
                        print('''
                    UMARŁEŚ!
                        ''')
                        death = 'dead'
                        break

def ilosc_przec():
    a = random.randint(1, 10000)
    if a % 2 == 0:
        print('Natrafiłeś na przeciwnika.')
        return 1
    elif a % 3 == 0:
        print('Natrafiłeś na dwóch przeciwników, przygotuj się na walkę.')
        return 2
    elif a % 2 == 0 and a % 3 == 0 and a % 5 == 0:
        print('Spotkałeś hordę przeciwników, przygotuj się na śmierć.')
        return 5
    else:
        print('Masz szczęście, w tym pomieszczeniu nie ma przeciwników.')
        return 0
def kierlos():
    kierunki = ['lewo','prawo','prosto']
    a = random.randint(0, 1000)
    kierwysl = []
    if a % 2 == 0:
        spr = 0
        while spr == 0:
            a = random.choice(kierunki)
            b = random.choice(kierunki)
            if a != b:
                spr = 1
                kierwysl.append(a)
                kierwysl.append(b)
                print('Kierunki, które możesz wybrać to: {0}, {1}.'.format(kierwysl[0], kierwysl[1]))
    elif a % 3 == 0:
        spr = 0
        while spr == 0:
            a = random.choice(kierunki)
            b = random.choice(kierunki)
            c = random.choice(kierunki)
            if a != b and b != c and c != a:
                spr = 1
                kierwysl.append(a)
                kierwysl.append(b)
                kierwysl.append(c)
                print('Kierunki, które możesz wybrać to: {0}, {1}, {2}.'.format(kierwysl[0], kierwysl[1], kierwysl[2]))
    else:
        kierwysl.append(random.choice(kierunki))
        print('Kierunek, który możesz wybrać to: {0}.'.format(kierwysl[0]))
    return input('Podaj kierunek w którym chcesz się poruszać: ')

def przedm():
    a = random.randint(0, 1000)
    lista = ['miecz', 'łuk', 'katalizator zaklęć', 'zbroję', 'tarczę']
    if a % 2 == 0 or a % 3 == 0:
        print('W komnacie nie znalazłeś żadnych przedmiotów.')
    else:
        obraz = random.randint(1, bohater.lvl*5)
        obr = random.randint(1, bohater.lvl*3)
        nazw = random.choice(lista)
        if nazw == 'tarczę' or nazw == 'zbroję':
            if nazw == 'tarczę':
                print('Udało Ci się znaleźć: {0} o obronie równej {1}. '
                      '(Obecna tarcza ma obronę równą {2})'.format(nazw, obr, bohater.tarcza['o']))
            else:
                print('Udało Ci się znaleźć: {0} o obronie równej {1}. '
                      '(Obecna zbroja ma obronę równą {2})'.format(nazw, obr, bohater.zbroja['o']))
            eq = input('Czy chcesz wyekwipować ten przedmiot? ')
            if eq == 'tak':
                if nazw == 'tarczę':
                    bohater.tarcza['n'] = nazw
                    bohater.tarcza['o'] = obr
                else:
                    bohater.zbroja['n'] = nazw
                    bohater.zbroja['o'] = obr
        elif nazw == 'miecz' or nazw == 'łuk' or nazw == 'katalizator zaklęć':
            print('Udało Ci się znaleźć: {0} o obrażeniach równych {1}. (Obecna broń to {2}'
                  ' o obrażeniach równych {3})'.format(nazw, obraz, bohater.bron['n'], bohater.bron['d']))
            eq = input('Czy chcesz wyekwipować ten przedmiot? ')
            if eq == 'tak':
                bohater.bron['n'] = nazw
                bohater.bron['d'] = obraz

def ekranStartowy():
    print('Witaj w Dungeon World - tekstowym dungeon crawlerze.')
    a = input('Czy chcesz rozpocząć swoją przygodę lub wczytać grę? ')
    if a[0] in ('R', 'r'):
        return True
    elif a[0] in ('W', 'w'):
        wczyt()
        return False

def zapis():
    global bohater
    a = shelve.open('zapis')
    a['postacr'] = bohater.r
    a['postacl'] = bohater.lvl
    a['postacd'] = bohater.dmg
    a['postacli'] = bohater.life
    a['postacs'] = bohater.si
    a['postacin'] = bohater.int
    a['postacw'] = bohater.wit
    a['postacz'] = bohater.zre
    a['postacu'] = bohater.unik
    a['postace'] = bohater.exp
    a['postacb'] = bohater.bron
    a['postaczb'] = bohater.zbroja
    a['postact'] = bohater.tarcza
    print('Zakończono zapisywanie.')
    a.close()

def wczyt():
    global bohater
    a = shelve.open('zapis')
    bohater.r = a['postacr']
    bohater.lvl = a['postacl']
    bohater.dmg = a['postacd']
    bohater.life = a['postacli']
    bohater.si = a['postacs']
    bohater.int = a['postacin']
    bohater.wit = a['postacw']
    bohater.zre = a['postacz']
    bohater.unik = a['postacu']
    bohater.exp = a['postace']
    bohater.bron = a['postacb']
    bohater.zbroja = a['postaczb']
    bohater.tarcza = a['postact']
    a.close()
    print('Zakończono wczytywanie')

def gra():
    global death
    death = ''
    if bohater.life > 0:
        stan = input("Co chcesz zrobić (1.Iść 2.Zobaczyć statystyki 3.Zapisać grę i wyjść)? ")
        if stan in ('iść', '1'):
            kierlos()
            for a in range(ilosc_przec()):
                P = Przeciwnik()
                P.walka()
            if death != 'dead':
                przedm()
                bohater.update()
                bohater.lvl_up()
                bohater.update()
                print('*' * 30)
            else:
                return 'dead'
        elif stan in ('zobaczyć statystyki', '2'):
            bohater.update()
            bohater.showStats()
            print('*' * 30)
        elif stan in ('zapisać grę', '3'):
            bohater.update()
            zapis()
            print('*' * 30)
            sys.exit()

def pocz():
    bohater.rasa()
    bohater.update()
    bohater.showStats()
    print('*' * 30)
    return True

x = ekranStartowy()
while x in (False, True):
    if x == True:
        while pocz():
            while gra() != 'dead':
                continue
            else:
                break
    elif x == False:
        while gra() != 'dead':
            continue
        else:
            while pocz():
                while gra() != 'dead':
                    continue
                else:
                    break