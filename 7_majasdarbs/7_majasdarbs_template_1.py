#!/usr/bin/env python3
'''
Python 7 mājasdarbs Nr.1

Uzdevums: aizpildīt vietas ar atzīmi TODO

Izveidot jaunu datu tipu, kurš paņem vārdisku un skaitlisku vērtību, un pēc tam spēj atdod numeriskas vērtības
Datu tips atļauj sekojošos ievadvērtības:
- "one", "two", "three", "four", "five"
'''

class JaunsDatuTips:

    def __init__(self, vertiba):
        # pārbaudīt vērtību "vertiba" vai sastāv no atļautām skatiliskiem vārdiem
        # un izveidot loģiku, kas savieno "one" kā 1; "two" kā 2 utt.
        if vertiba in ["one", "two", "three", "four", "five"]:
            self.vertiba = vertiba
        else:
            print("Nepareiza vertiba!")
            self.vertiba = None
        
        self.value_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}

    def get_int(self):
        # kad tiek izsaukta metode atdod parametru "vertiba" kā integer datu tipu
        return self.value_dict[self.vertiba]

    def get_float(self):
        # kad tiek izsaukta metode atdod parametru "vertiba" kā float datu tipu
        int_vertiba = self.get_int()       
        return float(int_vertiba)

    def get_string(self):
        # kad tiek izsaukta metode atdod parametru "vertiba" kā string datu tipu
        return self.vertiba

if __name__ == "__main__":
    x1 = JaunsDatuTips("one")
    x2 = JaunsDatuTips("two")
    x3 = JaunsDatuTips("three")
    x4 = JaunsDatuTips("four")
    x5 = JaunsDatuTips("five")

    # Kad uzvedums izpildīts, var pārbaudīt vai rezultāts ir pareizs, atkomentējot assert

    assert x1.get_int()==1
    assert x2.get_int()==2
    assert x3.get_int()==3
    assert x4.get_int()==4
    assert x5.get_int()==5

    assert x1.get_float()==1.0
    assert x2.get_float()==2.0
    assert x3.get_float()==3.0
    assert x4.get_float()==4.0
    assert x5.get_float()==5.0

    assert x1.get_string()=="one"
    assert x2.get_string()=="two"
    assert x3.get_string()=="three"
    assert x4.get_string()=="four"
    assert x5.get_string()=="five"