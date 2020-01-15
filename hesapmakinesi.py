from alanmodul import *

from cevremodul import *
import time

print("""
####################################################
#                                                  #
#    HESAP MAKİNESİ UYGULAMAMA HOŞ GELDİN!!!       #
#                                                  #
#               MEHMET ERDEM AKIN                  # 
#                                                  #
####################################################
      
    """)
time.sleep(0.4)
print("""
*Yapmak istediğiniz operasyonların numarası yanında yazmaktadır.*
      """)
time.sleep(0.5)
print("---#OPERASYONLAR#--- :")
print("1 : Topla")
print("2 : Çıkar")
print("3 : Çarp")
print("4 : Böl")
time.sleep(0.6)
print("---#ALANLAR#--- :")
print("5 : Dikdörtgen")
print("6 : Kare")
print("7 : Üçgen")
time.sleep(0.7)
print("---#ÇEVRE#---")
print("8 : Dikdörtgen")
print("9 : Kare")
print("10 : Üçgen")      

while True:
    time.sleep(0.9)
    print("\nLütfen yapmak istediğiniz işlem numarasını giriniz(Çıkmak için (ç) basınız):\t")
    time.sleep(1)
    secenek = input("=> Operasyon seçiminiz ? : ")
    if secenek=="ç":
        print("Uygulamadan çıkılıyor...")
        break
 



    elif secenek == "1":
        toplam=0
        while True:
            try:
                sayi=input("Toplanacak sayı ? (İşlemi Tamamlamak için (Ç) tuşuna basınız) : ")
                if(sayi=="ç"):
                    break
                sayi=int(sayi)
                toplam+=sayi
            except ValueError:
                print("Yanlış değer Girdiniz")
                print("lütfen rakam giriniz")
        print("Sayıların Toplamı:",toplam)
    
    elif secenek == "2":
        try:
            sayi1=input("Çıkarılacak sayı ? (işlemi sonlandırmak içim (ç)basınız) :")
            if(sayi1=="ç"):
                break
            sayi1=int(sayi1)    
            while True:
                sayi2=input("Çıkarılacak sayı ? (işlemi sonlandırmak içim (ç)basınız) :")
                if(sayi2=="ç"):
                    break
                sayi2=int(sayi2)  
                sayi1-=sayi2 
        except ValueError:
            print("Yanlış değer Girdiniz")
            print("lütfen rakam giriniz")
        print("Çıkarma sonucu : ",sayi1)
    
    elif secenek == "3":
        carpim=1
        while True:
            try:
                sayi = input("* Çarpılacak sayı ?  (işlemi sonlandırmak içim (ç)basınız) : ")
                if(sayi == "ç"):
                    break
                sayi=int(sayi)
                carpim*=sayi
            except ValueError:
                print("Yanlış değer girdiniz")
                print("lütfen rakam giriniz")
        print("=> Çarpım sonucu : " , carpim)
    
    elif secenek == "4":
        try:
            sayi1=input("Sayi Giriniz (işlemi sonlandırmak içim (ç)basınız) :")
            if(sayi1=="ç"):
                break
            sayi1=int(sayi1)    
            while True:
                sayi2=input("Sayi Girin (işlemi sonlandırmak içim (ç)basınız) :")
                if(sayi2=="ç"):
                    break
                sayi2=int(sayi2)  
                sayi1/=sayi2
        except ZeroDivisionError:
            print("Bir sayı 0'a bölünemez.")
        except ValueError:
            print("Yanlış değer Girdiniz")
            print("lütfen rakam giriniz")
        print("Sayıların Bölümü:",sayi1)
 
    elif secenek =="5":        
        while True:
            try:
                uzunkenar = input("* uzun kenarı giriniz (işlemi sonlandırmak içim (ç)basınız) : ")
                if(uzunkenar=="ç"):
                    break
                kisakenar = input("* kısa kenarı giriniz (işlemi sonlandırmak içim (ç)basınız) : ")
                if(kisakenar=="ç"):
                    break
                uzunkenar=int(uzunkenar)
                kisakenar=int(kisakenar)
                print("=> Dikdörtgenin Alanı : " + str(dikdortgenA(uzunkenar,kisakenar)))
            except ValueError:
                print("yanlış değer girdiniz")
                print("lütfen rakam giriniz")
                       
    
    elif secenek =="6":
        while True:
            try:
                kenar1 = input("*  kenarı giriniz (işlemi sonlandırmak içim (ç)basınız) : ")
                if(kenar1=="ç"):
                    break
                kenar1=int(kenar1)
                print("=> Karenin Alanı : " + str(kareA(kenar1)))
            except ValueError:
                print("yanlış değer girdiniz")
                print("lütfen rakam giriniz")
                

    elif secenek =="7":
        while True:
            try:
                taban = input("* taban değerini giriniz (işlemi sonlandırmak içim (ç)basınız) : ")
                if(taban=="ç"):
                    break
                yukseklık = input("* yüksekliği giriniz (işlemi sonlandırmak içim (ç)basınız) : ")
                if(yukseklık=="ç"):
                    break
                taban=int(taban)
                yukseklık=int(yukseklık)
                print("=> Üçgenin Alanı : " +  str(ucgenA(taban,yukseklık)))
            except ValueError:
                print("yanlış değer girdiniz")
                print("lütfen rakam giriniz")
    
    elif secenek =="8":
        while True:
            try:
                uzunkenar = input("* uzun kenarı giriniz (işlemi sonlandırmak içim (ç)basınız) : ")
                if(uzunkenar=="ç"):
                    break
                kisakenar = input("* kısa kenarı giriniz (işlemi sonlandırmak içim (ç)basınız) : ") 
                if(kisakenar=="ç"):
                    break
                uzunkenar=int(uzunkenar)
                kisakenar=int(kisakenar)
                print("=> Dikdörtgenin Çevresi : " + str(dikdortgenÇ(uzunkenar,kisakenar)))
            except ValueError:
                print("yanlış değer girdiniz")
                print("lütfen rakam giriniz")

    elif secenek =="9":
        while True:
            try:
                kenar1 = input("*  kenarı giriniz (işlemi sonlandırmak içim (ç)basınız) :  ")
                if(kenar1=="ç"):
                    break
                kenar1=int(kenar1)
                print("=> Karenin Çevresi : " + str(kareÇ(kenar1,)))
            except ValueError:
                print("yanlış değer girdiniz")
                print("lütfen rakam giriniz")
    
    elif secenek =="10":
        while True:
            try:
                kenar1 = input("* 1. kenarı giriniz (işlemi sonlandırmak içim (ç)basınız) : ") 
                if(kenar1=="ç"):
                    break
                kenar2 = input("* 2. kenarı giriniz (işlemi sonlandırmak içim (ç)basınız) : ")
                if(kenar2=="ç"):
                    break
                kenar3 = input("* 3. kenarı giriniz (işlemi sonlandırmak içim (ç)basınız) : ")
                if(kenar3=="ç"):
                    break
                kenar1=int(kenar1)
                kenar2=int(kenar2)
                kenar3=int(kenar3)
                print("=> Üçgenin Çevresi : " + str(ucgenÇ(kenar1,kenar2,kenar3)))
            except ValueError:
                print("yanlış değer girdiniz")
                print("lütfen rakam giriniz")
    
    else:
        print(" # Operasyon numarasını yanlış girdiniz !!!")
        print(" # Lütfen 1-10 aralığında geçerli bir numara giriniz !!!\n")
