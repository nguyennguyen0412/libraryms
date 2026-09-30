# Du an LibraryMS v0.1 - Quan ly thu vien don gian

## 1. Gioi thieu du an
Ung dung web quan ly thu vien don gian (Library Management System v0.1) duoc xay dung bang Flask (Python). 
Ho tro hien thi danh sach sach, loc theo the loai, xem chi tiet sach, cung cap API JSON va xu ly trang loi 404 tuy bien.

## 2. Huong dan cai dat va chay ung dung

Bao gom cac buoc sau:
- Tao va kich hoat moi truong ao:
  python -m venv venv
  venv\Scripts\activate

- Cai dat thu vien Flask:
  pip install flask

- Khoi chay ung dung:
  python app.py

Ung dung se chay tai dia chi: http://127.0.0.1:5000

## 3. Cac duong dan kiem thu giao dien HTML (Trinh duyet)

- Trang chu (Tong quan thu vien):
  http://127.0.0.1:5000/

- Danh sach toan bo sach (kem thanh loc the loai):
  http://127.0.0.1:5000/books

- Loc sach theo the loai Lap trinh:
  http://127.0.0.1:5000/books?category=L%E1%BA%ADp+tr%C3%ACnh

- Trang chi tiet sach hop le (ID = 1):
  http://127.0.0.1:5000/books/1

- Trang 404 HTML khi sach khong ton tai (ID = 999):
  http://127.0.0.1:5000/books/999

## 4. Cac lenh cURL kiem thu API (Du lieu JSON)

- Lay danh sach toan bo sach (JSON):
  curl -X GET http://127.0.0.1:5000/api/books

- Lay thong tin chi tiet sach co ID = 1 (JSON):
  curl -X GET http://127.0.0.1:5000/api/books/1

- Kiem thu loi 404 API khi sach khong ton tai (JSON):
  curl -X GET http://127.0.0.1:5000/api/books/999