import math

number_array = list()
average = delta = 0
number_index = input("Inserisci il numero dei numeri: ") 
for i in range(int(number_index)): 
    number_array.append(float(input("Inserisci il numero : "))) 
    average += float(number_array[i])
average /= float(number_index)
for i in range(int(number_index)):
    delta += (float(number_array[i]) - float(average)) 
    delta *= delta
delta /= float(number)
risultato = float(math.sqrt(delta))
print(f"Standard deviation = {str(risultato)}")