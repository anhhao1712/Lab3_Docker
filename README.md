LAB 3 – DOCKER & DOCKER COMPOSE

Bài thực hành gồm 2 phần:

Bài 1: Iperf3 UDP với Docker Compose

Bài 2: Web Flask + PostgreSQL với Docker Compose

Yêu cầu: Máy đã cài Docker và Docker Compose.

BÀI 1 – IPERF3 UDP
Mô tả

Hệ thống gồm 3 container:

node0: Iperf3 UDP Server

node1: UDP Client (10 Mbps)

node2: UDP Client (5 Mbps)

Các container chạy trong cùng Docker network nội bộ.

Cách chạy

Mở terminal tại thư mục Bai1:

cd Bai1
docker compose up
Kết quả mong đợi

Docker tạo network và 3 container.

node1 đạt khoảng 10 Mbits/sec.

node2 đạt khoảng 5 Mbits/sec.

Packet loss = 0%.

Hai client chạy song song trên hai port khác nhau.

Dừng hệ thống:

docker compose down
BÀI 2 – FLASK + POSTGRESQL
Mô tả

Hệ thống gồm:

web: Ứng dụng Flask

postgres: Cơ sở dữ liệu PostgreSQL

Hai container chạy trong cùng Docker network và giao tiếp nội bộ bằng tên service.

Cách chạy

Mở terminal tại thư mục Bai2:

cd Bai2
docker compose up --build

Lần đầu chạy sẽ build image từ Dockerfile.

Truy cập hệ thống

Mở trình duyệt và truy cập:

http://localhost:8888
Chức năng

Nhập nội dung vào form.

Nhấn Submit để lưu vào database.

Trang reload và hiển thị dữ liệu vừa thêm.

Reload lại trình duyệt dữ liệu vẫn còn do được lưu trong PostgreSQL.

Dừng hệ thống
docker compose down

Nếu muốn xóa luôn database:

docker compose down -v
