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



database = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}


username = input("username: ")
password = input("password: ")


#Přihlášení uživatele, pokud je uživatel registrovaný, vypíše se pozdrav. Pokud není, program se ukončí.
if username in database.keys():
  zadane_jmeno = username
  if password == database[zadane_jmeno]:
    print("-" * 40, f"\nWelcome to the app, {username}.\nWe have 3 texts to be analyzed.")
    print("-" * 40)
  else:
    print("unregistered user, terminating the program")
    exit()
else:
  print("unregistered user, terminating the program")
  exit()

# Vstup uživatele. Pokud je chybný, ukončení programu. 
selection = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
print("-" * 40)
if selection.isdigit() == True:
  numeric_input = int(selection)
  if numeric_input not in range (1,len(TEXTS) + 1):
    print("wrong input, terminating the program")
    exit()
else:
  print("wrong input, terminating the program")
  exit()


# Analýza textu: výběr a rozdělení textu
if numeric_input:
  slova = TEXTS[numeric_input - 1].split()
          
  pocet_slov = len(slova)

#Analýza textu: počítání slov s velkým písmenem,
#počítání slov psaných pouze velkými písmeny,
#počítání slov psaných pouze malými písmeny,
#počítání čísel, součet čísel         
  title = 0
  upper = 0
  lower = 0
  digit = 0
  sum_digit = 0
  for s in slova:
    if s.istitle():
      title += 1
    if s.isupper() and s.isalpha():
      upper += 1
    if s.islower():
      lower += 1
    if s.isdigit():
      digit += 1
    if s.isdigit():
      sum_digit += int(s)
  
    
          
  print(f"There are {pocet_slov} words in the selected text.\nThere are {title} titlecase words.")
  print(f"There is {upper} uppercase word.\nThere are {lower} lowercase words.")
  print(f"There are {digit} numeric strings.\nThe sum of all the numbers {sum_digit}.")

# Výpis grafu: očištění od interpunkce a rozdělení textu  
  texts_bez = TEXTS[numeric_input - 1].replace(",", "").replace(".", "")
  slova_1 = texts_bez.split()
  
# Výpis grafu: seznam délek slov  
  length_seq = []
  sum_occur = {}
  for sw in slova_1:
    length_seq.append(len(sw))

# Výpis grafu: počítání délek slov
  for so in length_seq:
    if so not in sum_occur:
      sum_occur.update({so:1})
    elif so in sum_occur:
      sum_occur[so] += 1

# Výpis grafu: stanovení nejvyšší hodnoty           
  sorted_so = sorted(sum_occur.items()) 
  occur = 0
  for key, value in sorted_so:
    if value > occur:
      occur = value

# Výpis grafu: dynamická velikost prostředního sloupce grafu
  print("-" * 40)
  print("{:>3}|{:^{}s}|{:<3}".format("LEN", "OCCURENCES", occur, "NR."))
  print("-" * 40)

  for key, value in sorted_so:
    print("{:>3}|{:<{}s}|{:<3}".format(key, "*" * value, occur, value))