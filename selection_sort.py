def find_smallest(arr):
    smallest = arr[0] # Для хранения наименьшего значения
    smallest_index = 0 # Для хранения индекса наименьшего значения
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selestion_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr) # Находит наименьшений элемент в массиве
        newArr.append(arr.pop(smallest)) # Добавляет его в новый массив
    return newArr

print(selestion_sort([23, 4, 64, 34, 12, 78]))