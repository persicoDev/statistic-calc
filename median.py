def get_median():
    number_array = list()
    number_index = int(input("Inserisci il numero dei numeri: "))
    for i in range(number_index):
        number_array.append(float(input("Inserisci il numero : ")))
    number_array = sorted(number_array)
    if number_index % 2 == 1:
        return number_array[number_index//2]
    elif number_index % 2 == 0:
        even_number_result = (number_array[(number_index//2)-1] + number_array[number_index//2])/2 
        return even_number_result   