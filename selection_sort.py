﻿def selection_sort2(arr: list):    
  #Описание:    
  #Функция реализует алгоритм сортировки выбором для списка.
  #Аргументы:    
  #- arr (list): Список данных, который нужно отсортировать.
  #Возвращает:    
  #- arr (list): Отсортированный список.
  #Примечание:   
  #Функция модифицирует исходный список, сортируя его в порядке возрастания.
    
  # Получение размера массива    
  array_size = len(arr) 
  # Проходим по всем элементам, кроме последнего, так как последний элемент
  # будет автоматически на своем месте после сортировки    
  for i in range(array_size - 1):
  # Устанавливаем начальный минимальный элемент на текущий индекс        
    min_idx = i
  # Ищем минимальный элемент в оставшейся части списка
    for j in range(i + 1, array_size):            
       # Если находим элемент меньше текущего минимального, обновляем
       # индекс минимального элемента            
       if arr[j] < arr[min_idx]:
          min_idx = j
        # Если нашли новый минимальный элемент, меняем его местами с текущим элементом        
       if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
