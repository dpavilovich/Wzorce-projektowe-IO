import time
import threading


class Magazyn:
    def __init__(self, pojemnosc):
        self.pojemnosc = pojemnosc
        self.produkty = []  
        self.producenci = []  
        self.konsumenci = []  

    def dodaj_producenta(self, producent):
        self.producenci.append(producent)

    def dodaj_konsumenta(self, konsument):
        self.konsumenci.append(konsument)

    def jest_miejsce(self):
        return len(self.produkty) < self.pojemnosc

    def sa_produkty(self):
        return len(self.produkty) > 0

    def dodaj_produkt(self, produkt):
        if self.jest_miejsce():
            self.produkty.append(produkt)

    def usun_produkt(self):
        if self.sa_produkty():
            return self.produkty.pop()
        return None

    def powiadom_producentow(self):
        for producent in self.producenci:
            producent.produkuj(self)

    def powiadom_konsumentow(self):
        for konsument in self.konsumenci:
            konsument.konsumuj(self)


class Producent:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.licznik = 0

    def produkuj(self, magazyn):
        if magazyn.jest_miejsce():
            produkt = f"{self.nazwa}-{self.licznik}"
            self.licznik += 1
            magazyn.dodaj_produkt(produkt)
            print(f"Producent {self.nazwa} wyprodukował: {produkt}")


class Konsument:
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def konsumuj(self, magazyn):
        produkt = magazyn.usun_produkt()
        if produkt:
            print(f"Konsument {self.nazwa} skonsumował: {produkt}")



def main():
    pojemnosc_magazynu = 5
    magazyn = Magazyn(pojemnosc_magazynu)

  
    producent1 = Producent("P1")
    producent2 = Producent("P2")
    producent3 = Producent("P3")

    konsument1 = Konsument("K1")
    konsument2 = Konsument("K2")
    konsument3 = Konsument("K3")

   
    magazyn.dodaj_producenta(producent1)
    magazyn.dodaj_producenta(producent2)
    magazyn.dodaj_producenta(producent3)

    magazyn.dodaj_konsumenta(konsument1)
    magazyn.dodaj_konsumenta(konsument2)
    magazyn.dodaj_konsumenta(konsument3)

 
    def magazyn_aktywny():
        while True:
            if magazyn.jest_miejsce():
                magazyn.powiadom_producentow()
            if magazyn.sa_produkty():
                magazyn.powiadom_konsumentow()
            time.sleep(2)

    
    thread = threading.Thread(target=magazyn_aktywny, daemon=True)
    thread.start()

   
    time.sleep(20)


if __name__ == "__main__":
    main()
