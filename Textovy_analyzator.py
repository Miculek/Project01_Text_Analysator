# autor: Mičulek Martin
#  ------------------------| Textový analyzátor |--------------------------------

#  Textový analyzátor - tento program provede jednoduchou analýzu zadaného textu


"""
+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

oddelovac = "-" * 60
uzivatele = {"bob" : "123", "ann" : "pass123", "mike" : "password123", "liz" : "pass123" }

uzivatel = (input("username:")).lower()
heslo = input("password:")

if uzivatel not in uzivatele.keys() or heslo != uzivatele.get(uzivatel):                         #ověření uživatele
    print("unregistered user, terminating the program..")
    exit()

print(oddelovac)
print(f"Welcome to the app, {uzivatel.title()}. We have 3 texts to be analyzed.")
print(oddelovac)
cislo_textu = input("Enter a number btw. 1 and 3 to select:")
print(oddelovac)

if cislo_textu not in {"1", "2", "3"} or not cislo_textu.isnumeric():                      # kontrola volby čísla textu
    print("Nenapsal jsi číslo, nebo je číslo mimo rozsah volby, terminating the program..")
    exit()


TEXT = TEXTS[int(cislo_textu) -1]            # vyberu text, řetězec rozdělím na slova, tá očistím od nežádoucích znaku
slova_textu = TEXT.split()
cista_slova = [slovo.strip(",.!?") for slovo in slova_textu]

analyza = {
    "pocet_slov" : len(cista_slova),
    "titlecace" : 0,
    "uppercase" : 0,
    "lovercase" : 0,
    "numeric" : 0,
    "sum_numbers" : 0
}

for slovo in cista_slova:                                           # dám vypoctené výstupy do slovniku "analyza"
    if slovo.istitle():
        analyza["titlecace"] += 1
    if slovo.isupper() and slovo.isalpha():                         # možna and slovo.isalpha()  nevím "30N"
        analyza["uppercase"] += 1
    if slovo.islower():
        analyza["lovercase"] += 1
    if slovo.isnumeric():
        analyza["numeric"] += 1
        analyza["sum_numbers"] += int(slovo)


print("There are {} words in the selected text.".format(analyza["pocet_slov"]))
print("There are {} titlecase words.".format(analyza["titlecace"]))
print("There are {} uppercase words.".format(analyza["uppercase"]))
print("There are {} lowercase words.".format(analyza["lovercase"]))
print("There are {} numeric strings.".format(analyza["numeric"]))
print("The sum of all the numbers" ,analyza["sum_numbers"])
print(oddelovac)
print("NR.|", "  OCCURENCES  ", "|LEN")
print(oddelovac)
i = 0
for slovo in cista_slova:                                                          # sloupcový graf délky slov
    i += 1
    print("{:>3}|{:<16}|{}".format(i,"*" * len(slovo), len(slovo)))
