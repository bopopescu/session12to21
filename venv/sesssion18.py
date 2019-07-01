import numpy as np

numbers=[10,20,30,40,50]
print(numbers,type(numbers))

array=np.array(numbers)
print(array,type(array))
print(len(array))
print(array[0])
print()

array[2]=222

array2=np.append(array,[11,12,13])
print(array2)


#itrate in array
for elm in array:
    print(elm)