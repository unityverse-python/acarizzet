class Urun:
    def __init__(self, urun_id, ad, fiyat, stok_miktari):
        self.urun_id = urun_id
        self.ad = ad
        self.fiyat = fiyat
        self.stok_miktari = stok_miktari

    def urun_bilgilerini_goruntule(self):
        print(f"Ürün ID: {self.urun_id}, Ürün Adı: {self.ad}, Fiyat: {self.fiyat} TL, Stok Miktarı: {self.stok_miktari} adet")

class Magaza:
    def __init__(self):
        self.urunler = []

    def urun_ekle(self, urun):
        self.urunler.append(urun)
        print(f"{urun.ad} ürünü mağazaya eklendi.")

    def urun_duzenle(self, urun_id, yeni_ad, yeni_fiyat, yeni_stok_miktari):
        for urun in self.urunler:
            if urun.urun_id == urun_id:
                urun.ad = yeni_ad
                urun.fiyat = yeni_fiyat
                urun.stok_miktari = yeni_stok_miktari
                print(f"{urun.ad} ürünü düzenlendi.")
                return
        print("Ürün bulunamadı.")

    def urun_listele(self):
        for urun in self.urunler:
            urun.urun_bilgilerini_goruntule()

    def siparis_al(self, urun_id, adet, musteri):
        for urun in self.urunler:
            if urun.urun_id == urun_id:
                if urun.stok_miktari >= adet:
                    urun.stok_miktari -= adet
                    toplam_fiyat = adet * urun.fiyat
                    if musteri.indirim_orani > 0:
                        toplam_fiyat *= (1 - musteri.indirim_orani)
                    print(f"{musteri.isim}, {urun.ad} ürününden {adet} adet sipariş verdi. Toplam Fiyat: {toplam_fiyat} TL")
                    return
                else:
                    print(f"{urun.ad} ürününden yeterli stok bulunmuyor.")
                    return
        print("Ürün bulunamadı.")

class Musteri:
    def __init__(self, isim, indirim_orani=0):
        self.isim = isim
        self.indirim_orani = indirim_orani

# Basit bir e-ticaret platformu simülasyonu
magaza = Magaza()

urun1 = Urun(1, "Laptop", 3000, 10)
urun2 = Urun(2, "Akıllı Telefon", 1500, 20)

magaza.urun_ekle(urun1)
magaza.urun_ekle(urun2)

urun3 = Urun(3, "Tablet", 800, 15)
magaza.urun_duzenle(2, "Yeni Akıllı Telefon", 1600, 25)

urun4 = Urun(4, "Klavye", 100, 5)
magaza.urun_ekle(urun4)

musteri1 = Musteri("Ahmet", 0.1)
musteri2 = Musteri("Mehmet")

magaza.siparis_al(1, 2, musteri1)
magaza.siparis_al(3, 3, musteri2)

print("\nMevcut Ürünler:")
magaza.urun_listele()

