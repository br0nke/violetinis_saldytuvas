#produkto isemimas is saldytuvo
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
    #PAKEITIMAS