""" Komandinio darbo užduotis
===[ Šaldytuvas ]===

Reikalavimai:

* Šaldytuvo turinys - žodynas, kurio raktas yra produkto pavadinimas, reikšmė - kiekis (float).
* Pridėti produktą į šaldytuvą. Pridedant egzistuojantį produktą, kiekiai sudedami su esančiais.
* Išimti produktą iš šaldytuvo. Išimant egzistuojantį produktą, kiekis atitinkamai sumažinamas.
* Patikrinti, ar reikiamas produkto kiekis yra šaldytuve.
* Išspausdinti visą šaldytuvo turinį su kiekiais.

BONUS:

* Patikrinti, ar receptas išeina. 
** Recepto įvedimas vyksta viena eilute, kuri po to išdalinama. Pva.: Sūris: 0.5, Pomidoras: 2, Duona: 0.4
** Jeigu receptas neišeina, išvardinti kiek ir kokių produktų trūksta.

"""
def prideti_produkta(saldytuvas, produktas, kiekis = 0):
    if produktas in saldytuvas.keys():
        saldytuvas[produktas] = saldytuvas[produktas] + kiekis
        print(f'{kiekis} sio {produktas} buvo pridetas i saldytuva')
        print(saldytuvas)
    else:
        saldytuvas[produktas] = kiekis
        print(f'{kiekis} sio {produktas} buvo pridetas i saldytuva')
        print(saldytuvas)

    return saldytuvas

def isimti_produkta(saldytuvas, pavadinimas):

    if pavadinimas in saldytuvas.keys():
        print(f'Ar noretumete istrinti visus {pavadinimas} is saldytuvo?')
        salyga = input('taip/ne   ')
        if salyga.lower() == 'taip':
            del saldytuvas[pavadinimas]
            print(f'Produktas {pavadinimas} buvo isimtas is saldytuvo')
            print(f'Saldytuve dabar yra: {saldytuvas}')
        elif salyga.lower() == 'ne':
            print(f'Irasykite kieki {pavadinimas} ka norite isimti')
            print(f'Saldytuve dabar yra: {saldytuvas}')
            pasalintas_kiekis = float(input())
            saldytuvas[pavadinimas] = saldytuvas[pavadinimas] - pasalintas_kiekis
            print(f'{pasalintas_kiekis} {pavadinimas} buvo issimtas is saldytuvo')
    else:
        print('Produkto nera')

    return saldytuvas
    
def patikrinti_kieki(saldytuvas, pavadinimas):
    if pavadinimas in saldytuvas.keys():
        print(f"Produktas {pavadinimas} yra saldytuve")
        print(f'Yra {saldytuvas[pavadinimas]} {pavadinimas} saldytuve')
    else:
        print(f"Produktas {pavadinimas} nera saldytuve")

def print_saldytuvas(saldytuvas):
    for key, value in saldytuvas.items():
        print(f'* {key} : {value}')
#cia yra uzduoties sprendimas be saldytuvo turinio ir be papildomos uzduoties

def main(saldytuvas):
        
    while True:

        print('violetinis saldytuvas')
        print('0: Iseiti')
        print('1: Prideti i saldytuva')
        print('2: Isimti is saldytuvo')
        print('3: Patikrinti ar porduktas yra saldytuve')
        print('4: Parodyti saldytuvo turini')
        print('5: Recepto kurimas')
        print('6: Recepto patikrinimas')
        choice = input('Pasirinkite')
        if choice == '0':
            break
        if choice == '1':
            produktas = input('Koki produkta noretumete prideti?: ')
            kiekis = float(input('Koki kieki noretumete prideti?: '))
            saldytuvas = prideti_produkta(saldytuvas, produktas, kiekis)
        if choice == '2':
            pavadinimas = input('Koki produkta noretumete issimti?: ')
            saldytuvas = isimti_produkta(saldytuvas, pavadinimas)
        if choice == '3':
            pavadinimas = input('Kokio produkto ieskote?: ')
            patikrinti_kieki(saldytuvas, pavadinimas)
        if choice == '4':
            print_saldytuvas(saldytuvas)
        if  choice == '5':
            break
