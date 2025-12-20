import json

class Books:
    def __init__(self, filename='book.txt'):
        self.filename = filename
        self.load_books()

    def load_books(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.books = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

    def add_book(self):
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

        for existing in self.books:
            if (existing["სახელწოდება"].lower() == title.lower() and
                    existing["ავტორი"].lower() == author.lower() and
                    existing["წელი"] == year):
                print("წიგნი უკვე რეგისტრირებულია სისტემაში.")
                return

        self.books.append({"სახელწოდება": title, "ავტორი": author, "წელი": year})
        self.save_books()
        print("წიგნი წარმატებით დარეგისტრირდა სისტემაში.")

    def save_books(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.books, file, indent=4)

    def show_books(self):
        if not self.books:
            print("სისტემაში წიგნი არ მოიძებნა.")
        else:
            print("სისტემაში ხელმისაწვდომია შემდეგი წიგნები:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. სახელწოდება: {book['სახელწოდება']}, ავტორი: {book['ავტორი']}, წელი: {book['წელი']}")

    def search_books(self):
        keyword = input("შეიყვანეთ საძიებო სიტყვა (წიგნის სახელწოდება ან ავტორი): ").lower()
        found = False
        print("ძიების შედეგები:")
        for book in self.books:
            if keyword in book['სახელწოდება'].lower() or keyword in book['ავტორი'].lower():
                print(f"სახელწოდება: {book['სახელწოდება']}, ავტორი: {book['ავტორი']}, წელი: {book['წელი']}")
                found = True
        if not found:
            print("საძიებო სიტყვის მიხედვით წიგნი არ მოიძებნა.")

class BookManager:
    def __init__(self):
        self.books = Books()

    def main(self):
        while True:
            print("\nწიგნების მართვის სისტემა")
            print("1. წიგნის დამატება")
            print("2. წიგნების ნუსხა")
            print("3. წიგნების ძიება")
            print("4. სისტემიდან გამოსვლა")
            choice = input("მიუთითეთ თქვენთვის სასურველი ოპერაცია (1-4): ")

            if choice == '1':
                self.books.add_book()
            elif choice == '2':
                self.books.show_books()
            elif choice == '3':
                self.books.search_books()
            elif choice == '4':
                print("თქვენ გამოხვედით სისტემიდან.")
                break
            else:
                print("ოპერაცია არ არის ვალიდური. სცადეთ ხელახლა.")

if __name__ == "__main__":
    manager = BookManager()
    manager.main()
