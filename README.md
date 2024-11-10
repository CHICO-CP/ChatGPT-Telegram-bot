# 🤖 ChatGPT Telegram Bot

This Telegram bot integrates ChatGPT's AI (using the Gemini API) to interact with users. It answers questions, provides assistance, handles commands, and stores queries for future analysis.

## 🚀 Features

- 🌟 Automatic responses to user queries.
- 💬 Available commands like `/start`, `/help`, `/info`, and `/privacy`.
- 🗃️ Handles queries and stores them in a database to improve service.
- 📲 Splits long responses into multiple messages if they exceed Telegram's character limit.

## 📋 Requirements

- Python 3.8 or higher
- Necessary libraries:
    ```bash
    pip install -r requirements.txt
    ```

- A Telegram Bot Token and OpenAI API Key (Gemini).

## 🛠️ Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/CHICO-CP/ChatGPT-Telegram-bot.git
    cd ChatGPT-Telegram-bot
    ```

2. Edit a `config.py` add your credentials:
    ```
    TELEGRAM_API_KEY=your_telegram_token
    ```
3. Edit a `openai_api` file add your api
    ```
    OPENAI_API_KEY=your_openai_api_key
    ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the bot:
    ```bash
    python run.py
    ```

## 📝 Commands

- `/start`: Starts the interaction with the bot.
- `/help`: Displays available commands.
- `/info`: Provides information about the bot’s capabilities and limitations.
- `/privacy`: Displays the bot's privacy policy.

## 🤝 Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

## 📜 License

This project is licensed under the MIT License.
