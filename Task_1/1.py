from random import randint


def bubble(tab):
    if tab:
        for i in range(0, len(tab)):
            for j in range(i, len(tab)):
                if tab[i] > tab[j]:
                    a = tab[i]
                    tab[i] = tab[j]
                    tab[j] = a


def insertion(tab):
    if tab:
        for i in range(1, len(tab)):
            j = i
            while j > 0:
                if tab[j] < tab[j - 1]:
                    a = tab[j - 1]
                    tab[j - 1] = tab[j]
                    tab[j] = a
                    j -= 1
                else:
                    break


def selection(tab):
    if tab:
        for i in range(0, len(tab)):
            min_index = i
            for j in range(i, len(tab)):
                if tab[min_index] > tab[j]:
                    min_index = j

            a = tab[i]
            tab[i] = tab[min_index]
            tab[min_index] = a


tab = []
tab2 = []
tab3 = []
for i in range(0, 20):
    tab.append(randint(0, 100))
    tab2.append(randint(0, 100))
    tab3.append(randint(0, 100))


print('before sort')
print(tab)
print('after sort')
bubble(tab)
print(tab)
print('second tab before sort')
print(tab2)
print('second tab after sort')
insertion(tab2)
print(tab2)
print('third before sort')
print(tab3)
selection(tab3)
print('third after sort')
print(tab3)
