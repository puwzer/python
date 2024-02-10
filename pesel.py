pesel = input()

#konwertuje string na array z liczbami
def konwersja(pesel):
    pesel_a = []
    temp = []

    for ttt in pesel:
        temp.append(ttt)

    for i in range(len(temp)):
        x = int(temp[i])
        pesel_a.append(x)

    return pesel_a

pesel_a = konwersja(pesel)



def sprawdzanie(pesel_a):
    
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    iloczyn_liczb = []
    cyfra = 0
    suma = 0

    for i in range(10):
        liczba = pesel_a[i] * wagi[i]
        iloczyn_liczb.append(liczba)
        cyfra = iloczyn_liczb[i] % 10
        suma = suma + cyfra

    kontrolna = 10 - (suma%10)
    return kontrolna



kontrolna = sprawdzanie(pesel_a)

if pesel_a[10] == kontrolna:
    print("Pesel jest poprawny")