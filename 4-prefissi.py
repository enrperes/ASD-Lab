# Scrivere un programma che stampi tutti i prefissi di una stringa ricevuta in input.

string = input("insert a string: ")

for i in range(len(string) -1, -1, -1): # len(string)-1 = starting index, -1 = ending index, -1 = step
    print(string[:i])