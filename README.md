# Error to ChatGPT

Công cụ này cho phép bạn nhanh chóng gửi các thông báo lỗi hoặc bất kỳ nội dung nào từ clipboard đến ChatGPT với phần giới thiệu tùy chọn.

## Cài đặt

1. Clone repository này:

    ```bash
    git clone https://github.com/yourusername/error-to-chatgpt.git
    ```

2. Di chuyển đến thư mục đã clone:

    ```bash
    cd error-to-chatgpt
    ```

3. Chạy script cài đặt với quyền admin:

    - Yêu cầu máy đã có python (nếu không, bạn vui lòng lên trang chủ python để tải và cài đặt)
    - Nhấp chuột phải vào `install.bat`
    - Chọn "Run as administrator"

4. Khởi động lại command prompt để sử dụng các lệnh mới.

## Sử dụng

1. Sao chép văn bản bạn muốn gửi đến ChatGPT vào clipboard.
2. Mở command prompt và sử dụng một trong các lệnh sau:
    - `eo` để gửi nội dung clipboard đến ChatGPT dưới dạng thông báo lỗi.
    - `eo [phần giới thiệu tùy chọn]` để gửi nội dung clipboard với phần giới thiệu tùy chỉnh.
    - `eoo [nội dung truy vấn]` để gửi truy vấn tùy chỉnh trực tiếp mà không sử dụng clipboard.

### Ví dụ:

-   `eo` sẽ gửi `"Hãy giúp tôi sửa lỗi này: [nội dung clipboard]"` đến ChatGPT.
-   `eo là cái gì` sẽ gửi `"[nội dung clipboard] là cái gì"` đến ChatGPT.
-   `eoo lỗi này là gì` sẽ gửi `"lỗi này là gì"` trực tiếp mà không sử dụng clipboard.

Công cụ này sẽ tự động mở trình duyệt mặc định của bạn với truy vấn ChatGPT.

## Yêu cầu

-   Windows 10 hoặc mới hơn
-   Python 3.6 hoặc mới hơn
-   Kết nối internet (cho thiết lập ban đầu và sử dụng)

## Khắc phục sự cố

Nếu gặp vấn đề, hãy đảm bảo rằng:

-   Bạn đã chạy script cài đặt với quyền admin
-   Bạn đã khởi động lại command prompt sau khi cài đặt
-   Python và pyperclip đã được cài đặt đúng cách
-   Clipboard của bạn chứa nội dung bạn muốn gửi

Để được hỗ trợ thêm, vui lòng mở một issue trên repository GitHub này.

## Lưu ý

Công cụ này sử dụng nội dung clipboard làm phần chính của truy vấn, trừ khi bạn sử dụng lệnh `eoo`. Hãy chắc chắn rằng bạn đã sao chép văn bản mong muốn trước khi chạy lệnh.
