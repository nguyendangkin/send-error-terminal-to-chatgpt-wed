import pyperclip
import urllib.parse
import subprocess
import platform

def send_to_chatgpt():
    # Lấy text được bôi đen từ clipboard
    error_text = pyperclip.paste()
    
    # Tạo URL cho ChatGPT với error_text
    base_url = "https://chat.openai.com/chat"
    query_params = urllib.parse.urlencode({"q": f"Hãy giúp tôi sửa lỗi này: {error_text}"})
    url = f"{base_url}?{query_params}"
    
    # Mở trình duyệt dựa trên hệ điều hành
    system = platform.system()
    try:
        if system == "Windows":
            subprocess.run(["powershell.exe", "Start", f'"{url}"'], check=True)
        elif system == "Darwin":  # macOS
            subprocess.run(["open", url], check=True)
        else:  # Linux và các hệ điều hành khác
            subprocess.run(["xdg-open", url], check=True)
    except subprocess.CalledProcessError:
        print("Không thể mở trình duyệt tự động. URL đã được copy vào clipboard.")
        pyperclip.copy(url)
        print(f"URL: {url}")
        print("Vui lòng mở trình duyệt và dán URL này vào thanh địa chỉ.")

if __name__ == "__main__":
    send_to_chatgpt()
