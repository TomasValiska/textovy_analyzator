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


users = ["bob", "ann", "mike", "liz"]
passwwords = ["123", "pass123", "password123", "pass123"]

username = input("username: ")
password = input("password: ")

if username in users:
  zadane_jmeno = username
  if password == passwwords[users.index(zadane_jmeno)]:
    print("-" * 40, f"\nWelcome to the app, {username}.\nWe have 3 texts to be analyzed.")
    print("-" * 40)
    selection = input("Enter a number btw. 1 and 3 to select: ")
    print("-" * 40)
    if selection.isdigit() == True:
      numeric_input = int(selection)
      if numeric_input in range (1,4):
        
        
        if numeric_input == 1:
          slova = TEXTS[0].split()
          
          pocet_slov = len(slova)
          
          title = 0
          for s in slova:
            if s.istitle():
              title += 1

          upper = 0
          for u in slova:
            if u.isupper() and u.isalpha():
              upper += 1

          lower = 0
          for l in slova:
            if l.islower():
              lower += 1

          digit = 0
          for d in slova:
            if d.isdigit():
              digit += 1

          sum_digit = 0
          for sd in slova:
            if sd.isdigit():
              sum_digit += int(sd)
          
          print(f"There are {pocet_slov} words in the selected text.\nThere are {title} titlecase words.")
          print(f"There is {upper} uppercase word.\nThere are {lower} lowercase words.")
          print(f"There are {digit} numeric strings.\nThe sum of all the numbers {sum_digit}.")



          texts_bez = TEXTS[0].replace(",", "").replace(".", "")
          slova_1 = texts_bez.split()
          length_seq = []
          sum_occur = {}

          for sw in slova_1:
            length_seq.append(len(sw))

          for so in length_seq:
            if so not in sum_occur:
              sum_occur.update({so:1})
            elif so in sum_occur:
              sum_occur[so] += 1
          
          sorted_so = sorted(sum_occur.items())

          print("-" * 40)
          print("{:>3}|{:^14}|{:<3}".format("LEN", "OCCURENCES", "NR."))
          print("-" * 40)

          for key, value in sorted_so:
            print("{:>3}|{:^14}|{:<3}".format(key, "*" * value, value))
        

        
        elif numeric_input == 2:
          slova = TEXTS[1].split()
          
          pocet_slov = len(slova)

          title = 0
          for s in slova:
            if s.istitle():
              title += 1

          upper = 0
          for u in slova:
            if u.isupper() and u.isalpha():
              upper += 1

          lower = 0
          for l in slova:
            if l.islower():
              lower += 1

          digit = 0
          for d in slova:
            if d.isdigit():
              digit += 1

          sum_digit = 0
          for sd in slova:
            if sd.isdigit():
              sum_digit += int(sd)
          
          print(f"There are {pocet_slov} words in the selected text.\nThere are {title} titlecase words.")
          print(f"There is {upper} uppercase word.\nThere are {lower} lowercase words.")
          print(f"There is {digit} numeric string.\nThe sum of all the numbers {sum_digit}.")


          texts_bez = TEXTS[1].replace(",", "").replace(".", "")
          slova_1 = texts_bez.split()
          length_seq = []
          sum_occur = {}

          for sw in slova_1:
            length_seq.append(len(sw))

          for so in length_seq:
            if so not in sum_occur:
              sum_occur.update({so:1})
            elif so in sum_occur:
              sum_occur[so] += 1
          
          sorted_so = sorted(sum_occur.items())

          print("-" * 40)
          print("{:>3}|{:^17}|{:<3}".format("LEN", "OCCURENCES", "NR."))
          print("-" * 40)

          for key, value in sorted_so:
            print("{:>3}|{:^17}|{:<3}".format(key, "*" * value, value))
        
        

        elif numeric_input == 3:
          slova = TEXTS[2].split()
          
          pocet_slov = len(slova)

          title = 0
          for s in slova:
            if s.istitle():
              title += 1

          upper = 0
          for u in slova:
            if u.isupper() and u.isalpha():
              upper += 1

          lower = 0
          for l in slova:
            if l.islower():
              lower += 1

          digit = 0
          for d in slova:
            if d.isdigit():
              digit += 1

          sum_digit = 0
          for sd in slova:
            if sd.isdigit():
              sum_digit += int(sd)
          
          print(f"There are {pocet_slov} words in the selected text.\nThere are {title} titlecase words.")
          print(f"There is {upper} uppercase word.\nThere are {lower} lowercase words.")
          print(f"There are {digit} numeric strings.\nThe sum of all the numbers {sum_digit}.")


          texts_bez = TEXTS[2].replace(",", "").replace(".", "")
          slova_1 = texts_bez.split()
          length_seq = []
          sum_occur = {}

          for sw in slova_1:
            length_seq.append(len(sw))

          for so in length_seq:
            if so not in sum_occur:
              sum_occur.update({so:1})
            elif so in sum_occur:
              sum_occur[so] += 1
          
          sorted_so = sorted(sum_occur.items())

          print("-" * 40)
          print("{:>3}|{:^15}|{:<3}".format("LEN", "OCCURENCES", "NR."))
          print("-" * 40)

          for key, value in sorted_so:
            print("{:>3}|{:^15}|{:<3}".format(key, "*" * value, value))
      
      
      else:
        print("wrong input, terminating the program")
    else:
      print("wrong input, terminating the program")
  else:
    print("unregistered user, terminating the program")
else:
  print("unregistered user, terminating the program")







  
  