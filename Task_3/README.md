# Uwagi początkowe:
- Do tego zadania trzeba zapronować rozwiązanie. Złożoność jest ważna, ale nie najważniejsza
- Zadanie może niewyjść, ale należy wtedy przedstawić swój pomysł na rozwiązanie i analiza dlaczego nie jest dobre (nie chodzi o implementacje) :)
- Do tego zadania zostały wygenerowane dane - znajdziesz je w repozytorium
- Niekorzystamy z gotowych rozwiązań (m. in.) bibliotek do rozwiązania problemu. Można wykorzystać je do analizy wydajnościowej (porównać ze swoim rozwiązaniem).
- zwizualizuj rozwiązanie
- *przestrzeń można zdyskretyzować tzn. podzielić na skonczoną liczbe punktów/elementów*

# Zadanie 1: (5 pkt)

W odległej krainie płynającej miodem i mlekiem rozwija się prężnie sieć niewielkich sklepów spożywczych ozdobiona zielonym logo. Głównym mechanizmem tej sieci sklepików jest agresywna polityka zajmowania każdej przestrzeni dostępnej w danej miejscowości. Jako, że jesteś młodym agentem nieruchomości a zarem dobrym przyjacielem dyrektora lokalnego odziału w mieście królów, dostałeś ambitne zadanie - wybranie nowej lokalizacji. Zakładając, że masz nieograniczone fundusze a głównym kryterium jest ograniczenie tzw. *wewnętrznego kanibalizmu* to na podstawie otrzymanych danych opracuj i zaimplementuj algorytm, który zaproponuje wszystkie możliwe optymalne lokalizacje oraz wybierze tą najlepszą.

## Punktacja:
- algorytm zaproponuje optymalne lokalizacje w pesymistycznym czasie większym niż/równym n^2 (3 pkt, typowy brute force) albo mniejszym (4 pkt)
- algorytm do wyboru najlepszej lokalizacji będzie działać w czasie mniejszym niż n^2 (1 pkt)
- analia problemu: rozpatrzenie możliwych przypadków (+ skrajnych) (1 pkt)
- implementacja innych, dodatkowych algorytmów (1pkt za każdy, maksymalnie 3pkt)
- analiza wydajnościowa swojego rozwiązania względem innego rozwiązania (kolegi, funkcji bibliotecznej itp.) (1pkt)

## Dane wejściowe:
- w repozytorium znajdziecie plik z danymi testowymi - jest to zwyczajny zbiór punktów w schemacie: ID X Y
- wymiar przestrzeni: 1x1
- znajdziecie także rysunki przedstawiające dane testowe wraz z przykładowym diagramem woronoja

## Podpowiedź:
  - diagramy woronoja mogą być przydatne (ale nie są konieczne!):
    - https://cfbrasz.github.io/Voronoi.html
    - https://www.reddit.com/r/explainlikeimfive/comments/5tsxju/eli5voronoi_diagrams/
    - https://mathworld.wolfram.com/VoronoiDiagram.html
  - maksymalna liczba pkt. do zdobycia: 5 - czyli można się ratować w inny sposób
  - inne metody też są ok np. heurestyczne (w tym przypadku złożoność nie będzie brana pod uwagę przy ocenie)
  - dodatkowe algorytmy nie muszą być optymalne, natomiast mogą być ciekawe :)
    
