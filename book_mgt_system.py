# Books Management System

import json

try:
    with open('book.txt', 'r', encoding='utf-8') as file:
        books = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    books = []

def add_book():
    while True:
        title = input("შეიყვანეთ წიგნის სახელწოდება: ").strip()
        if title:
            break
        print("წიგნის სახელწოდების შეყვანა სავალდებულოა.")
    while True:
        author = input("შეიყვანეთ წიგნის ავტორი: ").strip()
        if author:
            break
        print("წიგნის ავტორის შეყვანა სავალდებულოა.")
    while True:
        publication_year = input("შეიყვანეთ წიგნის გამოცემის წელი: ")
        try:
            year = int(publication_year)
            if year > 2025:
                print("გთხოვთ, სწორად მიუთითეთ წიგნის გამოცემის წელი.")
                continue
            break
        except ValueError:
            print("გთხოვთ წიგნის გამოცემის წელი შეიყვანოთ ციფრებით.")

    for existing in books:
        if (existing["სახელწოდება"].lower() == title.lower() and
                existing["ავტორი"].lower() == author.lower() and
                existing["წელი"] == year):
            print("წიგნი უკვე რეგისტრირებულია სისტემაში.")
            return

    books.append({"სახელწოდება": title, "ავტორი": author, "წელი": year})
    with open('book.txt', 'w', encoding='utf-8') as file:
        json.dump(books, file, indent=4)
    print("წიგნი წარმატებით დარეგისტრირდა სისტემაში.")

def show_books():
    if not books:
        print("სისტემაში წიგნი არ მოიძებნა.")
    else:
        print("სისტემაში ხელმისაწვდომია შემდეგი წიგნები:")
        for i, book in enumerate(books, 1):
            print(f"{i}. სახელწოდება: {book['სახელწოდება']}, ავტორი: {book['ავტორი']}, წელი: {book['წელი']}")

def search_books():
    keyword = input("შეიყვანეთ საძიებო სიტყვა (წიგნის სახელწოდება ან ავტორი): ").lower()
    found = False
    print("ძიების შედეგები:")
    for book in books:
        if keyword in book['სახელწოდება'].lower() or keyword in book['ავტორი'].lower():
            print(f"სახელწოდება: {book['სახელწოდება']}, ავტორი: {book['ავტორი']}, წელი: {book['წელი']}")
            found = True
    if not found:
        print("საძიებო სიტყვის მიხედვით წიგნი არ მოიძებნა.")

def main():
    while True:
        print("\nწიგნების მართვის სისტემა")
        print("1. წიგნის დამატება")
        print("2. წიგნების ნუსხა")
        print("3. წიგნების ძიება")
        print("4. სისტემიდან გამოსვლა")
        choice = input("მიუთითეთ თქვენთვის სასურველი ოპერაცია (1-4): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            show_books()
        elif choice == '3':
            search_books()
        elif choice == '4':
            print("თქვენ გამოხვედით სისტემიდან.")
            break
        else:
            print("ოპერაცია არ არის ვალიდური. სცადეთ ხელახლა.")

if __name__ == "__main__":
    main()