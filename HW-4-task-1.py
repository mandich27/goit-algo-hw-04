
def total_salary(path):
    try:
        total = 0
        count = 0
        with open(path, "r", encoding="utf-8") as file:           # Відкриваєм файл в режимі читання і режимі кодування utf-8
            for el in file:
                _, salary = el.strip().split(",")                 # Видаляємо пробіли і розділяємо елементи в файлі за допомогою коми
                total += int(salary)                              # Додаємо всі числа
                count += 1                                        # Рахуємо кожну ітерацію, одна ітерація одна людина
        average = total/count                                     # Ділимо суму на кількість ітерацій(людей)
        return total, average
    except FileNotFoundError:
        print("Файл не знайдено!")


if __name__== "__main__":
    path = "salaries.txt"                                        # Присвоюємо шлях до файла змінній path
    total, average = total_salary(path)                          # Викликаєм функцію


print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
