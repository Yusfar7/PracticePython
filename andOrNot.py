"""durum = True 

if durum:
    print("Hazır!")
else:
    print("Bir sorunla karşılaşıldı.")
"""

def sayi():
    sayi1 = int(input("0'dan 10'a kadar bir sayı giriniz: "))
    if sayi1 >=0 and sayi1 <=10:
        print("Doğru sayı girdiniz.")
    else:
        print("0'dan 10'a kadar olan bir sayı girmeniz gerekiyor.")
        sayi()
sayi()