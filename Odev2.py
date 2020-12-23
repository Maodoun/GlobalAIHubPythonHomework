#Turkish Ai Hub- Introduction to Python Course İkinci Ödev
list1 = []

name = str(input("Lutfen Adinizi giriniz: "))
lastname = str(input("Lutfen Soyadinizi giriniz: "))
age = int(input("Lutfen Yaşinizi giriniz: "))
dateofbirth = int(input("Lütfen dogum yilinizi yaziniz: "))
list1.append([name, lastname, age, dateofbirth])

#if type(name) != str:    KONTROL İÇİN AMA EKSİK BİR NOKTADA
#    Print("Lütfen adinizi giriniz")

for i in list1:
    print(i)

if (age < 18):
    print("You can't go out because it's too dangerous")
else:
    print("You can go out to the street")
