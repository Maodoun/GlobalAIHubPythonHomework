#Turkish Ai Hub- Introduction to Python Course İlk Ödev

name = str(input("Lutfen Adinizi giriniz: "))
soyadi = str(input("Lutfen Soyadinizi giriniz: "))
yasiniz = int(input("Lutfen Yaşinizi giriniz: "))
sehir = str(input("Yaşadiginiz Şehiri giriniz: "))
meslek = str(input("Lutfen Mesleginizi giriniz: "))

print(type(name))
print(type(soyadi))
print(type(yasiniz))
print(type(sehir))
print(type(meslek))


name = input("Lutfen Adinizi giriniz: ")
soyadi = input("Lutfen Soyadinizi giriniz: ")
yasiniz = input("Lutfen Yaşinizi giriniz: ")
sehir = input("Yaşadiginiz Şehiri giriniz: ")
meslek = input("Lutfen Mesleginizi giriniz: ")

print("Adiniz: {} ve Soyadiniz: {}, Yasiniz: {}, Yasadiginiz Sehir: {} ve Mesleginiz: {} ".format(name ,soyadi, yasiniz, sehir, meslek ))
