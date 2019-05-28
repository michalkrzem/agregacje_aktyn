from parametry import par

pliki_param = par()


def wpisz_naglowek():
    '''
        Funkcja tworzy oddzielne pliki dla poszczególnych parametrów, do których będą wpisywane dane
        w odpowiedniej formie do późniejszego przeliczania statystyk
    '''

    nag = '1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21   22   23   24'    # godziny pomiarów
    czas = 'Rok,Miesiac,Dzien,'                             # pierwsze elementy nagłówka
    naglowek = ','.join(nag.split()) + '\n'                 # dzielimy godziny przecinkami i tworzymy listę ze znakiem końca lini

    for pl in pliki_param:
        with open(pl, "a+") as csv:
            csv.writelines('Stacja,')                       # na samym początku zapisujemy do pliku znak " , "
            if pl == 'bilans.csv':                          # dla bilansu wpisujemy 24 godziny
                csv.writelines(czas)
                csv.writelines(naglowek)
            else:
                csv.writelines(czas)
                csv.writelines(naglowek[6:53])              # dla pozostałych parametrów wpisujemy godziny 4:21
                csv.writelines('\n')                        # na końcu każdej lini dodajemy \n, żeby następny
                                                            # wiersz, zaczynał się od nowej linii


if __name__ == "__main__":
    wpisz_naglowek()
