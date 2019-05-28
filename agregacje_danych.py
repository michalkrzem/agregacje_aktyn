import naglowek
import kopiowanie_danych
import pandas as pd
import numpy as np


"""Program ma obliczyć sumy dobowe i miesięczne na podstawie plików wsadowych. 
Wykorzystywane są zaimportowane moduły utworzone przez administratora. """

naglowek.wpisz_naglowek()
######################################################################################
kopiowanie_danych.kopiuj()
######################################################################################
promieniowanie = naglowek.pliki_param

for pl in promieniowanie:
    result = pd.read_csv(pl, error_bad_lines=False, index_col='Stacja', low_memory=False)

    print("Trwa obliczanie sum", pl)

    filtr = result >= 9999      # w przypadku braku wartości oznaczonej 9999 zamieniamy na NaN
    result[filtr] = np.NaN

    result.set_index(["Rok", "Miesiac", "Dzien"], inplace=True)     # określamy index
    result = result.stack(dropna=True).to_frame("Sumy")             # transformujemy kolumny na wiesze

    sum_miesieczna = result.groupby(by=["Rok", "Miesiac"]).agg("sum")   # grupujemy i obliczamy sumy
    sum_dobowa = result.groupby(by=["Rok", "Miesiac", "Dzien"]).agg("sum")

    sum_dobowa.to_csv('wyniki_dobowe' + pl)
    sum_miesieczna.to_csv('wyniki miesieczne' + pl)

