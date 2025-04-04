import math_operations as mo

def main():
    a = 10
    b = 5
    print(f"Summ: {mo.add(a, b)}")
    print(f"Difference: {mo.subtract(a, b)}")
    print(f"Composition: {mo.multiply(a, b)}")
    try:
        print(f"Division: {mo.divide(a, b)}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()