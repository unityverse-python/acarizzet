class Hesap:
    def __init__(self, hesap_numarası, bakiye, faiz_oranı=0.0):
        self.hesap_numarası = hesap_numarası
        self.bakiye = bakiye
        self.faiz_oranı = faiz_oranı

    def para_yatır(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            print(f"{miktar} TL yatırıldı. Yeni bakiye: {self.bakiye} TL")
        else:
            print("Geçersiz işlem: Yatırılan miktar negatif olamaz.")

    def para_çek(self, miktar):
        if 0 < miktar <= self.bakiye:
            self.bakiye -= miktar
            print(f"{miktar} TL çekildi. Yeni bakiye: {self.bakiye} TL")
        else:
            print("Geçersiz işlem: Yetersiz bakiye veya negatif miktar.")

    def hesap_bakiyesi(self):
        return self.bakiye

    def faiz_uygula(self):
        faiz_miktarı = self.bakiye * (self.faiz_oranı / 100)
        self.para_yatır(faiz_miktarı)

    def __str__(self):
        return f"Hesap Numarası: {self.hesap_numarası}, Bakiye: {self.bakiye} TL"


class Musteri:
    def __init__(self, isim, soyisim, adres):
        self.isim = isim
        self.soyisim = soyisim
        self.adres = adres
        self.hesaplar = {}

    def hesap_ekle(self, hesap):
        self.hesaplar[hesap.hesap_numarası] = hesap

    def hesap_sil(self, hesap_numarası):
        if hesap_numarası in self.hesaplar:
            del self.hesaplar[hesap_numarası]
            print(f"{hesap_numarası} numaralı hesap silindi.")
        else:
            print(f"{hesap_numarası} numaralı hesap bulunamadı.")

    def __str__(self):
        return f"Müşteri Adı: {self.isim} {self.soyisim}, Adres: {self.adres}"

# Örnek Kullanım
musteri1 = Musteri("Ali", "Veli", "İstanbul")
hesap1 = Hesap("12345", 1000, 5)
hesap2 = Hesap("67890", 5000, 3)

musteri1.hesap_ekle(hesap1)
musteri1.hesap_ekle(hesap2)

print(musteri1)
print(hesap1)
print(hesap2)

hesap1.para_yatır(2000)
hesap1.para_çek(500)
hesap1.faiz_uygula()

print(musteri1.hesaplar["12345"])

musteri1.hesap_sil("67890")

