import tkinter as tk
import model

class Kviz:
    def __init__(self, okno):
        self.okno = okno
        self.vprasaj = tk.Label(okno, text = "Pozdravjen v kvizu!", font = ("Times", 13))
        self.vprasaj.grid(row = 1, column = 2)
        self.zacni = tk.Button(okno, text ="ZAČNI", command = self.zastavi_vprasanje,  font = ("Times", 13))
        self.zacni.grid(row = 10, column = 2)
        self.rezultat = tk.Label(okno, text ="")
        self.rezultat.grid(row = 10, column = 3)

    def zastavi_vprasanje(self):
        if model.v.vpr == 5:
            self.koncaj()
        else:
            #gumba in napis na začetku pravzaprav zamenjamo s tema dvema.
            self.rezultat.config(text = "Rezultat: {}".format(model.v.rezultat), font = ("Times", 13))
            self.zacni.config(text ="Novo vprašanje", command = self.zastavi_vprasanje, font = ("Times", 13), bg = "magenta")
            vprasanje, odgovori, pravilen_odgovor = model.v.vprasaj_vprasanje()
            self.vprasaj.config(text = "{}. vprašanje:\n".format(model.v.vpr) + vprasanje)
            
            self.gumbi = []
            gumbA = tk.Button(text= odgovori[0], command = lambda:self.preveri(odgovori, pravilen_odgovor, 0), height=1, width=12, font = ("Times", 13))
            gumbA.grid(row = 2, column = 2)
            self.gumbi.append(gumbA)
            
            gumbB = tk.Button(text= odgovori[1], command = lambda:self.preveri(odgovori, pravilen_odgovor, 1), height=1, width=12, font = ("Times", 13))
            gumbB.grid(row = 3, column = 2)
            self.gumbi.append(gumbB)
            
            gumbC = tk.Button(text= odgovori[2], command = lambda:self.preveri(odgovori, pravilen_odgovor, 2), height=1, width=12, font = ("Times", 13))
            gumbC.grid(row = 4, column = 2)
            self.gumbi.append(gumbC)

    def preveri(self, odgovori, pravilen_odgovor, izbran_odgovor):
        #preveri ali je izbran odgovor pravilen, če je ga pobarva zeleno in rezultatu prišteje točko
        #če je izbran odgovor napačen, ga pobarva rdečo in rezultat se ne spremeni.
        if model.v.preveri_odgovor(odgovori[izbran_odgovor], pravilen_odgovor):
            self.gumbi[izbran_odgovor].config(bg = "green")
        else:
            self.gumbi[izbran_odgovor].config(bg = "red")
        for gumb in self.gumbi:
            gumb.config(state = "disabled")
        self.rezultat.config(text ="Rezultat: {}".format(model.v.rezultat))

    def koncaj(self):
        self.vprasaj.config(text = "Konec kviza!")
        self.rezultat.config(text = "Zbral si {} točk od {} možnih. Čestitam!".format(model.v.rezultat, 5))
        self.zacni.destroy()
                
okno = tk.Tk()
moja_igra = Kviz(okno)
okno.mainloop()

        
