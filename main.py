#!/usr/bin/env python3
from type_calc.average  import get_average
from type_calc.median import get_median
from type_calc.mode import get_mode
from type_calc.standard_deviation import get_standard_deviation

def menu():
    while True:
        print('-------------------------------------------------')
        choice = int(input('\t1- esegui la media\n\t2- esegui la mediana\n\t3- esegui la moda\n\t4- esegui lo scarto quadratico medio\n\t0- uscita dal programma.\n\tinserimento:  '))
        if choice == 1:
            print(get_average())
        if choice == 2:
            print(get_median())
        if choice == 3:
            print(get_mode())
        if choice == 4: 
            print(get_standard_deviation())
        if choice == 0:
            break

if __name__ == '__main__':
    menu()
