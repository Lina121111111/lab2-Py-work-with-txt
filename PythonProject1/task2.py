def divide_numbers():
    try:
        a = float(input("Input the first numer: "))
        b = float(input("Input the second numer: "))
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: division by zero.")
    except ValueError:
        print("Error: Entering non-numeric values.")

if __name__ == "__main__":
    divide_numbers()
