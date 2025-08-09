import telebot
import requests
import os

TOKEN = os.environ.get("BOT_TOKEN")
MY_ID = 72192114359  # فقط برای شهابین

bot = telebot.TeleBot(TOKEN)

def ask_ai(question):
    try:
        url = "https://huggingface-api-bot-phi.vercel.app/ask"
        response = requests.post(url, json={"question": question}, timeout=20)
        if response.status_code == 200:
            return response.json().get("answer", "پاسخی پیدا نشد.")
        else:
            return "خطا: API پاسخ نداد."
    except Exception as e:
        return f"خطا: {e}"

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.from_user.id == MY_ID:
        bot.reply_to(message, ask_ai(message.text))

bot.polling()
