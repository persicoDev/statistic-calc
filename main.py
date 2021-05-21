#!/usr/bin/env python3
import average
import median
import mode
import standard_deviation

def menu():
    choice = int(input('1- esegui la media\n2- esegui la mediana\n3- esegui la moda\n4- esegui lo scarto quadratico medio: '))
    if choice == 1:
        print(average.get_average())
    if choice == 2:
        print(median.get_median())
    if choice == 3:
        print(mode.get_mode())
    if choice == 4: 
        print(standard_deviation.get_standard_deviation())

if __name__ == '__main__':
    menu()
