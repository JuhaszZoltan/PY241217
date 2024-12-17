# a ciklusnak van else ága:
# ez akkor fut le, ha a ciklus törzsében sosem futott le 'break' utasítás
# avagy: a break a ciklust a hozzá tartozó 'else' záradék UTÁNRA töri

sorozat:list[int] = [26, 2, 11, 7, 42, 7, 34]

k:int = int(input('keresett szam: '))

for i in range(len(sorozat)):
    if sorozat[i] == k:
        print('van találat')
        print(f'indexe: {i}')
        break
else: print('nincs találat')

titok:str = "qwerty123"
for _ in range(3):
    jelszo = input('írd be a jelszót: ')
    if titok == jelszo:
        break
else: print('nincs több próbálkozási lehetőség')

print('kövi sor')