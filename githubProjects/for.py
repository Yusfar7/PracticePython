'''for i in range(30):
    print(i ,"1{}".format(i*"0"))'''

'''tr_harfler = "şçöğüİıÖÜ"
parola = input("Parolanız: ")
for karakter in parola:
    if karakter in tr_harfler:
     print("Parolada Türkçe karakter kullanılamaz")'''

'''sayilar = "12345"
for sayi in sayilar:
    print(int(sayi)*2, end=" ")'''

'''tr= "şçğüİıÖÜöü"
s= input("sifre: ")
for h in s:
    if h in tr:
        print("Turkce karakter kullanmayin.")'''

'''s = int(input("sayi: "))
f = 1
for i in range(1,s+1):
    f *= i
print(f)'''

'''metin= input("sayi girin: ")
for i in metin:
    print(i)'''

s= int(input("Boyut girin: "))

for satir in range(1, s+1):
    for sutun in range(1, s+1):
        deger=satir*sutun
        print("{0:4}".format(deger), end="")
    print()