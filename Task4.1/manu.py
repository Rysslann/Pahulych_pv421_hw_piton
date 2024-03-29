def calculate_sum(numbers):
    return sum(numbers)


def main():
    try:
        numbers = []
        while True:
            try:
                num = float(input("Введіть число (або негативне, щоб завершити введення): "))
                if num < 0:
                    break
                numbers.append(num)
            except ValueError:
                print("Помилка: введіть число.")

        total = calculate_sum(numbers)
        print(f"Сума елементів списку: {total}")
    except ValueError as ve:
        print(f"Помилка: {ve}")


if __name__ == "__main__":
    main()
