# Arbeidskrav 2 av Laurent Zogaj


# Oppgave 1
alder = int(input('Hvilket år er du født? '))
alder_i_2024 = 2024 - alder
print(f'Du blir {alder_i_2024} år i 2024.')

# Oppgave 2
antall_elever = int(input('Skriv inn antall elever: '))
pizzastykker_per_elev = 0.25
antall_pizzaer = antall_elever * pizzastykker_per_elev
antall_pizzaer = -(-antall_pizzaer // 1)  
print(f'Det må handles inn {antall_pizzaer:.0f} pizzaer til festen.')

# Oppgave 3
import numpy as np

v_grad = float(input('Skriv inn graden: '))
v_rad = v_grad * np.pi / 180
print(f'{v_grad} grader tilsvarer {v_rad:.4f} radianer.')

# Oppgave 4
# a)
data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}

# b)
land = input('Skriv inn et land: ')
if land in data:
    hovedstad, innbyggere = data[land]
    print(f'{hovedstad} er hovedstaden i {land} og det er {innbyggere} mill. innbyggere i {hovedstad}.')
else:
    print(f'{land} finnes ikke i dataene.')

# c)
while True:
    nytt_land = input('Skriv inn et nytt land: ')

    if nytt_land in data:
        print(f'{nytt_land} finnes allerede i dataene. Skriv inn et annet nytt land.')
    else:
        hovedstad = input(f'Skriv inn hovedstaden i {nytt_land}: ')
        innbyggere = float(input(f'Skriv inn antall innbyggere (i mill.) i {hovedstad}: '))
        data[nytt_land] = [hovedstad, innbyggere]
        print(f'{nytt_land} lagt til: {data[nytt_land]}')
        break  

print(f'Oppdatert data: {data}')

# Oppgave 5
import math

def beregn_figur(a, b):
    areal_halvsirkel = math.pi * (a / 2)**2 / 2
    omkrets_halvsirkel = math.pi * a / 2

    areal_trekant = (a * b) / 2
    omkrets_trekant = a + b + math.sqrt(a**2 + b**2)

    total_areal = areal_halvsirkel + areal_trekant
    total_omkrets = omkrets_halvsirkel + omkrets_trekant

    return total_areal, total_omkrets

a = float(input('Skriv inn a (diameter): '))
b = float(input('Skriv inn b (høyde): '))

areal, omkrets = beregn_figur(a, b)
print(f'Arealet er {areal:.2f} og ytre omkrets er {omkrets:.2f}.')

# Oppgave 6
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
y = -x**2 - 5

plt.plot(x, y, label='f(x) = -x^2 - 5')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graf av f(x) = -x^2 - 5')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.legend()
plt.grid(True)
plt.show()

