from Classlar import *

print("""MARKET URUN BILGILERI
1-URUN EKLEME
2-URUN SILME
3-VERI TABANINDA BULUNAN MEVCUT URUN OZELLIKLERINI GORME
4-URUN BILGILERINI GUNCELLEME""")

islem=input("Lutfen yapmak istediginiz islemi seciniz=")

if(islem=="1"):
    print(obje.urun_gir())
elif(islem=="2"):
    print(obje.urun_sil())
elif(islem=="3"):
    print(obje.tum_urunleri_goster())
elif(islem=="4"):
    print(obje.urun_guncelle())
