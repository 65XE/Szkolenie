def tabelka(imie, nazwisko, mail, nr, header=True):
    if header:
        print(f"| {'Imie'.ljust(15)} | {'Nazwisko'.ljust(15)} | {'e-mail'.ljust(20)} | {'Nr'.center(10)} |")
    print(f"| {imie.ljust(15)} | {nazwisko.ljust(15)} | {mail.ljust(20)} | {nr.rjust(10)} |")

tabelka("Pawel", "Kowalczyk", "pk@wp.pl", str(65))
tabelka("Miroslaw", "Fryc", "mf@wp.pl", str(123434), False)