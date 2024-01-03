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

def prideti_produktą(saldytuvas, produktas, kiekis):
    if produktas in saldytuvas:
        saldytuvas[produktas] += kiekis
    else:
        saldytuvas[produktas] = kiekis

def isimti_produktą(saldytuvas, produktas, kiekis):
    if produktas in saldytuvas:
        if saldytuvas[produktas] >= kiekis:
            saldytuvas[produktas] -= kiekis
            if saldytuvas[produktas] == 0:
                del saldytuvas[produktas]
            return True
        else:
            print("Nepakankamas produktų kiekis šaldytuve.")
            return False
    else:
        print("Produktas nerastas šaldytuve.")
        return False

def patikrinti_kieki(saldytuvas, produktas, kiekis):
    if produktas in saldytuvas and saldytuvas[produktas] >= kiekis:
        print(f"Produktų {produktas} kiekis šaldytuve yra pakankamas.")
        return True
    else:
        print(f"Produktų {produktas} kiekis šaldytuve nepakankamas.")
        return False

def ispausdinti_turini(saldytuvas):
    print("Šaldytuvo turinys:")
    for produktas, kiekis in saldytuvas.items():
        print(f"{produktas}: {kiekis:.2f} kg")

def patikrinti_recepta(saldytuvas, receptas):
    truksta_produktu = {}
    recepto_produktai = dict(item.split(':') for item in receptas.split(','))

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

saldytuvas = {}

prideti_produktą(saldytuvas, "Obuoliai", 5.5)
prideti_produktą(saldytuvas, "Pienas", 2.3)
prideti_produktą(saldytuvas, "Morkos", 3.2)
prideti_produktą(saldytuvas, "Burokai", 13.2)

ispausdinti_turini(saldytuvas)

isimti_produktą(saldytuvas, "Pienas", 1.2)
isimti_produktą(saldytuvas, "Obuoliai", 2.8)

ispausdinti_turini(saldytuvas)

patikrinti_kieki(saldytuvas, "Obuoliai", 1)
patikrinti_kieki(saldytuvas, "Pienas", 3)

receptas = "Morkos: 2.0, Kiaušiniai: 4.0, Obuoliai: 3.0, Pienas: 5.0"

patikrinti_recepta(saldytuvas, receptas)