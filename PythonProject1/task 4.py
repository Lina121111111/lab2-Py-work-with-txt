import re

def extract_data_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
    phones = re.findall(r'\+7-\d{3}-\d{3}-\d{2}-\d{2}', text)
    capital_words = re.findall(r'\b[A-ZА-ЯЁ][a-zа-яё]*\b', text)

    return emails, phones, capital_words

def save_to_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(f"{item}\n")

def main():
    emails, phones, capital_words = extract_data_from_file('text.txt')
    save_to_file('emails.txt', emails)
    save_to_file('phones.txt', phones)
    save_to_file('capital_words.txt', capital_words)

if __name__ == "__main__":
    main()