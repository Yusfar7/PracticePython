a= float(input("sayi1 giriniz: "))
b= float(input("sayi2 giriniz: "))
try:
    print(a/b)
except ZeroDivisionError:
    print("0'a bölünemez")