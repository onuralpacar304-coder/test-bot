import os
import time
from telegram import Bot

# Telegram bilgileri
TOKEN = "8383015523:AAGBJeuiPv25xrQHjhFlYS660NNSoxu-LCc"
CHAT_ID = "922463721"

bot = Bot(token=TOKEN)

# Test mesajı gönder
bot.send_message(chat_id=CHAT_ID, text="🤖 Test botu çalışıyor! ✅")

print("✅ Mesaj gönderildi!")

# 10 saniye bekle, sonra tekrar gönder
time.sleep(10)
bot.send_message(chat_id=CHAT_ID, text="10 saniye geçti, hala çalışıyorum! 🚀")

print("✅ İkinci mesaj gönderildi!")
