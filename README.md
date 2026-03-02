# 🚀 LAB 3 – DOCKER & DOCKER COMPOSE

Bài thực hành gồm 2 phần:

* 🧪 **Bài 1:** Iperf3 UDP với Docker Compose
* 🌐 **Bài 2:** Web Flask + PostgreSQL với Docker Compose

---

## 📌 YÊU CẦU

* Đã cài đặt **Docker**
* Đã cài đặt **Docker Compose**

---

## 🧪 BÀI 1 – IPERF3 UDP

### 🔎 1. Mô tả

Hệ thống gồm 3 container chạy trong cùng một Docker Network nội bộ:

| Container | Vai trò |
|-----------|---------|
| `node0` | Iperf3 UDP Server |
| `node1` | UDP Client – 10 Mbps |
| `node2` | UDP Client – 5 Mbps |

### ▶️ 2. Cách chạy

Mở terminal tại thư mục `Bai1`:
```bash
cd Bai1
docker compose up
```

### ✅ 3. Kết quả mong đợi

* Docker tạo network và 3 container
* `node1` đạt khoảng **10 Mbits/sec**
* `node2` đạt khoảng **5 Mbits/sec**
* Packet loss = **0%**
* Hai client hoạt động song song trên hai port khác nhau

### ⛔ 4. Dừng hệ thống
```bash
docker compose down
```

---

## 🌐 BÀI 2 – FLASK + POSTGRESQL

### 🔎 1. Mô tả

Hệ thống gồm 2 container giao tiếp qua Docker Network bằng tên service:

| Container | Vai trò |
|-----------|---------|
| `web` | Ứng dụng Flask |
| `postgres` | Cơ sở dữ liệu PostgreSQL |

### ▶️ 2. Cách chạy

Mở terminal tại thư mục `Bai2`:
```bash
cd Bai2
docker compose up --build
```

### 🌍 3. Truy cập hệ thống

Mở trình duyệt và truy cập:
```
http://localhost:8888
```

### 🧩 4. Chức năng

* Nhập nội dung vào form
* Nhấn **Submit** để lưu vào database
* Trang reload và hiển thị dữ liệu mới
* Reload lại trình duyệt dữ liệu vẫn còn do được lưu trong **PostgreSQL**

### ⛔ 5. Dừng hệ thống
```bash
docker compose down
```

> Xóa luôn database (volume):
```bash
docker compose down -v
```
