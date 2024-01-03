class Saldytuvas:
    def __init__(self):
        self.turinys = {}

    def prideti_produktą(self, produktas, kiekis):
        if produktas in self.turinys:
            self.turinys[produktas] += kiekis
        else:
            self.turinys[produktas] = kiekis

    def isimti_produktą(self, produktas, kiekis):
        if produktas in self.turinys:
            if self.turinys[produktas] >= kiekis:
                self.turinys[produktas] -= kiekis
                if self.turinys[produktas] == 0:
                    del self.turinys[produktas]
                return True
            else:
                print("Nepakankamas produktų kiekis šaldytuve.")
                return False
        else:
            print("Produktas nerastas šaldytuve.")
            return False

    def patikrinti_kieki(self, produktas, kiekis):
        if produktas in self.turinys and self.turinys[produktas] >= kiekis:
            print(f"Produktų {produktas} kiekis šaldytuve yra pakankamas.")
            return True
        else:
            print(f"Produktų {produktas} kiekis šaldytuve nepakankamas.")
            return False

    def ispausdinti_turini(self):
        print("Šaldytuvo turinys:")
        for produktas, kiekis in self.turinys.items():
            print(f"{produktas}: {kiekis:.2f} kg.")

    def patikrinti_recepta(self, receptas):
        truksta_produktu = {}
        recepto_produktai = dict(item.split(':') for item in receptas.split(','))

        for produktas, reikalingas_kiekis in recepto_produktai.items():
            reikalingas_kiekis = float(reikalingas_kiekis)
            if produktas not in self.turinys or self.turinys[produktas] < reikalingas_kiekis:
                truksta_produktu[produktas] = reikalingas_kiekis - self.turinys.get(produktas, 0)

        if truksta_produktu:
            print("Receptas neišeina. Trūksta šių produktų:")
            for produktas, trukstamas_kiekis in truksta_produktu.items():
                print(f"{produktas}: trūksta {trukstamas_kiekis}")
        else:
            print("Receptas išeina su turimais produktais.")

# Pavyzdys naudojant klases su float kiekiais
saldytuvas = Saldytuvas()

saldytuvas.prideti_produktą("Obuoliai", 5.5)
saldytuvas.prideti_produktą("Pienas", 2.3)
saldytuvas.prideti_produktą("Obuoliai", 3.2)

saldytuvas.ispausdinti_turini()

saldytuvas.isimti_produktą("Pienas", 1.2)
saldytuvas.isimti_produktą("Obuoliai", 2.8)

saldytuvas.ispausdinti_turini()

saldytuvas.patikrinti_kieki("Obuoliai", 1)
saldytuvas.patikrinti_kieki("Pienas", 3)

receptas = "Pienas: 1, Obuoliai: 4, Duona: 0.5"
saldytuvas.patikrinti_recepta(receptas)
