# استفاده از تصویر رسمی Python
FROM python:3.9-slim

# تنظیم دایرکتوری کاری داخل کانتینر
WORKDIR /app

# کپی کردن فایل‌های پروژه به داخل کانتینر
COPY . /app

# نصب وابستگی‌ها
RUN pip install --no-cache-dir -r requirements.txt

# باز کردن پورت 5000 برای API
EXPOSE 5000

# اجرای برنامه
CMD ["python", "app.py"]
