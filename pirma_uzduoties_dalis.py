
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
            print(f'Įveskite kiekį {pavadinimas}, kurį norite išimti: ')
            norimas_kiekis = float(input())
            if norimas_kiekis > saldytuvas[pavadinimas]:
                print('Norimas kiekis virsija turima kieki')
            else:
                saldytuvas[pavadinimas] -= norimas_kiekis
                print(f'{norimas_kiekis} {pavadinimas} buvo isimtas is saldytuvo')
                print(f'Saldytuve dabar yra: {saldytuvas}')
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

def patikrinti_recepta(saldytuvas, receptas):
    truksta_produktu = {}
    reikalinga_receptui = input('Iveskite savo recepta: Iveskite produkta ir kieki')
    recepto_produktai = dict(item.split(':') for item in reikalinga_receptui.split(','))
#cia reikia dabaigti papildoma uzduoti!!!
    for produktas, reikalingas_kiekis in recepto_produktai.items():
        reikalingas_kiekis = float(reikalingas_kiekis)
        if produktas not in saldytuvas or saldytuvas[produktas] < reikalingas_kiekis:
            truksta_produktu[produktas] = reikalingas_kiekis - saldytuvas.get(produktas, 0)
    if truksta_produktu:
        print("Receptui reikia: ", receptas)
        print("Receptas neišeina. Trūksta šių produktų:")
        for produktas, trukstamas_kiekis in truksta_produktu.items():
            print(f"{produktas}: trūksta {trukstamas_kiekis:.2f} kg")
    else:
        print(receptas)
        print("Receptas išeina su turimais produktais.")

    return saldytuvas

def main(saldytuvas):
        
    while True:


        print('--- violetinis saldytuvas ---')
        print('0: Iseiti')
        print('1: Prideti i saldytuva')
        print('2: Isimti is saldytuvo')
        print('3: Patikrinti ar produktas yra saldytuve')
        print('4: Parodyti saldytuvo turini')
        print('5: Recepto patikrinimas')
        choice = input('Pasirinkite ')
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
        if choice == '5':
            break


#pasirasom dar salyga, kad veiktu pirmos dalies kodas
saldytuvas = {}
print(saldytuvas)

saldytuvas = prideti_produkta(saldytuvas, 'pienas', 1.5)
patikrinti_kieki(saldytuvas, 'pienas')
print_saldytuvas(saldytuvas) 

main(saldytuvas)