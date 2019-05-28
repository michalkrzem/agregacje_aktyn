def par():
    """Tworzymy listę parametrów, które użytkownik poda w pierwszym etapie programu"""

    pliki_parametry = []
    print("Podaj poniżej, jakie parametry chcesz sumować")
    pr_calkowite = input("Czy chcesz sumować dane dotyczące promieniownaia całkowitego? T/N ? ")
    pr_rozproszone = input("Czy chcesz sumować dane dotyczące promieniownaia rozproszonego? T/N ? ")
    pr_odbite = input("Czy chcesz sumować dane dotyczące promieniownaia odbitego? T/N ? ")
    pr_bilans = input("Czy chcesz sumować dane dotyczące bilansu promieniowania całkowitego? T/N ? ")

    if pr_calkowite.lower() == 't':
        pliki_parametry.append('calkowite.csv')
    if pr_rozproszone.lower() == 't':
        pliki_parametry.append('rozproszone.csv')
    if pr_odbite.lower() == 't':
        pliki_parametry.append('odbite.csv')
    if pr_bilans.lower() == 't':
        pliki_parametry.append('bilans.csv')

    return pliki_parametry


if __name__ == "__main__":
    par()
