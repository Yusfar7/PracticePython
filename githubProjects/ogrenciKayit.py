a = input("isim: ")
b = input("soyisim: ")
c = input("okul no: ")
d = input("okul adı: ")

f = input("Cinsiyet: E/K ")
g = input("Tel no")

while True:
    e = input("TC no: ")
    if len(e) == 11:
        break
    else:
        print("hatalı TC") 

print("Ogrenci Bilgileri: ")
print("Adı: " + a)
print("Soyadı: " + b)
print("Okul No" + c)
print("Okul Adı: " + d)
print("TC: " + e)
print("Cinsiyet: " + f)
print("İletişim: " + g)