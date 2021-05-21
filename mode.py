from statistics import mode

def get_mode():
    number_array = list()
    number_index = int(input("Inserisci il numero dei numeri: "))
    for i in range(number_index):
        number_array.append(float(input("Inserisci il numero : ")))
    return (mode(number_array))