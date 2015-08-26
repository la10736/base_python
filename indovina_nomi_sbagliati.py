import random

a = 0
b = 2000
c = random.randint(a, b)
d = 0

while True:
    d = d + 1
    print("--- Tentativo numero " + str(d) + ".")
    e = a - 1
    while not a <= e <= b:
        f = input("Inserisci un numero tra " + str(a) + " e " + str(b) + ":")
        try:
            e = int(f)
        except:
            print("Ma chi vuoi prendere in giro? '" + f + "' non è un numero!")
    if e == c:
        print("BRAVO!!!! Hai indovinato in " + str(d) + " tentativi.")
        import sys
        sys.exit()
    g = "Peccato non hai indovinato... prova ancora con un numero più "
    if e > c:
        g = g + "basso"
    if e < c:
        g = g + "alto"
    print(g + ".")
