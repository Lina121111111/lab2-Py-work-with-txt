def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file.readlines()]

def write_results_to_file(filename, total, average, maximum, minimum):
    with open(filename, 'w') as file:
        file.write(f"Summ: {total}\n")
        file.write(f"Average: {average}\n")
        file.write(f"Max: {maximum}\n")
        file.write(f"Min: {minimum}\n")

def main():
    numbers = read_numbers_from_file('data.txt')
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    write_results_to_file('result.txt', total, average, maximum, minimum)

if __name__ == "__main__":
    main()
