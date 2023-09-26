"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Michal Krejčí
email: don.night@post.cz
discord: donnight
"""

uzivatele_hesla = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

from task_template import TEXTS as texts

jmeno = input("username: ")
heslo = input("password: ")

titlecase_words = 0
uppercase_words = 0
lowercase_words = 0
numeric_string = 0
sum_digits = 0
pocty_pismen = {}

if jmeno in uzivatele_hesla and uzivatele_hesla[jmeno] == heslo:
    print("-" * 40,
        "\nWelcome to the app,", jmeno,
        "\nWe have 3 texts to be analyzed."
    )
    print("-" * 40)
    cislo_textu = input("Enter a number btw. 1 and 3 to select: ")
    print("-" * 40)

    if cislo_textu.isdigit() and 1 <= int(cislo_textu) <= 3:
        vybrany_text = texts[int(cislo_textu) - 1].split()
        print("There are", len(vybrany_text), "words in the selected text.")

        for slovo in vybrany_text:
            slovo = slovo.replace(",", "").replace(".", "")
            if slovo.isalpha() and (slovo.istitle() or slovo.isupper()):
                titlecase_words += 1
            if slovo.isupper() and slovo.isalpha():
                uppercase_words += 1
            if slovo.islower():
                lowercase_words += 1
            if slovo.isdigit():
                numeric_string += 1
                sum_digits += int(slovo)
            delka_slova = len(slovo)
            if delka_slova in pocty_pismen:
                pocty_pismen[delka_slova] += 1
            else:
                pocty_pismen[delka_slova] = 1

        print("There are", titlecase_words, "titlecase words.")
        print("There are", uppercase_words, "uppercase words.")
        print("There are", lowercase_words, "lowercase words.")
        print("There are", numeric_string, "numeric strings.")
        print("The sum of all the numbers", sum_digits)
        print("-" * 40)

        sirka_sloupce = max(pocty_pismen.values()) + 2
        print(f"LEN|{'OCCURENCES':^{sirka_sloupce}}|NR.")
        print("-" * 40)

        for klic, hodnota in sorted(pocty_pismen.items()):
            hvezdy = "*" * hodnota
            print(f"{klic:3}|{hvezdy:<{sirka_sloupce}}|{hodnota}")

    elif cislo_textu.isdigit():
        print("Number is not in range.")
    else:
        print("Not a number.")

elif jmeno in uzivatele_hesla and uzivatele_hesla[jmeno] != heslo:
    print("Wrong password.")
else:
    print("Unregistered user, terminating the program..")
