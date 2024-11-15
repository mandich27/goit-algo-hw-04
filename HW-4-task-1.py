
def total_salary(path):
    try:
        total = 0
        count = 0
        with open(path, "r", encoding="utf-8") as file:           # Відкриваєм файл в режимі читання і режимі кодування utf-8
            for el in file:
                _, salary = el.strip().split(",")                 # Видаляємо пробіли і розділяємо елементи в файлі за допомогою коми
                if salary:
                    total += float(salary)                        # Додаємо всі числа переводимо в флоат
                    count += 1                                    # Рахуємо кожну ітерацію, одна ітерація одна людина
        if count == 0:                                            # Якщо в тексті не було числових значень, виводимо повідомлення про це, і повертаємо 0,0
           print("Текст не місттить цифрових значень заробітньої плати")
           return 0,0
        average = total/count                                     # Ділимо суму на кількість ітерацій(людей)
        return total, average
    
    except FileNotFoundError:
        print("Файл не знайдено!")
        return 0,0


if __name__== "__main__":
    path = "salaries.txt"                                        # Присвоюємо шлях до файла змінній path
    total, average = total_salary(path)                          # Викликаєм функцію


print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
