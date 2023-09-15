import time
print("Witam w kalkulatorze Ksawerego")
print()
print("==================")
print("1. Dodawanie")
print("2. odejmowanie")
print("3. mnozenie")
print("4. Dzielenie")
print("===================")
print()
metoda = input("Ktorą metode wybierasz?: ")
print()
print("=======================================")
Liczba_pierwsza = int(input("Liczba 1: "))
print()
Liczba_druga = int(input("Liczba 2: "))
print("========================================")
print()
print("================")
print("czekaj...")
print("================")
time.sleep(2)
print()
print("============================")
print("Robie kalkulacje...")
print("============================")
if metoda == "1":
    print("Twoja odpowiedz to:")
    print(int(Liczba_pierwsza) + int(Liczba_druga))
    koniec = input("Dziekuje za korzystanie z kalkulatora, napisz 'koniec', zeby wyjsc z programu: ")
    if koniec == "koniec":
        quit()

if metoda == "2":
    print("Twoja odpowiedz to:")
    print(int(Liczba_pierwsza) - int(Liczba_druga))
    koniec = input("Dziekuje za korzystanie z kalkulatora, napisz 'koniec', zeby wyjsc z programu: ")
    if koniec == "koniec":
        quit()

if metoda == "3":
    print("Twoja odpowiedz to:")
    print(int(Liczba_pierwsza) * int(Liczba_druga))
    koniec = input("Dziekuje za korzystanie z kalkulatora, napisz 'koniec', zeby wyjsc z programu: ")
    if koniec == "koniec":
        quit()

if metoda == "4":
    print("Twoja odpowiedz to:")
    print(int(Liczba_pierwsza) / int(Liczba_druga))
    koniec = input("Dziekuje za korzystanie z kalkulatora, napisz 'koniec', zeby wyjsc z programu: ")
    if koniec == "koniec":
        quit()