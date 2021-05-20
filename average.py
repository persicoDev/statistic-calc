def get_average():
    number_array = list()
    average = 0
    number_index = input("Inserisci il numero dei numeri: ") 
    for i in range(int(number_index)): 
        number_array.append(float(input("Inserisci il numero : "))) 
        average += float(number_array[i])
    average /= float(number_index)
    return str(average)