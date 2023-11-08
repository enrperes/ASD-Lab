# Scrivere un programma che stampi tutti i suffissi di una stringa ricevuta in input.

string = input("Inserisci una stringa: ")

# Stampa tutti i suffissi della string
for i in range(len(string)):
    print(string[i:])
