import random

class Vprasanja:
    def __init__(self):
        self.vprasanja = {}
        # vprasanja so slovar vprasanj z nabori odgovorov (prvi je pravilen)
        # prebere vprasanja.txt po vrsticah in shranjuje v slovar
        with open ("vprasanja.txt", "r") as f:
            for vrstica in f.readlines():
                razclenjeno = []
                beseda = ""
                for znak in vrstica:
                    if znak == ";":
                        razclenjeno.append(beseda)
                        beseda = ""
                    else:
                        beseda += znak
                 #izpise vprašanja v obliki slovarja
                self.vprasanja[razclenjeno[0]] = razclenjeno[1:4]
        #izpise vprašanja v obliki seznama
        self.vprasanja = list(self.vprasanja.items())
        #katero vprasanje po vrsti je to
        self.vpr = 0
        self.rezultat = 0
        

    def __repr__(self):
        return "Vprasanja(vprasanja = {}, vprasanje = {}, rezultat = {})".format(
            self.vprasanja, self.vpr, self.rezultat)

    def vprasaj_vprasanje(self):
        vprasanje, odgovori = self.vprasanja[self.vpr]
        pravilen_odgovor = odgovori[0]
        random.shuffle(odgovori, random.random)
        self.vpr += 1
        return vprasanje, odgovori, pravilen_odgovor
    
    def preveri_odgovor(self, izbrani_odgovor, pravilen_odgovor):
        #preveri ali je izbrani odgovor pravilen in rezultatu prišteje točko
        if izbrani_odgovor == pravilen_odgovor:
            self.rezultat += 1
            return True
        else:
            return False


v = Vprasanja()
