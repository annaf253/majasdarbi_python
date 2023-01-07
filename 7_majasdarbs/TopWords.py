#!/usr/bin/env python3
'''
Python 7 mājasdarbs Nr.2

Uzdevums: aizpildīt vietas ar atzīmi TODO

Izveidot klasi, kura pārveido 5. nodarbības mājasdarbu Nr. 2 saturu par klasi

'''
import matplotlib.pyplot as plt
import json

class TopWords:
    '''
    Izveidot klasi, kurai ir 2 publiskas metodes:
    - setVardnica -  definē failu
    - grafiks - izvada grafiku

    Klasei nav pieejami publiski parametri
    '''
    def set_dict(self, vardnicaFails):
        with open(vardnicaFails) as f:
            self.__vardnica = json.load(f)

    def get_bar_plot(self):
        # izsaucot šo metodi izvada bar tipa grafiku. dati ir parametrs __vardnica
        plt.figure(figsize=(11, 6))
        plt.bar(range(len(self.__vardnica)), list(self.__vardnica.values()))
        plt.xticks(range(len(self.__vardnica)), list(self.__vardnica.keys()))
        plt.xlabel("Biežums")
        plt.ylabel("Vārds")
        plt.title("Biežākie Vārdi")
        plt.show()        


if __name__ == "__main__":
    obj = TopWords()
    obj.set_dict("top_vardi.json")