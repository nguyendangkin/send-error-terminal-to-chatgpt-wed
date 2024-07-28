#!/bin/bash

# Cài đặt các dependency
pip install pyperclip

# Tạo thư mục bin nếu chưa tồn tại
mkdir -p ~/bin

# Copy script chính vào thư mục bin
cp error_to_chatgpt.py ~/bin/error_to_chatgpt.py

# Tạo alias trong .bashrc
echo "alias eo='python3 ~/bin/error_to_chatgpt.py eo'" >> ~/.bashrc
echo "alias eoo='python3 ~/bin/error_to_chatgpt.py eoo'" >> ~/.bashrc
echo "alias eo='python3 ~/bin/error_to_chatgpt.py eo' && alias eoo='python3 ~/bin/error_to_chatgpt.py eoo'" >> ~/.zshrc


echo "Cài đặt hoàn tất. Vui lòng khởi động lại terminal hoặc chạy 'source ~/.bashrc' để áp dụng thay đổi."