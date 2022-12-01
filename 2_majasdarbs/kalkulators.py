import sys
from calc import summa, atnemsana, multiplikacija, dalisana, eksponenta, check_float

def main():
    if len(sys.argv) < 4:
        exit()
    else:
        skaitlis_1 = sys.argv[1]
        skaitlis_1 = check_float(skaitlis_1)
        skaitlis_2 = sys.argv[3]
        skaitlis_2 = check_float(skaitlis_2)
        ievade = sys.argv[2]

        if ievade == '+':
            print("rezultāts: ", summa(skaitlis_1,skaitlis_2))
        elif ievade == '-':
            print("rezultāts: ", atnemsana(skaitlis_1,skaitlis_2))
        elif ievade == '*':
            print("rezultāts: ", multiplikacija(skaitlis_1,skaitlis_2))     
        elif ievade == '/':
            print("rezultāts: ", dalisana(skaitlis_1,skaitlis_2))  
        elif ievade == 'eksp':
            print("rezultāts: ", eksponenta(skaitlis_1,skaitlis_2))          
        else:
            print("operācija nav atrasta.")
            exit()

if __name__ == "__main__":
    main()