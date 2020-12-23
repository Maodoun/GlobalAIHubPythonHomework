#Turkish Ai Hub- Introduction to Python Course İkinci Ödev

name = input("Lutfen Adinizi giriniz: ")
lastname = input("Lutfen Soyadinizi giriniz: ")
age = int(input("Lutfen Yaşinizi giriniz: "))
dateofbirth = int(input("Lütfen dogum yilinizi yaziniz: "))

list1 = []
list1.append(f"Adın: {name}, Soyadın: {lastname}, Yasın: {age}, Doğum yılın: {dateofbirth}")

for i in list1:
    print(i)

if (age < 18):
    print("You can't go out because it's too dangerous")
else:
    print("You can go out to the street")
