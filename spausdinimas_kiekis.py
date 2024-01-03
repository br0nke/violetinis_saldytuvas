# spasdinimas ir kieko tikrinimas kiekio
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
#PAKEITIMAS