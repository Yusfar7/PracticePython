def toplama(sayi1,sayi2):
    return sayi1+sayi2

def cikarma(sayi1,sayi2):
    return sayi1-sayi2

def carpma(sayi1,sayi2):
    return sayi1*sayi2

def bolme(sayi1,sayi2):
    if float(sayi2) ==0:
        return "0'a bölünemez"
    
    return sayi1/sayi2

'''def bolme(sayi1,sayi2):
    try: 
        return sayi1/sayi2
    except ZeroDivisionError:
        return "0'a bölünemez" '''


islem = input("islem tipi sec: 1/2/3/4:")

sayi1= float(input("sayi1: "))
sayi2= float(input("sayi2: "))

if islem == "1":
    print(sayi1,"+",sayi2,"=",toplama(sayi1,sayi2))

elif islem == "2":
    print(sayi1,"-",sayi2,"=",cikarma(sayi1,sayi2))

elif islem == "3":
    print(sayi1,"*",sayi2,"=",carpma(sayi1,sayi2))

elif islem == "4":
    print(sayi1,"/",sayi2,"=",bolme(sayi1,sayi2))
else:
    print("geçersiz sayi")