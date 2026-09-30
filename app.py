import markupsafe
from flask import Flask, render_template, request, abort, jsonify
app = Flask(__name__)

# 1. Danh sách BOOKS >= 4 cuốn
BOOKS = [
    {
        "id": 1,
        "title": "Lập trình Python cơ bản",
        "author": "Nguyễn Văn A",
        "year": 2023,
        "category": "Lập trình",
        "available": True,
    },
    {
        "id": 2,
        "title": "Flask Web Development",
        "author": "Miguel Grinberg",
        "year": 2018,
        "category": "Lập trình",
        "available": False,
    },
    {
        "id": 3,
        "title": "Đại số tuyến tính",
        "author": "Trần Văn B",
        "year": 2021,
        "category": "Toán học",
        "available": True,
    },
    {
        "id": 4,
        "title": "Hệ điều hành Mã nguồn mở",
        "author": "Lê Văn C",
        "year": 2022,
        "category": "Hệ thống",
        "available": True,
    },
]


def get_book_by_id(book_id):
    return next((b for b in BOOKS if b["id"] == book_id), None)


# 2. Trang chủ /
@app.route("/")
def index():
    total_books = len(BOOKS)
    available_books = sum(1 for b in BOOKS if b["available"])
    return render_template(
        "index.html", total_books=total_books, available_books=available_books
    )


# 3. /books : Bảng sách + Lọc category
@app.route("/books")
def book_list():
    raw_category = request.args.get("category", "")
    selected_category = str(markupsafe.escape(raw_category)) if raw_category else ""

    categories = sorted(list(set(b["category"] for b in BOOKS)))

    if selected_category:
        filtered_books = [b for b in BOOKS if b["category"] == selected_category]
    else:
        filtered_books = BOOKS

    return render_template(
        "books.html",
        books=filtered_books,
        categories=categories,
        selected_category=selected_category,
    )


# 4. /books/<int:book_id> : Chi tiết sách
@app.route("/books/<int:book_id>")
def book_detail(book_id):
    book = get_book_by_id(book_id)
    if not book:
        abort(404, description=f"Không có sách với ID = {book_id}")
    return render_template("detail.html", book=book)


# 5. API /api/books và /api/books/<int:book_id>
@app.route("/api/books")
def api_books():
    return jsonify(BOOKS)


@app.route("/api/books/<int:book_id>")
def api_book_detail(book_id):
    book = get_book_by_id(book_id)
    if not book:
        return jsonify({"error": f"Không có sách với ID = {book_id}"}), 404
    return jsonify(book)


# 6. Trang 404 tuỳ biến
@app.errorhandler(404)
def page_not_found(e):
    msg = getattr(e, "description", "Trang không tồn tại")
    return render_template("404.html", error_message=msg), 404


if __name__ == "__main__":
    app.run(debug=True)