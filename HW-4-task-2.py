
def get_cats_info(path):
    cats_info = []                                                          # Створюємо пустий список cats_info
    try:
        with open(path, 'r', encoding= 'utf-8') as file:                    # Відкриваєм файл в режимі читання і режимі кодування utf-8
            for el in file:
                id, name, age = el.strip().split(',')                       # Видаляємо пробіли і розділяємо елементи в файлі за допомогою коми
                cats_info.append({'id' : id, 'name' : name, 'age' : age})   # Створюємо словник на кожну ітерацію
        return cats_info                                                    # Повертаєм створені словники в список cats_info
    except FileNotFoundError:
        print("Файл не знайдено!")

path = 'cats_info.txt'                                                      # Присвоюємо шлях до файла змінній path

cats_info = get_cats_info(path)                                             # Викликаєм функцію

print(cats_info)