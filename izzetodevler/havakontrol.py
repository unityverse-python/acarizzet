import random

class HavaTrafikKontrol:
    def __init__(self):
        self.ucuslar = []
    
    def yeni_ucus_ekle(self, ucus):
        self.ucuslar.append(ucus)
        print(f"{ucus} takip ediliyor.")
    
    def iniş_izni_ver(self, ucus):
        if ucus in self.ucuslar:
            print(f"{ucus} için iniş izni verildi.")
            self.ucuslar.remove(ucus)
        else:
            print(f"{ucus} takip edilmiyor veya iniş izni verilemez.")

class Ucak:
    def __init__(self, kod):
        self.kod = kod
    
    def __str__(self):
        return f"Uçak {self.kod}"

# Basit bir hava trafik kontrol simülasyonu
trafik_kontrol = HavaTrafikKontrol()

for i in range(5):
    yeni_ucak = Ucak(f"THY{i}")
    trafik_kontrol.yeni_ucus_ekle(yeni_ucak)

for i in range(3):
    ucak = trafik_kontrol.ucuslar[random.randint(0, len(trafik_kontrol.ucuslar) - 1)]
    trafik_kontrol.iniş_izni_ver(ucak)

print("Aktif Uçaklar:")
for ucus in trafik_kontrol.ucuslar:
    print(ucus)