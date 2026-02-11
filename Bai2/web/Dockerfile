FROM python:3.10

# 1. Tạo thư mục làm việc trong container
WORKDIR /app

# 2. Copy requirements trước (để tận dụng cache)
COPY requirements.txt .

# 3. Cài thư viện
RUN python -m pip install --upgrade pip \
    && python -m pip install -r requirements.txt

# 4. Copy toàn bộ source code
COPY . .

# 5. Lệnh chạy app Flask
CMD ["python", "app.py"]
