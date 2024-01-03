#receptas
def patikrinti_recepta(saldytuvas, receptas):
    truksta_produktu = {}
    recepto_produktai = dict(item.split(':') for item in receptas.split(','))

    for produktas, reikalingas_kiekis in recepto_produktai.items():
        reikalingas_kiekis = float(reikalingas_kiekis)
        if produktas not in saldytuvas or saldytuvas[produktas] < reikalingas_kiekis:
            truksta_produktu[produktas] = reikalingas_kiekis - saldytuvas.get(produktas, 0)
    if truksta_produktu:
        print("Receptas neišeina. Trūksta šių produktų:")
        for produktas, trukstamas_kiekis in truksta_produktu.items():
            print(f"{produktas}: trūksta {trukstamas_kiekis:.2f} kg")
    else:
        print("Receptas išeina su turimais produktais.")
        #PAKEITIMAS