#prideti produkta i saldytuva
def prideti_produktą(saldytuvas, produktas, kiekis):
    if produktas in saldytuvas:
        saldytuvas[produktas] += kiekis
    else:
        saldytuvas[produktas] = kiekis
    #PAKEITIMAS
    