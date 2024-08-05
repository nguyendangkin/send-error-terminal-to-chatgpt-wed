# Error to ChatGPT

This tool allows you to quickly send error messages or any clipboard content to ChatGPT with optional custom introductions.

## Installation

1. Clone this repository:

    ```
    git clone https://github.com/yourusername/error-to-chatgpt.git
    ```

2. Navigate to the cloned directory:

    ```
    cd error-to-chatgpt
    ```

3. Run the install script with administrator privileges:

    - Right-click on `install.bat`
    - Select "Run as administrator"

4. Restart your command prompt to use the new commands.

## Usage

1. Copy the text you want to send to ChatGPT to your clipboard.
2. Open a command prompt and use one of the following commands:
    - `eo` to send the clipboard content to ChatGPT as an error message
    - `eo [custom introduction]` to send the clipboard content with a custom introduction

Examples:

-   `eo` will send "Hãy giúp tôi sửa lỗi này: [clipboard content]" to ChatGPT
-   `eo là cái gì` will send "[clipboard content] là cái gì" to ChatGPT

The tool will automatically open your default web browser with the ChatGPT query.

## Requirements

-   Windows 10 or later
-   Python 3.6 or later
-   Internet connection (for initial setup and usage)

## Troubleshooting

If you encounter any issues, please ensure that:

-   You ran the install script with administrator privileges
-   You've restarted your command prompt after installation
-   Python and pyperclip are correctly installed
-   Your clipboard contains the text you want to send

For further assistance, please open an issue on this GitHub repository.

## Note

This tool uses the clipboard content as the main part of the query. Make sure you've copied the desired text before running the command.
