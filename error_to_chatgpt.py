import pyperclip
import urllib.parse
import subprocess
import platform
import sys

def create_chatgpt_url(query):
    base_url = "https://chat.openai.com/chat"
    query_params = urllib.parse.urlencode({"q": query})
    return f"{base_url}?{query_params}"

def open_browser(url):
    system = platform.system()
    try:
        if system == "Windows":
            subprocess.run(["powershell.exe", "Start", f'"{url}"'], check=True)
        elif system == "Darwin":  # macOS
            subprocess.run(["open", url], check=True)
        else:  # Linux and other operating systems
            subprocess.run(["xdg-open", url], check=True)
    except subprocess.CalledProcessError:
        print("Không thể mở trình duyệt tự động. URL đã được copy vào clipboard.")
        pyperclip.copy(url)
        print(f"URL: {url}")
        print("Vui lòng mở trình duyệt và dán URL này vào thanh địa chỉ.")

def send_to_chatgpt(custom_intro=None):
    clipboard_content = pyperclip.paste()
    
    if custom_intro:
        query = f"{clipboard_content} {custom_intro}"
    else:
        query = f"Hãy giúp tôi sửa lỗi này: {clipboard_content}"
    
    url = create_chatgpt_url(query)
    open_browser(url)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        custom_intro = " ".join(sys.argv[1:])
        send_to_chatgpt(custom_intro)
    else:
        send_to_chatgpt()