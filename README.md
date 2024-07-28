# Error to ChatGPT

Công cụ này giúp bạn nhanh chóng gửi các thông báo lỗi từ terminal lên ChatGPT để nhận được sự trợ giúp.

## Tính năng

-   Sao chép thông báo lỗi từ terminal
-   Tự động mở ChatGPT với câu hỏi được điền sẵn
-   Hỗ trợ mở trong tab hiện tại hoặc tab mới
-   Hỗ trợ Windows (với WSL), macOS và các hệ điều hành dựa trên Unix

## Yêu cầu hệ thống

-   Python 3.6+
-   pip (trình quản lý gói của Python)
-   Git (để clone repository)

## Cài đặt

1. Clone repository này:

    ```
    git clone https://github.com/your-username/error-to-chatgpt.git
    cd error-to-chatgpt
    ```

2. Chạy script cài đặt:

    ```
    bash install.sh
    ```

3. Khởi động lại terminal của bạn hoặc chạy:
    ```
    source ~/.bashrc
    ```

## Sử dụng

1. Khi bạn gặp lỗi trong terminal, hãy sao chép (copy) đoạn thông báo lỗi.

2. Sử dụng một trong hai lệnh sau:

    - `eo`: Mở ChatGPT trong tab hiện tại (nếu đã mở) hoặc tab mới (nếu chưa mở)
    - `eoo`: Luôn mở ChatGPT trong một tab mới

3. Trình duyệt mặc định của bạn sẽ mở với ChatGPT, kèm theo câu hỏi được điền sẵn về lỗi của bạn.

## Xử lý sự cố

-   Nếu lệnh không hoạt động, hãy đảm bảo rằng bạn đã khởi động lại terminal hoặc chạy `source ~/.bashrc`.
-   Đối với người dùng WSL: Nếu trình duyệt không tự động mở, URL sẽ được sao chép vào clipboard. Bạn có thể mở trình duyệt Windows và dán URL vào.

## Đóng góp

Đóng góp luôn được chào đón! Vui lòng mở một issue hoặc tạo một pull request.

## Giấy phép

MIT License. Xem file [LICENSE](LICENSE) để biết thêm chi tiết.
