'''a= float(input("sayi1 giriniz: "))
b= float(input("sayi2 giriniz: "))
try:
    print(a/b)
except ZeroDivisionError:
    print("0'a bölünemez")'''

a= float(input("sayi giriniz: "))
if a%3 == 0 and a%2==0:
    print("sayi 6 ya tam bölünür")
elif a%3 == 0:
    print("3'e tam bölünür")
elif a%2 == 0:
    print("2'ye tam bölünür")
else:
    print("2 yada 3'e bölünmez")