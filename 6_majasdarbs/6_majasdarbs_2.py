#!/usr/bin/env python3
'''
Python 6 nodarbības mājasdarbs Nr.2

Uzdevums: aizpildīt vietas ar atzīmi TODO
'''
import matplotlib.pyplot as plt
import json
import numpy as np

# Importēt failu "top_vardi.json" un saglabāt atslēgas kā listi ar nosaukumu "x"
# vērtības kā listi ar nosaukumu "y"
with open('top_vardi.json') as f:
    data = json.load(f)

x = list(data.keys())
y = list(data.values())

# izveidot stabiņveidu grafiku kas rāda vārdu biežumu (y ass), Vārdus uz x ass
# piemērs ir mājasdarbu failā
fig, ax = plt.subplots()
ax.bar(range(len(data)), y)
plt.xticks(range(len(data)), x, rotation=90)
plt.show()



