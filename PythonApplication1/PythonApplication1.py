import math
##Ulesanne 1
nimi = input("Kirjuta sinu nimi: ")
print("Tere " + str(nimi))

print()

##Ulesanne2.1
a = 3+8/(4-2)*4
print(a)
b = 3+8/4-2*4
print(b)


##Ulesanne2.2
r = float(3)
d = r * r
Skv = d * d
Pkv = 4 * d
Skr = math.pi * (pow(r, 2))
Pkr = float(2 * math.pi * r)

print("Площадь квадрата: " + str(Skv))
print("Периметр квадрата: " + str(Pkv))
print("Площадь круга: " + str(Skr))
print("Периметр круга: " + str(Pkr))

##Ulesanne 4
Rmaa = 6378
dcoin = float(2.5) #см
dcoinm = dcoin / 100
maapikk = 2*Rmaa*math.pi
coinarv = int(maapikk//dcoinm)
print("Длина земли в 2 евровых монетах равна " + str(coinarv))

##Ulesanne 4
print("""kill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll kill-koll killkoll
kill-koll""")
# Я не использовал переменные, так как в данном случае это не имеет смысл


print()
##Ulesanne 5
print("""Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?""")
next = str(input("Хотите следующую песню, напишите jah или ei: "))
if next == "jah":
    print("""Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.

""")
else:
    print("Пока")
    
##Ulesanne 6
a = float(input("Введите первую сторону прямоугольника: "))
b = float(input("Введите вторую сторону прямоугольника: "))
p = (a+b)*2
s = a*b
print("Периметр прямоугольника равен: " + str(p))
print("Площадь прямоугольника равна: " + str(s))

##Ulesanne 7
liiterbenzin = float(input("Введите количество литров бензина: "))
km = float(input("Введите количество пройденых километров: "))
rashod_topliva = (liiterbenzin/km)*100
print("Ваш расход топлива на 100км состовляет: " + str(rashod_topliva))


##Ulesanne 8
speed = float(29.9)
speedmin = speed / 60 #скорость в минутах
minutes = 1
distance = speedmin * minutes
print("Роликовый конькобежец проходит за одну минуту: " + str(distance) + " километров")

##Ulesanne 9
time_minutes = int(input("Введите время в минутах: "))
time_hours = int(time_minutes/60)
time_minutes2 = int(time_minutes%60)
print("Сейчас " + str(time_hours) + ":" + str(time_minutes2))











