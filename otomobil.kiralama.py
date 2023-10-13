class Araba:
    def __init__(self, marka, model, yil, fiyat):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.fiyat = fiyat
        self.kirada_mi = False

class Kullanici:
    def __init__(self, isim, adres):
        self.isim = isim
        self.adres = adres
        self.kiralanan_araba = None
        self.kiralama_gecmisi = []

    def araba_kirala(self, araba, kiralama_suresi):
        if araba.kirada_mi:
            print("Bu araba zaten kirada.")
        else:
            araba.kirada_mi = True
            self.kiralanan_araba = araba
            kiralama_tarihi = datetime.now()
            iade_tarihi = kiralama_tarihi + timedelta(days=kiralama_suresi)
            self.kiralama_gecmisi.append((self.kiralanan_araba, kiralama_tarihi, iade_tarihi))
            print(f"{self.isim}, {araba.marka} {araba.model} aracını {kiralama_suresi} gün boyunca kiraladı.")

    def araba_iade_et(self):
        if not self.kiralanan_araba:
            print("Hiç araba kiralamamışsınız.")
        else:
            iade_tarihi = datetime.now()
            kira_suresi = (iade_tarihi - self.kiralama_gecmisi[-1][1]).days
            kira_ucreti = kira_suresi * self.kiralanan_araba.fiyat
            araba = self.kiralanan_araba
            araba.kirada_mi = False
            self.kiralanan_araba = None
            print(f"{self.isim}, {araba.marka} {araba.model} aracını iade etti.")
            print(f"Kira Süresi: {kira_suresi} gün, Toplam Kira Ücreti: {kira_ucreti} TL")
            self.kiralama_gecmisi[-1] = (araba, self.kiralama_gecmisi[-1][1], iade_tarihi)

    def kiralama_gecmisini_goruntule(self):
        if not self.kiralama_gecmisi:
            print("Kiralama geçmişi bulunmuyor.")
        else:
            print(f"{self.isim} adlı kullanıcının kiralama geçmişi:")
            for kira in self.kiralama_gecmisi:
                araba, kiralama_tarihi, iade_tarihi = kira
                print(f"{araba.marka} {araba.model}, Kiralama Tarihi: {kiralama_tarihi}, İade Tarihi: {iade_tarihi}")


# Test etmek için kullanım örnekleri
from datetime import datetime, timedelta

araba1 = Araba("Toyota", "Corolla", 2022, 200)
araba2 = Araba("Honda", "Civic", 2022, 180)

kullanici1 = Kullanici("Ahmet", "İstanbul")
kullanici2 = Kullanici("Mehmet", "Ankara")

kullanici1.araba_kirala(araba1, 7)
kullanici2.araba_kirala(araba2, 5)

kullanici1.araba_iade_et()
kullanici2.araba_iade_et()

kullanici1.kiralama_gecmisini_goruntule()
kullanici2.kiralama_gecmisini_goruntule()
