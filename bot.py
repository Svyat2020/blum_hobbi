import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота, который вы получили от BotFather
API_TOKEN = '7437889063:AAGakOxzoGBnBON2gSYfzseRUurV5MTcfP0'
WEB_APP_URL = 'https://Svyat2020.github.io/blum_hobbi/index.html'  # Ссылка на вашу игру (URL после публикации)

logging.basicConfig(level=logging.INFO)

bot = Bot(token=7437889063:AAGakOxzoGBnBON2gSYfzseRUurV5MTcfP0)
dp = Dispatcher(bot)

# Команда /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Нажми на кнопку ниже, чтобы начать зарабатывать Blum монеты!", reply_markup=types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton("Играть", web_app=types.WebAppInfo(url=https://Svyat2020.github.io/blum_hobbi/index.html))
    )
  )

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)