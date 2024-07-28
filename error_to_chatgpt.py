import pyperclip
import urllib.parse
import subprocess
import platform
import sys

def create_chatgpt_url(error_text):
    base_url = "https://chat.openai.com/chat"
    query_params = urllib.parse.urlencode({"q": f"Hãy giúp tôi sửa lỗi này: {error_text}"})
    return f"{base_url}?{query_params}"

def open_browser(url, new_tab=False):
    system = platform.system()
    try:
        if system == "Windows":
            if new_tab:
                subprocess.run(["powershell.exe", "Start", f'"{url}"', "-WindowStyle", "Normal"], check=True)
            else:
                subprocess.run(["powershell.exe", "Start", f'"{url}"'], check=True)
        elif system == "Darwin":  # macOS
            if new_tab:
                subprocess.run(["open", "-na", "Google Chrome", "--args", "--new-tab", url], check=True)
            else:
                subprocess.run(["open", url], check=True)
        else:  # Linux và các hệ điều hành khác, bao gồm WSL
            if "microsoft-standard" in platform.uname().release:  # WSL detection
                if new_tab:
                    subprocess.run(["powershell.exe", "Start", f'"{url}"', "-WindowStyle", "Normal"], check=True)
                else:
                    subprocess.run(["powershell.exe", "Start", f'"{url}"'], check=True)
            else:
                if new_tab:
                    subprocess.run(["xdg-open", url], check=True)
                else:
                    subprocess.run(["xdg-open", url], check=True)
    except subprocess.CalledProcessError:
        print("Không thể mở trình duyệt tự động. URL đã được copy vào clipboard.")
        pyperclip.copy(url)
        print(f"URL: {url}")
        print("Vui lòng mở trình duyệt và dán URL này vào thanh địa chỉ.")

def send_to_chatgpt(new_tab=False):
    error_text = pyperclip.paste()
    url = create_chatgpt_url(error_text)
    open_browser(url, new_tab)

if __name__ == "__main__":
    command = sys.argv[0]
    if command.endswith("eoo"):
        send_to_chatgpt(new_tab=True)
    else:
        send_to_chatgpt(new_tab=False)
