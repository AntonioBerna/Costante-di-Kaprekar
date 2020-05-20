def controllo_input(n):
    if len(n) < 4:
        raise TypeError("Errore: il numero deve avere minimo 4 cifre")


def ordina_crescente(n):
    return "".join(sorted(n))


def ordina_decrescente(n):
    return "".join(reversed(sorted(n)))


def costante_kaprekar(n):
    iterazioni_max_kaprekar = 7
    for i in range(iterazioni_max_kaprekar):
        kaprekar = int(ordina_decrescente(str(n))) - int(ordina_crescente(str(n)))
        print("Iterazioni:", i+1, ">>", int(ordina_decrescente(str(n))), "-", int(ordina_crescente(str(n))), "=", kaprekar)
        n = kaprekar

        if n == 6174 or n == 0:
            print("Numero di iterazioni:", i+1)
            break

def main():
    print("Costante di Kaprekar\n")
    n = str(input(">> "))
    controllo_input(n)
    costante_kaprekar(n)

if __name__ == "__main__":
    main()
