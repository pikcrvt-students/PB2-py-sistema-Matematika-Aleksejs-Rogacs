#Programmu izveidoja: Aleksejs Rogačs
import time

print('Labdien,student! Šodien jums ir jāiepazīstas ar tādu tēmu kā "Kvadrātvienādojums un augstāku pakāpju vienādojumi". \
Vispirms tiks sniegta teorija. Pēc teorijas izlasīšanas varēsi veikt patstāvīgā darba uzdevumus.\
Pēc patstāvīgā darba veikšanas būs kontroldarbs vērtēšanai.')
print()
print()
time.sleep(3)

#Teoretiska daļa
print('Teorija')
print()
print('Kvadrātvienādojumu atrisināšanas metodes')
print('Vienādojumu ax**2+bx+c=0, kur a, b un c ir reāli skaitļi un a≠0,\
sauc par kvadrātvienādojumu.')
print()
print('Kvadrātvienādojuma saknes var atrast pēc formulām:')
print('x1 = -b+√D/2a \
      x2 = -b-√D/2a \
      D = b**2 -4*a*c')
print()
print('Vērtību D sauc par diskriminantu. \
Pēc diskriminanta vērtības var noteikt kvadrātvienādojuma sakņu skaitu.\n\
Ja D<0 (negatīvs), tad vienādojumam nav atrisinājuma reālo skaitļu kopā.\n\
Ja D=0, tad vienādojumam ir divas vienādas saknes.\n\
Ja D>0 (pozitīvs), tad vienādojumam ir divas dažādas saknes.')
print()
print('Kvadrātvienādojumu x2+bx+c=0 var risināt, izmantojot Vjeta teorēmu: \n\
x1*x2=c\n\
x1+x2=-b\n\
Ievēro: koeficients pie x**2 ir a=1!')
print()
print()
print('Nepilnie kvadrātvienādojumi\n\
\n\
Ir divu veidu nepilnie kvadrātvienādojumi:\n\
1. Ja c=0, tad vienādojums ir ax**2+bx=0\n\
2. Ja b=0, tad ax**2+c=0.\n\
\n\
Nepilnos kvadrātvienādojumus drīkst risināt ar diskriminanta formulām, \
bet racionālāk būs izvēlēties speciālas metodes:\n\
1) ax**2+bx=0 risina, sadalot reizinātājos (iznesot pirms iekavām x).\n\
x(ax+b)=0\n\
Tātad x=0 vai ax+b=0. (Jo divu skaitļu reizinājums ir vienāds ar nulli\
tikai tad, ja vismaz viens no šiem skaitļiem ir 0.)\n\
Viena sakne ir 0, bet otra sakne ir x=-b/a\n\
\n\
2) ax**2+c=0 risina, pārnesot saskaitāmos dažādās pusēs un tad velkot kvadrātsakni.\n\
ax2=−c (izdala abas puses ar a)\n\
x**2=−c/a \n\
|x|=√ -c/a\n\
Tas nozīmē, ka x1 = sqrt(-c/a)   un  x2= -sqrt(-c/a)')
print()
print()
print('Vienādojuma atrisināšana, sadalot reizinātājos')
print('Ja divu vai vairāku lielumu reizinājums ir 0, tad vismaz viens no reizinātājiem ir 0.\n\
(Tas nozīmē, ka visiem reizinātājiem reizē nav obligāti jābūt vienādiem ar nulli, tāpēc raksta vārdu "vai").')
print()
print('1) Visus locekļus pārnes vienādojuma kreisajā pusē, labajā pusē jābūt 0.     x**3=16x --> x**3 - 16x=0 \n\
2) Kreiso pusi sadala reizinātājos.       x(x**2−16)=0\n\
3) Katru reizinātāju pielīdzina 0.        x=0 vai x**2−16=0\n\
4) Atrisina katru no iegūtajiem vienādojumiem. x=0  x**2=16 ----> |x|=4\n\
5) Uzraksta atbildi.   x1=0, x=−4, x=4')
print()
input('Nospiediet Enter, lai turpinātu')
print()
print()

#Patstavīgais darbs
print('Šeit sākas patstāvīgais darbs. \n\
Tiks doti risināmie uzdevumi un jāievada atbilde. \
Pēc tam jūs varat pāriet uz pārbaudes darbu.')
print()
def izvada_pirmo_uzdevumu():
    print('1.uzdevums. Atradi kvadrātvienadojuma x**2+4x+3=0 saknes. Pirmkart ievadi mazāko skaitli.')
    print()
    pareiz_atbilde1= -3
    pareiz_atbilde2= -1
    studenta_atbilde1 = int(input('Ievadiet pirmo sakni: '))
    studenta_atbilde2 = int(input('Ievadiet otro sakni: '))
    print()
    if studenta_atbilde1 == pareiz_atbilde1 and studenta_atbilde2 == pareiz_atbilde2:
        print('Saknes ir pareizas. Malacis!')
    elif studenta_atbilde1 != pareiz_atbilde1 and studenta_atbilde2 != pareiz_atbilde2:
        print('Abas saknes ir nepareizas')
    else:
        print('Viena no saknem ir nepareiza')


