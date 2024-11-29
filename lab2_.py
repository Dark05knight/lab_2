# -*- coding: utf-8 -*-
from os import mkdir, path
import matplotlib.pyplot as plt
from array_generator import generate_random_array
from data_saver import save_sorted_data_to_file
from plot_saver import save_plot
from data_loader import load_data_from_file

# Реализация сортировки методом "Корзин"
def bucket_sort(arr):
    if not arr:
        return []
    min_val = min(arr)
    max_val = max(arr)
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]
    for num in arr:
        index = int(bucket_count * (num - min_val) / (max_val - min_val + 1))
        buckets[index].append(num)
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))
    return sorted_array

# Проверка расширения файла при сохранении графиков
def check_file_extension(filename, valid_extensions):
    if not any(filename.endswith(ext) for ext in valid_extensions):
        print(f"Неверное расширение файла. Добавьте одно из следующих: {valid_extensions}.")
        return False
    return True

# Сохранение графика с проверкой на существование файла
def save_plot(data: list, fname: str):
    valid_extensions = [".png", ".jpg", ".jpeg"]
    if not check_file_extension(fname, valid_extensions):
        return
    if path.exists(fname):
        print(f"Внимание: Файл '{fname}' уже существует.")
        overwrite = input("Перезаписать файл? (д/н): ").lower()
        if overwrite != 'д':
            print("График не сохранен.")
            return
    try:
        plt.plot(data)
        plt.title('Отсортированные данные')
        plt.xlabel('Индекс')
        plt.ylabel('Значение')
        plt.savefig(fname)
        plt.close()
        print(f"График сохранен в файл {fname}.")
    except Exception as e:
        print(f"Ошибка при сохранении графика: {e}")

# Главное меню
def display_menu():
    print("\nМеню:")
    print("1. Загрузить данные из файла")
    print("2. Сгенерировать случайный массив")
    print("3. Ввести числа вручную")
    print("4. Выйти")

# Ввод данных вручную с использованием цикла
def manual_input_loop():
    while True:
        manual_input = input("Введите числа, разделенные пробелами, или 'q' для выхода: ")
        if manual_input.lower() == 'q':
            return None
        try:
            data = [int(num) for num in manual_input.split()]
            return data
        except ValueError:
            print("Неверный ввод. Введите только целые числа.")

# Подменю
def display_submenu():
    print("\nПодменю:")
    print("1. Сохранить отсортированные данные в файл")
    print("2. Сохранить график")
    print("3. Вернуться в главное меню")

def main_menu():
    arr = []
    while True:
        display_menu()
        choice = input("Выберите опцию (1-4): ")

        if choice == "1":
            file_path = input("Введите путь к файлу: ")
            arr = load_data_from_file(file_path)
            if arr:
                arr = bucket_sort(arr)
                print("Отсортированный массив:", arr)

        elif choice == "2":
            try:
                size = int(input("Введите размер массива: "))
                min_value = int(input("Введите минимальное значение: "))
                max_value = int(input("Введите максимальное значение: "))
                arr = generate_random_array(size, min_value, max_value)
                print("Исходный массив:", arr)
                arr = bucket_sort(arr)
                print("Отсортированный массив:", arr)
            except ValueError:
                print("Неверный ввод. Введите целые числа.")

        elif choice == "3":
            arr = manual_input_loop()
            if arr is None:
                continue
            arr = bucket_sort(arr)
            print("Отсортированный массив:", arr)

        elif choice == "4":
            print("Программа завершена.")
            break

        else:
            print("Неверный выбор. Введите число от 1 до 4.")
            continue

        while True:
            display_submenu()
            sub_choice = input("Выберите опцию (1-3): ")

            if sub_choice == "1":
                sorted_dir = 'sorted/'
                if not path.exists(sorted_dir):
                    mkdir(sorted_dir)
                output_file = input("Введите имя файла для сохранения отсортированных данных: ")
                full_path = path.join(sorted_dir, output_file)
                if path.exists(full_path):
                    print(f"Внимание: Файл '{full_path}' уже существует.")
                    overwrite = input("Перезаписать файл? (д/н): ").lower()
                    if overwrite != 'д':
                        print("Данные не сохранены.")
                        continue
                save_sorted_data_to_file(full_path, arr)
                print(f"Отсортированные данные сохранены в файл {output_file}.")

            elif sub_choice == "2":
                imgs_dir = 'imgs/'
                if not path.exists(imgs_dir):
                    mkdir(imgs_dir)
                output_image = input("Введите имя файла для сохранения графика: ")
                save_plot(arr, path.join(imgs_dir, output_image))

            elif sub_choice == "3":
                break

            else:
                print("Неверный выбор. Введите 1, 2 или 3.")

# Запуск программы
if __name__ == "__main__":
    main_menu()