def format_data(name, age):
    if age < 0 or age > 130:
        return "Некоректний вік. Вік повинен бути в діапазоні від 0 до 130"
    return f"Привіт, {name}! Твій вік — {age}"


def main():
    try:
        name = input("Введіть ваше ім'я: ")
        age = int(input("Введіть ваш вік: "))
        result = format_data(name, age)
        print(result)
    except ValueError:
        print("Помилка: введіть коректний вік.")


if __name__ == "__main__":
    main()
