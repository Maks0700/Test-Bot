from aiogram import executor,Bot,Dispatcher,types
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton
from Api import api
import random

bot=Bot(api)
dp=Dispatcher(bot)

async def on_start(_):
    print("Success!!!")

arr_photo=["city.jpg","nature.jpg","pets.jpg"]



@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    await message.answer("Hello my friend!")


@dp.message_handler(commands=["photo"])
async def send_photo(message:types.Message):
    bot.send_photo(message.from_user.id,random.choice(arr_photo))







if __name__=="__main__":
    executor.start_polling(dp,on_startup=on_start,skip_updates=True)
