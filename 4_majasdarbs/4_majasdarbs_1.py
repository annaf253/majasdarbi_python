#!/usr/bin/env python3
'''
Python  mājasdarbs Nr.4-1

Uzdevums: aizpildīt vietas ar atzīmi TODO
'''
# set(draugs for dic in [Janis, Andris] for draugs in dic.keys())

## Jānis un Andris savu draugu telefonnumurus ir saglabājuši vārdnīcā.
Janis = {"Andris" : "041123451", "Martins" : "041123457", "Santa" : "041123458", "Kristine" : "041123459"}
Andris = {"Janis" : "041123456", "Martins" : "041123457", "Santa" : "041123458", "Kristina" : "041123450"}

## Uzdevums 1 - Izvadīt to draugu vārdus, kuru numuri ir vienādi
numri = set(draugs for draugs in Andris.keys() if draugs in Janis.keys())
## Atkomentēt assert testu, lai pārbaudītu rezultātu
assert numri == {'Martins', 'Santa'}
print("vienādi numuri ir ", numri)

## Uzdevums 2 - Izvadīt to draugu vārdus, kuru numuri ir satopami Jāņa vārdnīcā, be nav Andra
numri = set(draugs for draugs in Janis.keys() if draugs not in Andris.keys()) 
## Atkomentēt assert testu, lai pārbaudītu rezultātu
assert numri == {'Andris', 'Kristine'}
print("Jāņa vārdnīcā ir unikāli sekojošie draugi: ", numri)

## Uzdevums 3 - Izvadīt to draugu vārdus, kuru numuri ir sastopami TIKAI Jāņa vārdnīcā vai TIKAI Andra vārdnīcā (unikāli draugi)
numri = set([draugs for draugs in Andris.keys() if draugs not in Janis.keys()] + [draugs for draugs in Janis.keys() if draugs not in Andris.keys()])
## Atkomentēt assert testu, lai pārbaudītu rezultātu
assert numri == {'Janis', 'Andris', 'Kristine', 'Kristina'}
print("Unikāli draugi ir ", numri)

## Uzdevums 4 - Martins paziņo Jānim un Andrim ka maina telefona numuru. Modificēt abu vārdnīcas
Janis['Martins'] = "041123400"
Andris['Martins'] = "041123400"
## Atkomentēt assert testu, lai pārbaudītu rezultātu
assert Janis == {'Andris': '041123451', 'Martins': '041123400', 'Santa': '041123458', 'Kristine': '041123459'}
assert Andris == {'Janis': '041123456', 'Martins': '041123400', 'Santa': '041123458', 'Kristina': '041123450'}
print("Jāņa Vārdnīca ", Janis)
print("Andra Vārdnīca ", Andris)

## Uzdevums 5 - Andris iepazīstas ar Tomu, kura telefonnumurs ir 041999888. Ievietot Andra vārdnicā jauno draugu.
Andris['Toms'] = "041999888"
## Atkomentēt assert testu, lai pārbaudītu rezultātu 
assert Andris == {'Janis': '041123456', 'Martins': '041123400', 'Santa': '041123458', 'Kristina': '041123450', 'Toms': '041999888'}
print("Andra Vārdnīca ", Andris)

## Uzdevums 6 - Jānis sastrīdās ar Santu un grib izdzēst viņas numuru.
Janis.pop('Santa')
## Atkomentēt assert testu, lai pārbaudītu rezultātu
assert Janis == {'Andris': '041123451', 'Martins': '041123400', 'Kristine': '041123459'}
print("Jāņa Vārdnīca ", Janis)