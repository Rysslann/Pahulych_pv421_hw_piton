def format_greeting(name, age):
    try:
        if age < 0 or age > 130:
            raise ValueError("Некоректний вік. Вік повинен бути в діапазоні від 0 до 130")
        return f"Привіт, {name}! Твій вік — {age}"
    except ValueError as ve:
        return f"Помилка: {ve}"


def main():
    name = input("Введіть ваше ім'я: ")
    try:
        age = int(input("Введіть ваш вік: "))
        result = format_greeting(name, age)
        print(result)
    except ValueError:
        print("Помилка: введіть коректний вік.")


if __name__ == "__main__":
    main()
