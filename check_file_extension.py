# -*- coding: utf-8 -*-
# Проверка расширения файла при сохранении графиков
def check_file_extension(filename, valid_extensions):
    if not any(filename.endswith(ext) for ext in valid_extensions):
        print(f"Неверное расширение файла. Добавьте одно из следующих: {valid_extensions}.")
        return False
    return True
    valid_extensions = [".png", ".jpg", ".jpeg"]
    valid_extensions2 = [".py",".sln",".pyproj"]
    if check_file_extension(filename, valid_extensions2):
        print("файлы кода изменить запрещено")
        return
    if not check_file_extension(fname, valid_extensions):
        return
    if path.exists(fname):
        print(f"Внимание: Файл '{fname}' уже существует.")
        overwrite = input("Перезаписать файл? (д/н): ").lower()
        if overwrite != 'д':
            print("График не сохранен.")
            return
