# Traffic Penalty Checker
Đây là bài tập lớn môn tự động hóa

## Features

Tự động kiêm tra phạt nguội vào lúc **6:00** sáng và **12:00** trưa hàng ngày

## Requirements

- `python-dotenv`
- `schedule`
- `pytesseract`
- `selenium`

## External Dependencies

**browser_driver**: 
- Với windows: tải tại: https://developer.chrome.com/docs/chromedriver/downloads
- Với linux (arch): `yay -S chromedriver`

**Tesseract OCR**
- Với windows: Tải tại https://github.com/UB-Mannheim/tesseract/wiki
- Với linux(arch): `sudo pacman -S tesseract`

## Installation

1.  Clone repo:
```bash
    git clone https://github.com/huyga1185/traffic-penalty-checker
```

2. Cài đặt thư viện

```bash
    pip install -r requirements.txt
```

3. Mở folder repo
```bash
    cd trafic-penalty-checker
```

## Usage

- Bước 1: clone repo và cài đặt lib cần thiết
- Bước 2: Tạo file **.env** có nội dung sau:

```bash
    #biển kiểm xoát
    bkx = 'biển kiểm xoát'
    #browser driver
    browser_driver = 'browser_driver_path'
    #loại xe cần kiểm tra
    # 0 với  oto, 1 với xe máy, 2 với xe đạp điện
    loai_xe = 0
```

- Bước 3: Khởi chạy
```bash
    python main.py
```
