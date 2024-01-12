def prideti_produkta(saldytuvas, produktas, kiekis=0):
    if produktas in saldytuvas.keys():
        saldytuvas[produktas] += kiekis
        print(f'{kiekis} {produktas} buvo pridėtas į šaldytuvą')
    else:
        saldytuvas[produktas] = kiekis
        print(f'{kiekis} {produktas} buvo pridėtas į šaldytuvą')

    return saldytuvas

def isimti_produkta(saldytuvas, pavadinimas):
    if pavadinimas in saldytuvas.keys():
        print(f'Ar norite ištrinti visus {pavadinimas} iš šaldytuvo?')
        salyga = input('taip/ne: ')
        if salyga.lower() == 'taip':
            del saldytuvas[pavadinimas]
            print(f'Produktas {pavadinimas} buvo išimtas iš šaldytuvo')
            print(f'Šaldytuve dabar yra: {saldytuvas}')
        elif salyga.lower() == 'ne':
            print(f'Įveskite kiekį {pavadinimas}, kurį norite išimti: ')
            norimas_kiekis = float(input())
            if norimas_kiekis > saldytuvas[pavadinimas]:
                print('Norimas kiekis viršija turimą kiekį')
            else:
                saldytuvas[pavadinimas] -= norimas_kiekis
                print(f'{norimas_kiekis} {pavadinimas} buvo išimtas iš šaldytuvo')
                print(f'Šaldytuve dabar yra: {saldytuvas}')
    else:
        print('Produkto nėra')

    return saldytuvas

def patikrinti_kieki(saldytuvas, pavadinimas):
    if pavadinimas in saldytuvas.keys():
        print(f"Produktas {pavadinimas} yra šaldytuve")
        print(f'Yra {saldytuvas[pavadinimas]} {pavadinimas} šaldytuve')
    else:
        print(f"Produktas {pavadinimas} nėra šaldytuve")

def print_saldytuvas(saldytuvas):
    for key, value in saldytuvas.items():
        print(f'* {key} : {value}')

def patikrinti_recepta(saldytuvas, receptas):
    truksta_produktu = {}
    reikalinga_receptui = dict(item.split(': ') for item in receptas.split(', '))
    for produktas, reikalingas_kiekis_str in reikalinga_receptui.items():
        reikalingas_kiekis = float(reikalingas_kiekis_str)
        if produktas in saldytuvas:
            trukstamas_kiekis = reikalingas_kiekis - saldytuvas[produktas]
            if trukstamas_kiekis > 0:
                truksta_produktu[produktas] = trukstamas_kiekis
        else:
            truksta_produktu[produktas] = reikalingas_kiekis
        
    if truksta_produktu:
        print('Trūksta šių produktų:')
        for produktas, trukstamas_kiekis in truksta_produktu.items():
            print(f'{produktas}: {trukstamas_kiekis}')
    else:
        print('Receptas išeina')

    return saldytuvas

def main(saldytuvas):
    while True:
        print('---Violetinis šaldytuvas---')
        print('0: Išeiti')
        print('1: Pridėti į šaldytuvą')
        print('2: Išimti iš šaldytuvo')
        print('3: Patikrinti ar produktas yra šaldytuve')
        print('4: Parodyti šaldytuvo turinį')
        print('5: Patikrinti receptą')
        choice = input('Pasirinkite: ')
        if choice == '0':
            break
        if choice == '1':
            produktas = input('Kokį produktą norėtumėte pridėti?: ')
            kiekis = float(input('Kokį kiekį norėtumėte pridėti?: '))
            saldytuvas = prideti_produkta(saldytuvas, produktas, kiekis)
        if choice == '2':
            pavadinimas = input('Kokį produktą norėtumėte išimti?: ')
            saldytuvas = isimti_produkta(saldytuvas, pavadinimas)
        if choice == '3':
            pavadinimas = input('Kokio produkto ieškote?: ')
            patikrinti_kieki(saldytuvas, pavadinimas)
        if choice == '4':
            print_saldytuvas(saldytuvas)
        if choice == '5':
            receptas = input("Įveskite receptą (Pvz.: produktas1: kiekis1(skaicius), produktas2: kiekis2(skaicius)): ")
            patikrinti_recepta(saldytuvas, receptas)
        else:
            print("Klaida! Įveskite meniu pasirinkimą")
            

saldytuvas = {}
print(saldytuvas)

saldytuvas = prideti_produkta(saldytuvas, 'pienas', 1.5)
patikrinti_kieki(saldytuvas, 'pienas')
print_saldytuvas(saldytuvas)

main(saldytuvas)
