
import re

def extract_dates_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    # Находим все даты в формате DD.MM.YYYY
    dates = re.findall(r'\b(\d{2})\.(\d{2})\.(\d{4})\b', text)
    return dates

def convert_dates(dates):
    # Преобразуем даты в формат YYYY-MM-DD
    converted_dates = [f"{year}-{month}-{day}" for day, month, year in dates]
    return converted_dates

def save_dates_to_file(filename, dates):
    with open(filename, 'w', encoding='utf-8') as file:
        for date in dates:
            file.write(f"{date}\n")

def main():
    dates = extract_dates_from_file('text.txt')
    converted_dates = convert_dates(dates)
    save_dates_to_file('dates.txt', converted_dates)

    # Сортируем даты по возрастанию
    sorted_dates = sorted(converted_dates)
    print("Sort dates:", sorted_dates)

if __name__ == "__main__":
    main()