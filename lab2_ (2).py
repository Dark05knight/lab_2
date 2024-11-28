# -*- coding: utf-8 -*-
from os import mkdir, path
from array_generator import generate_random_array  # Инструмент для создания случайных массивов
from data_saver import save_sorted_data_to_file  # Инструмент для сохранения отсортированных данных в файл
from plot_saver import save_plot  # Инструмент для сохранения графиков
from data_loader import load_data_from_file  # Инструмент для загрузки данных из файла

# Реализация Bucket Sort
def bucket_sort(arr):
    if not arr:
        return []

    # Определение минимального и максимального значения
    min_val = min(arr)
    max_val = max(arr)
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    # Распределение элементов по корзинам
    for num in arr:
        index = int(bucket_count * (num - min_val) / (max_val - min_val + 1))
        buckets[index].append(num)

    # Сортировка каждой корзины и их объединение
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))  # Использование `sorted()` для сортировки каждой корзины

    return sorted_array

# Отображение главного меню
def display_menu():
    print("\nМеню:")
    print("1. Загрузить данные из файла")
    print("2. Сгенерировать случайные массивы")
    print("3. Ввести числа вручную")
    print("4. Выйти")

# Отображение подменю
def display_submenu():
    print("\nПодменю:")
    print("1. Сохранить отсортированные данные в файл")
    print("2. Сохранить графики")
    print("3. Вернуться в главное меню")

# Основная функция
def main_menu():
    arr = []
    while True:
        display_menu()
        choice = input("Введите ваш выбор (1-4): ")  # Ввод выбора (1-4):
        
        if choice == "1":  # Загрузить данные из файла
            file_path = input("Введите путь к файлу: ")  # Ввод пути к файлу:
            arr = load_data_from_file(file_path)
            if arr:
                arr = bucket_sort(arr)  # Сортировка данных
                print("Отсортированный массив:", arr)  # Отображение отсортированного массива

        elif choice == "2":  # Сгенерировать случайные массивы
            try:
                size = int(input("Введите размер массива: "))  # Ввод размера массива:
                min_value = int(input("Введите минимальное значение: "))  # Ввод минимального значения:
                max_value = int(input("Введите максимальное значение: "))  # Ввод максимального значения:
                arr = generate_random_array(size, min_value, max_value)
                print("Оригинальный массив:", arr)
                arr = bucket_sort(arr)
                print("Отсортированный массив:", arr)
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите целые числа.")

        elif choice == "3":  # Ввести числа вручную
            manual_input = input("Введите числа, разделенные пробелами: ")  # Ввод чисел, разделенных пробелами:
            try:
                arr = [int(num) for num in manual_input.split()]
                arr = bucket_sort(arr)
                print("Отсортированный массив:", arr)
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите корректные числа.")

        elif choice == "4":  # Выйти
            print("Конец программы.")  # Конец программы.
            break

        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 4.")
            continue

        # Работа с подменю
        while True:
            display_submenu()
            sub_choice = input("Введите ваш выбор (1-3): ")  # Ввод выбора (1-3):
            
            if sub_choice == "1":  # Сохранить отсортированные данные в файл
                sorted_dir = 'sorted/'
                if not path.exists(sorted_dir):
                    mkdir(sorted_dir)
                output_file = input("Введите имя файла для сохранения отсортированных данных: ")  # Ввод имени файла:
                save_sorted_data_to_file(path.join(sorted_dir, output_file), arr)
                print(f"Отсортированные данные сохранены в {output_file}.")  # Данные сохранены.

            elif sub_choice == "2":  # Сохранить графики
                imgs_dir = 'imgs/'
                if not path.exists(imgs_dir):
                    mkdir(imgs_dir)
                output_image = input("Введите имя файла для сохранения графика: ")  # Ввод имени файла:
                save_plot(arr, path.join(imgs_dir, output_image))
                print(f"График сохранен в {output_image}.")  # График сохранен.

            elif sub_choice == "3":  # Вернуться в главное меню
                break

            else:
                print("Неверный выбор. Пожалуйста, введите 1, 2 или 3.")  # Неверный выбор.

# Запуск программы
if __name__ == "__main__":
    main_menu()