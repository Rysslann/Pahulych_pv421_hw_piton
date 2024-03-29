def main():
    try:
        name = input("Введіть ваше ім'я: ")
        age = int(input("Введіть ваш вік: "))

        if age < 0 or age > 130:
            raise ValueError("Некоректний вік. Вік повинен бути в діапазоні від 0 до 130")

        print(f"Привіт, {name}! Твій вік — {age}")
    except ValueError as ve:
        print(f"Помилка: {ve}")


if __name__ == "__main__":
    main()
