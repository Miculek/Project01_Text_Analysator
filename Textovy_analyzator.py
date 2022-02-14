# autor: Mičulek Martin
#  ----------------------------| Textový analyzátor |------------------------------------

# - tento program provede jednoduchou analýzu zadaného textu

#-------------------------------- načtení textu ze souboru ------------------------------

import task_template
TEXTS = task_template.TEXTS

oddelovac = "-" * 60
uzivatele = {"bob" : "123", "ann" : "pass123", "mike" : "password123", "liz" : "pass123" }

#------------------------------ ověření uživatele a uvítání -----------------------------
# -------- podmínky tvořím tak, ať nemusím stále posouvat kod odsazováním ---------------

uzivatel = (input("username:")).lower()
heslo = input("password:")

if uzivatel not in uzivatele.keys() or heslo != uzivatele.get(uzivatel):
    print("unregistered user, terminating the program..")
    exit()

print(oddelovac)
print(f"Welcome to the app, {uzivatel.title()}. We have 3 texts to be analyzed.")
print(oddelovac)
cislo_textu = input("Enter a number btw. 1 and 3 to select:")
print(oddelovac)

#------------------------------- kontrola volby čísla textu -----------------------------

if cislo_textu not in {"1", "2", "3"} or not cislo_textu.isnumeric():
    print("Nenapsal jsi číslo, nebo je číslo mimo rozsah volby, terminating the program..")
    exit()

# ---------vyberu text, řetězec rozdělím na slova, tá očistím od nežádoucích znaku ---------

TEXT = TEXTS[int(cislo_textu) -1]
slova_textu = TEXT.split()
cista_slova = [slovo.strip(",.!?") for slovo in slova_textu]

# ---------------------- dám vypoctené výstupy do slovniku "analyza" --------------------
analyza = {
    "pocet_slov" : len(cista_slova),
    "titlecase" : 0,
    "uppercase" : 0,
    "lowercase" : 0,
    "numeric" : 0,
    "sum_numbers" : 0
}

for slovo in cista_slova:
    if slovo.istitle():
        analyza["titlecase"] += 1
    if slovo.isupper():                         # možna and slovo.isalpha()  nevím "30N"
        analyza["uppercase"] += 1
    if slovo.islower():
        analyza["lowercase"] += 1
    if slovo.isnumeric():
        analyza["numeric"] += 1
        analyza["sum_numbers"] += int(slovo)

# -------------------------- výpis textové analýzy --------------------------------------

print("There are {} words in the selected text.".format(analyza["pocet_slov"]))
print("There are {} titlecase words.".format(analyza["titlecase"]))
print("There are {} uppercase words.".format(analyza["uppercase"]))
print("There are {} lowercase words.".format(analyza["lowercase"]))
print("There are {} numeric strings.".format(analyza["numeric"]))
print("The sum of all the numbers", analyza["sum_numbers"])
print(oddelovac)
print("NR.|", "OCCURENCES".center(14), "|LEN")
print(oddelovac)

#----------------------------------- sloupcový graf délky slov --------------------------

for index, slovo in enumerate(cista_slova, 1):
    print("{:>3}|{:<16}|{}".format(index,"*" * len(slovo), len(slovo)))