izvada_pirmo_uzdevumu()
input('Nospiediet Enter, lai pariet uz nākamo uzdevumu.')
print()
print()

def izvada_otro_uzdevumu():
    print('2.uzdevums. Atradi kvadrātvienadojuma 2x**2-13x-7=0 saknes.Atrisiniet, \
izmantojot diskriminanta formulu.Pirmkart ievadi lielako skaitli.\
Uzrakstiet savas atbildes kā decimāldaļas ar vienu zīmi aiz komata.')
    print()
    pareiz_atbilde1= 7
    pareiz_atbilde2= -0.5
    studenta_atbilde1 = float(input('Ievadiet pirmo sakni: '))
    studenta_atbilde2 = float(input('Ievadiet otro sakni: '))
    print()
    if studenta_atbilde1 == pareiz_atbilde1 and studenta_atbilde2 == pareiz_atbilde2:
        print('Saknes ir pareizas. Malacis!')
    elif studenta_atbilde1 != pareiz_atbilde1 and studenta_atbilde2 != pareiz_atbilde2:
        print('Abas saknes ir nepareizas')
    else:
        print('Viena no saknem ir nepareiza')
        

izvada_otro_uzdevumu()
input('Nospiediet Enter, lai pariet uz nākamo uzdevumu.')
print()
print()

def izvada_trešo_uzdevumu():
    print('3.uzdevums. Atradi kvadrātvienadojuma 4x**2-100=0 saknes.\
Pirmkart ievadi lielako skaitli.')
    print()
    pareiz_atbilde1= 5
    pareiz_atbilde2= -5
    studenta_atbilde1 = int(input('Ievadiet pirmo sakni: '))
    studenta_atbilde2 = int(input('Ievadiet otro sakni: '))
    print()
    if studenta_atbilde1 == pareiz_atbilde1 and studenta_atbilde2 == pareiz_atbilde2:
        print('Saknes ir pareizas. Malacis!')
    elif studenta_atbilde1 != pareiz_atbilde1 and studenta_atbilde2 != pareiz_atbilde2:
        print('Abas saknes ir nepareizas')
    else:
        print('Viena no saknem ir nepareiza')


izvada_trešo_uzdevumu()
input('Nospiediet Enter, lai pariet uz nākamo uzdevumu.')
print()
print()
input('Šeit sākas parbaudes darbs. Būs 5 piemēri. Par katru pareizi atrisinātu\
piemēru tiek doti 2 punkti.1 punkts - 1 balle. Pēc visu uzdevumu izpildes \
tiks teikts vērtējums. Lai sakt pildit darbu nospiediet Enter')
print()

def izvada_pd_pirmo_uzdevumu():
    global punktu_skaits_par_pirmo
    print('1.uzdevums. Atradi kvadrātvienadojuma x**2+5x+6=0 saknes. Pirmkart ievadi mazāko skaitli.\
Par uzdevumu var dabūt 2 punktus.')
    print()
    pareiz_atbilde1= 2
    pareiz_atbilde2= 3
    studenta_atbilde1 = int(input('Ievadiet pirmo sakni: '))
    studenta_atbilde2 = int(input('Ievadiet otro sakni: '))
    print()
    print()
    punktu_skaits_par_pirmo = 0 
    if studenta_atbilde1 == pareiz_atbilde1 and studenta_atbilde2 == pareiz_atbilde2:
        punktu_skaits_par_pirmo = punktu_skaits_par_pirmo + 2 
    elif studenta_atbilde1 != pareiz_atbilde1 and studenta_atbilde2 != pareiz_atbilde2:
        punktu_skaits_par_pirmo = punktu_skaits_par_pirmo + 0
    else:
        punktu_skaits_par_pirmo = punktu_skaits_par_pirmo + 1
        

izvada_pd_pirmo_uzdevumu()


