def main():
    numbers = []

    while True:
        try:
            num = float(input("Введіть додатне число (або негативне, щоб завершити введення): "))
            if num < 0:
                break  # EXIT
            numbers.append(num)
        except ValueError:
            print("Помилка: введіть число.")

    try:
        if any(num < 0 for num in numbers):
            raise ValueError("Виявлено від'ємне число.")
        total = sum(numbers)
        print(f"Сума всіх додатніх чисел: {total}")
    except ValueError as ve:
        print(f"Помилка: {ve}")


if __name__ == "__main__":
    main()
