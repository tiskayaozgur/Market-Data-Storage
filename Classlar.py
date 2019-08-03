import sqlite3

class Veri_Tabani(): #Veri tabani adi altinda bir class olusturdum.
    def __init__(self):

        self.baglanti_olustur() #baglanti_olustur adinda bir method tanimladim.



    def baglanti_olustur(self): #veri tabani ve tablo olusturdum.
        self.baglanti=sqlite3.connect("Urun_Bilgileri.db") #Urun_Bilgileri adi altinda bir veri tabani olusturdum.
        self.cursor=self.baglanti.cursor() #imleci tanimaldim.
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Bilgiler( AD TEXT, URETİM TEXT, STT TEXT, GRAMAJ INT)")#tablo olusturdum
        self.baglanti.commit()#tabloyu veri tabanina bagladim.

    def baglanti_kes(self): #Veri tabani ile olan baglantiyi kesmek icin.
        self.baglanti.close()

    def urun_gir(self): #Database'e urun eklemek icin olusturdugum fonksiyon.
        self.ad=input("Ürün adi giriniz=")
        self.uretim_tarihi=input("Ürünün üretim tarihini giriniz=")
        self.stt=input("Ürünün son tüketim tarihini giriniz=")
        self.gram=int(input("Ürünün gramini giriniz="))

        self.cursor.execute("INSERT INTO Bilgiler VALUES(?,?,?,?)",(self.ad,self.uretim_tarihi,self.stt,self.gram))
        self.baglanti.commit()#sorgumu db'de calistirdim.

    def tum_urunleri_goster(self): #Veri tabanimda hangi urunlerin oldugunu gosteren fonksiyonum.
        self.cursor.execute("SELECT * FROM Bilgiler")
        liste=self.cursor.fetchall()
        print(liste)

    def urun_sil(self): #Istenilen urunu komple silmeye yarar. Yani urune dair tum bilgileri silmek icin olusturdugum fonk.
        self.isim=input("Database'den silmek istediginiz ürün adini  giriniz=")
        self.cursor.execute("DELETE FROM Bilgiler where AD=?",(self.isim,))#en sona virgül atma sebebimiz demet seklinde tutuldugu icin veri.(?)
        self.baglanti.commit()


    def urun_guncelle(self):#Urun guncellemek icin olusturdugum fonksiyon.
        self.cursor.execute("SELECT * FROM Bilgiler")
        liste=self.cursor.fetchall()
        for i in liste:
            a=i[0]
            b=i[1]
            c=i[2]#guncellemek istedigim verinin adini aldim.
            d=i[3]


        print("Ürünün neyini guncellemek istiyorsunuz?")
        print("1-Adini=\n 2-Uretim Tarihini=\n 3-STT=\n 4-Urunun Gramini=")
        islem=input("Bir islem seciniz=")
        if(islem=="1"):
            self.a = input("Guncellemek istediginiz urun adini giriniz=")
            self.yeni_ad = input("Yeni ürün adini giriniz=")
            self.cursor.execute("UPDATE Bilgiler SET AD=? WHERE AD=?", (self.yeni_ad, self.a))
            self.baglanti.commit()


        elif(islem=="2"):
            self.b = input("Guncellemek istediginiz urun uretim tarihini giriniz=")
            self.yeni_tarih = input("Yeni ürün URETİM TARİHİNİ giriniz=")
            self.cursor.execute("UPDATE Bilgiler SET URETİM=? WHERE URETİM=?", (self.yeni_tarih, self.b))
            self.baglanti.commit()

        elif(islem=="3"):
            self.c = input("Guncellemek istediginiz urunun STT giriniz=")
            self.yeni_stt= input("Yeni ürün STT giriniz=")
            self.cursor.execute("UPDATE Bilgiler SET STT=? WHERE STT=?", (self.yeni_stt, self.c))
            self.baglanti.commit()

        elif(islem=="4"):
            self.d = input("Guncellemek istediginiz urun gramajini giriniz=")
            self.yeni_gram = input("Yeni ürün GRAMİNİ giriniz=")
            self.cursor.execute("UPDATE Bilgiler SET GRAMAJ=? WHERE GRAMAJ=?", (self.yeni_gram, self.d))
            self.baglanti.commit()


obje=Veri_Tabani() #Veri_Tabani adli calss'imdan obje adinda bi obje olusutrdum ve bu objemin methodlarini diger yerde kulanabilmke icin.

