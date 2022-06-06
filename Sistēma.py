#Programmu izveidoja: Aleksejs Rogačs
import time

print('Labdien,student! Šodien jums ir jāiepazīstas ar tādu tēmu kā \
"Kvadrātvienādojums un augstāku pakāpju vienādojumi". \
Vispirms tiks sniegta teorija. Pēc teorijas izlasīšanas varēsi veikt \
patstāvīgā darba uzdevumus.\
Pēc patstāvīgā darba veikšanas būs kontroldarbs vērtēšanai.\n\n')
time.sleep(3)

teorija = open('Teorija.txt',encoding='utf8')
print(teorija.read())
teorija.close()


input('Nospiediet Enter, lai turpinātu\n\n')

#Patstavīgais darbs
print('Šeit sākas patstāvīgais darbs. \n\
Tiks doti risināmie uzdevumi un jāievada atbilde. \
Pēc tam jūs varat pāriet uz pārbaudes darbu.')
print()
def izvada_pirmo_uzdevumu():
    print('1.uzdevums. Atradi kvadrātvienadojuma x**2+4x+3=0 saknes. \
Pirmkart ievadi mazāko skaitli.\n')
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
input('Nospiediet Enter, lai pariet uz nākamo uzdevumu.\n\n')

def izvada_otro_uzdevumu():
    print('2.uzdevums. Atradi kvadrātvienadojuma 2x**2-13x-7=0 saknes.Atrisiniet, \
izmantojot diskriminanta formulu.Pirmkart ievadi lielako skaitli.\
Uzrakstiet savas atbildes kā decimāldaļas ar vienu zīmi aiz komata.\n')
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
input('Nospiediet Enter, lai pariet uz nākamo uzdevumu.\n\n')

def izvada_trešo_uzdevumu():
    print('3.uzdevums. Atradi kvadrātvienadojuma 4x**2-100=0 saknes.\
Pirmkart ievadi lielako skaitli.\n')
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
input('Nospiediet Enter, lai pariet uz nākamo uzdevumu.\n\n')
input('Šeit sākas parbaudes darbs. Būs 5 piemēri. Par katru pareizi atrisinātu \
piemēru tiek doti 2 punkti.1 punkts - 1 balle. Pēc visu uzdevumu izpildes \
tiks teikts vērtējums. Lai sakt pildit darbu nospiediet Enter')
print()

def izvada_pd_pirmo_uzdevumu():
    global punktu_skaits_par_pirmo
    print('1.uzdevums. Atradi kvadrātvienadojuma x**2+5x+6=0 saknes. \
Pirmkart ievadi mazāko skaitli.\
Par uzdevumu var dabūt 2 punktus.\n')
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
    print('2.uzdevums. Atradi kvadrātvienadojuma 4x**2-8x=0 saknes. \
Pirmkart ievadi mazāko skaitli.\
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
    print('3.uzdevums. Atradi kvadrātvienadojuma x**2-6.5x-6=0 saknes. \
Pirmkart ievadi mazāko skaitli.\
Par uzdevumu var dabūt 2 punktus.Uzrakstiet savas atbildes kā \
decimāldaļas ar diviem cipariem aiz komata.\n')
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
Par uzdevumu var dabūt 2 punktus.\n')
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
Par uzdevumu var dabūt 2 punktus.\n')
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

      

