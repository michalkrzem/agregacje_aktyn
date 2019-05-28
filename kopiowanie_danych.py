from glob import glob
import naglowek


def kopiuj():
    '''
    Funkcja ma za zadanie skopiować dane z odpowiednimi parametrami do odpowiednich plików
    z pominięciem zbędnych informacji zawartych w plikach. Uwzględnia liczbę godzin
    dla jakich są wykonywane pomiary (4-21  ;   1-24)
    '''

    dl_naglowka = 18        # standardowa długość nagłówka (4:21)
    dl_naglowka_q = 24      # długość nagłówka dla bilansu (1-24)
    files = glob("*.DAN")   # pobieramy listę nowo utworzonych plików

    pliki = []              # tworzymy listę, która ma docelowo zawierać nazwy plików
    for f in files:
        if files:
            with open(f, "r", -1, "utf-8") as csv:
                radiation = csv.read()
                print(radiation)    # wyświetlamy zawartość poszczegłolnych plików
                pliki.append(f)
    pliki.sort()

    for plik in pliki:                                          # dla każdego pliku tworzymy puste listy
        with open(plik, "r") as zawartosc:                      # będące magazynami na odpowiednie dane:
            calk = []                                           # promieniowanie całkowite
            rozpr = []                                          # promieniowanie rozproszone
            bil = []                                            # bilans całkowity
            odb = []                                            # promieniowanie odbite

            zawartosc_iter = iter(zawartosc)                    # tworzymy iterator

            linia = next(zawartosc_iter)
            days_count = int(linia.split()[-1])                 # na podstawie ilości dni podanej w pliku określamy ilość iteracji
            if days_count == 1:                                 # czasami za datą znajdują się jedynki,
                days_count = int(linia.split()[-2])             # w zależności od tego dobieramy odpowiednią wartość
            data_columns_to_read = 0                            # która wskazuje na wartość iteratora (zaczynamy od zera)
            for linia in zawartosc_iter:                        # dla każdej linii sprawdzamy, czy zaczyna się od
                if linia.startswith('Godzinne wartosci'):       # 'Godzinne...', jesli tak ostatni element linii
                    param = linia.split()[-1]                   # to parametr, którego dane znajdują się w pliku poniżej
                elif data_columns_to_read:                      # w przeciwnym wypadku zmniejszamy wartość iteratora
                    data_columns_to_read -= 1
                    name = plik[:3] + ',' + plik[3:5] + ',' + plik[6:8] + ','
                    if param == 'K!':
                        calk.append(name)    # do linii dodajemy nazwe stacji oraz datę oddzielając je przecinkami
                        calk.append(','.join(linia.split()) + '\n')   # dokładamy dane oddzielone przecinkami i przechodzimy do następnej linii
                    if param == 'D':
                        rozpr.append(name)   # powyższe, dla każdego parametru
                        rozpr.append(','.join(linia.split()) + '\n')
                    if param == 'Q':
                        bil.append(name)
                        bil.append(','.join(linia.split()) + '\n')
                    if param == 'K^':
                        odb.append(name)
                        odb.append(','.join(linia.split()) + '\n')
                elif linia:
                    linia_split = linia.split()
                    if (len(linia_split) == dl_naglowka or len(linia_split) == dl_naglowka_q) and param != 'U':
                        data_columns_to_read = days_count

            parametry = naglowek.pliki_param
            for parametr in parametry:              # zapisujemy dane do poszczególnych plików
                with open(parametr, "a+") as csv:
                    if parametr == 'calkowite.csv':
                        csv.writelines(calk)
                    if parametr == 'rozproszone.csv':
                        csv.writelines(rozpr)
                    if parametr == 'odbite.csv':
                        csv.writelines(odb)
                    if parametr == 'bilans.csv':
                        csv.writelines(bil)


if __name__ == "__main__":
    kopiuj()