def izvada_otro_pd_uzdevumu():
    global punktu_skaits_par_otro
    print('2.uzdevums. Atradi kvadrātvienadojuma 4x**2-8x=0 saknes. Pirmkart ievadi mazāko skaitli.\
Par uzdevumu var dabūt 2 punktus.')
    print()
    pareiz_atbilde1= 0
    pareiz_atbilde2= 2
    studenta_atbilde1 = int(input('Ievadiet pirmo sakni: '))
    studenta_atbilde2 = int(input('Ievadiet otro sakni: '))
    print()
    print()
    punktu_skaits_par_otro = 0 
    if studenta_atbilde1 == pareiz_atbilde1 and studenta_atbilde2 == pareiz_atbilde2:
        punktu_skaits_par_otro = punktu_skaits_par_otro + 2 
    elif studenta_atbilde1 != pareiz_atbilde1 and studenta_atbilde2 != pareiz_atbilde2:
        punktu_skaits_par_otro = punktu_skaits_par_otro + 0
    else:
        punktu_skaits_par_otro = punktu_skaits_par_otro + 1


izvada_otro_pd_uzdevumu()


def izvada_trešo_pd_uzdevumu():
    global punktu_skaits_par_trešo
    print('3.uzdevums. Atradi kvadrātvienadojuma x**2-6.5x-6=0 saknes. Pirmkart ievadi mazāko skaitli.\
Par uzdevumu var dabūt 2 punktus.Uzrakstiet savas atbildes kā \
decimāldaļas ar diviem cipariem aiz komata.')
    print()
    pareiz_atbilde1= -0.82
    pareiz_atbilde2= 7.32
    studenta_atbilde1 = float(input('Ievadiet pirmo sakni: '))
    studenta_atbilde2 = float(input('Ievadiet otro sakni: '))
    print()
    punktu_skaits_par_trešo = 0 
    if studenta_atbilde1 == pareiz_atbilde1 and studenta_atbilde2 == pareiz_atbilde2:
        punktu_skaits_par_trešo = punktu_skaits_par_trešo + 2 
    elif studenta_atbilde1 != pareiz_atbilde1 and studenta_atbilde2 != pareiz_atbilde2:
        punktu_skaits_par_trešo = punktu_skaits_par_trešo + 0
    else:
        punktu_skaits_par_trešo = punktu_skaits_par_trešo + 1


izvada_trešo_pd_uzdevumu()


def izvada_ceturto_pd_uzdevumu():
    global punktu_skaits_par_ceturto
    print('4.uzdevums. Zināms, ka kvadrātvienādojuma x**2+Ax+V=0 saknes ir −13 un 5. \
Pirmkart ievadi mazāko skaitli.Nosaki, kādi ir koeficienti A un V.\
Par uzdevumu var dabūt 2 punktus.')
    print()
    pareiz_atbilde1= -65
    pareiz_atbilde2= 8
    studenta_atbilde1 = int(input('Ievadiet pirmo sakni: '))
    studenta_atbilde2 = int(input('Ievadiet otro sakni: '))
    print()
    punktu_skaits_par_ceturto = 0 
    if studenta_atbilde1 == pareiz_atbilde1 and studenta_atbilde2 == pareiz_atbilde2:
        punktu_skaits_par_ceturto = punktu_skaits_par_ceturto + 2 
    elif studenta_atbilde1 != pareiz_atbilde1 and studenta_atbilde2 != pareiz_atbilde2:
        punktu_skaits_par_ceturto = punktu_skaits_par_ceturto + 0
    else:
        punktu_skaits_par_ceturto = punktu_skaits_par_ceturto + 1


izvada_ceturto_pd_uzdevumu()


def izvada_piekto_pd_uzdevumu():
    global punktu_skaits_par_piekto
    print('5.uzdevums. Taisnstūra garuma un platuma starpība ir 9 cm. \
Aprēķini taisnstūra platumu un garumu, ja taisnstūra laukums ir 90 cm**2!\
Pirmkart ievadi mazāko skaitli.\
Par uzdevumu var dabūt 2 punktus.')
    print()
    pareiz_atbilde1= 6
    pareiz_atbilde2= 15
    studenta_atbilde1 = int(input('Platums : '))
    studenta_atbilde2 = int(input('Garums: '))
    print()
    punktu_skaits_par_piekto = 0 
    if studenta_atbilde1 == pareiz_atbilde1 and studenta_atbilde2 == pareiz_atbilde2:
        punktu_skaits_par_piekto = punktu_skaits_par_piekto + 2 
    elif studenta_atbilde1 != pareiz_atbilde1 and studenta_atbilde2 != pareiz_atbilde2:
        punktu_skaits_par_piekto = punktu_skaits_par_piekto + 0
    else:
        punktu_skaits_par_piekto = punktu_skaits_par_piekto + 1


izvada_piekto_pd_uzdevumu()

atzīme = punktu_skaits_par_pirmo + punktu_skaits_par_otro + \
         punktu_skaits_par_trešo + punktu_skaits_par_ceturto + punktu_skaits_par_piekto 
print('Visi parbaudes darba uzdevumi ir izpildīti. Jūsu atzīme ir: ',atzīme)


      

