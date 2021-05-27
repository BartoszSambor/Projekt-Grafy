# Projekt-Grafy

**Projekt zaliczeniowy na zajęcia z Teorii Grafów.**


## Struktura projektu

Folder **Algorithm** zawiera implementację struktury grafu oraz algorytmu Bellmana-Forda w jezyku Python.
W **Analysis** znajduję się rozwiązanie części teoretycznej - zadania 1-8 oraz analiza algorytmu.

## Uruchamianie programu
**Wymagania**
Zainstalowany Python 3.1 lub nowszy.

**Uruchamianie**
Uruchamiamy plik main.py" w folderze Algorithm, każde środowisko powinno sobie dać radę, albo można użyć wiersza poleceń:
>python3 main.py

**Dane wejściowe**
Podajemy względną ścieżkę do pliku w którym zapisana jest reprezentacja grafu, dla przykładowych grafów w repozytorium (w folderach Algorithm i Data) będzie to wyglądać tak:
> exampleGraph1.json
> ../Data/exampleGraph2.json
> ../Data/exampleGraph3.txt
Następnie enter i wpisujemy numer wierzchołka z którego algorytm ma rozpocząć działanie.

**Dane wyjścione**
Program wypisuje zbiór, w którym klucze są indeksami wierzchołków, a wartości są minimalnymi odległościami z wierzchołka początkowego.


## Budowa pliku z grafem
Plik (typu .json lub .txt) ma zawierać listę sąsiedztwa wzbogaconą o wagę krawędzi, wierzchołki ponumerowane kolejnymi liczbami całkowitymi nieujemnymi, wagi to dowolne liczby całkowite, 
najprościej wytłumaczyć na przykładzie:
>[{"1": "7"},      
>{"0": "7", "2": "-1", "3": 10}, 
>{}.
>{"0": "2", "1": "2"}]

Wierzchołek o indeksie 0 jest połączony krawędzią o wadze 7  z wierzchołkiem 1
wierzchołek 1 jest połączony z zerowym wagą 7, z drugim wagą -1 i z trzecim wagą 10,
wierzchołek 2 nie ma żadnych krawędzi wychodzących,
wierzchołek 3 jest połączony z zerowym wagą 2 i z pierwszym wagą 2
