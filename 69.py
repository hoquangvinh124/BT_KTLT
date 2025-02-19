from datetime import datetime, timedelta

class Book:
    def __init__(self, book_id, title, author, genre, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available

    def edit_book(self, title=None, author=None, genre=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if genre:
            self.genre = genre

    def __str__(self):
        return f"{self.title} by {self.author} ({'Available' if self.available else 'Not Available'})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_books(self, book_id=None, title=None, author=None, genre=None):
        results = [book for book in self.books if
                   (book_id is not None and book.book_id == book_id) or
                   (title is not None and title.lower() in book.title.lower()) or
                   (author is not None and author.lower() in book.author.lower()) or
                   (genre is not None and genre.lower() in book.genre.lower())]
        return results


class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email

    def edit_member(self, name=None, email=None):
        if name:
            self.name = name
        if email:
            self.email = email

    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id})"


class BookLoanForm:
    def __init__(self, loan_id, member, book, borrow_date=None, return_date=None):
        self.loan_id = loan_id
        self.member = member
        self.book = book
        if self.book.available:
            self.book.available = False
            self.borrow_date = borrow_date if borrow_date else datetime.now()
            self.due_date = self.borrow_date + timedelta(days=14)  # Giả sử thời gian mượn mặc định là 14 ngày
            self.return_date = return_date
        else:
            raise ValueError("Book is not available for borrowing")

    def return_book(self):
        self.return_date = datetime.now()
        self.book.available = True
        return self.calculate_late_fee()

    def calculate_late_fee(self):
        if not self.return_date:
            return 0  # Chưa trả sách, không tính phí

        late_days = (self.return_date - self.due_date).days
        return max(0, late_days * 2000)  #Giả sử phí trễ: 2000 VND/ngày

    def __str__(self):
        status = "Returned" if self.return_date else "Not Returned"
        return f"Loan ID: {self.loan_id} - {self.book.title} borrowed by {self.member.name} ({status})"


#Thêm sách
book1 = Book(1, "Harry Potter", "J. K. Rowling", "Magic")
book2 = Book(2, "Detective Conan", "Aoyama Gosho", "Fiction")
library = Library()
library.add_book(book1)
library.add_book(book2)

#Tìm sách
print([book.__str__() for book in library.search_books(genre="Fiction")])
print([book.__str__() for book in library.search_books(book_id=1)])

#Thêm thành viên
member1 = Member(1, "Vinh", "vinhhq234112e@st.uel.edu.vn")
print(member1)

#Mượn sách
loan1 = BookLoanForm(1, member1, book1)
print(book1)
print(book2)
print(loan1)

# Giả sử trả sách muộn 5 ngày
loan1.return_date = loan1.due_date + timedelta(days=5)
print(f"Late fee: {loan1.calculate_late_fee()} VND")
loan1.return_book()

# Chỉnh sửa thông tin sách và thành viên
book1.edit_book(title="Doraemon", author="Fujiko Fujio")
member1.edit_member(name="Nguoi ao den bi an", email="kaitokid@gmail.com")
print(book1)
print(member1)

