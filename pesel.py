pesel = input()
temp = []
pesel_a = []

def konwersja(pesel, temp, pesel_a):
    for ttt in pesel:
        temp.append(ttt)

    for i in range(len(temp)):
        x = int(temp[i])
        pesel_a.append(x)

    # print(pesel_a)

konwersja(pesel, temp, pesel_a)

def sprawdzanie(pesel, temp, pesel_a):
    
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
    print(kontrolna)

sprawdzanie(pesel, temp, pesel_a)
