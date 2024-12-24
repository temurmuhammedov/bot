""" 
This is an echo bot. 
It echoes any incoming text messages. 
""" 
 
import logging 
import asyncio 
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from button import menu, inlne, part, dpart
from details import detail as dt

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
API_TOKEN = '7714613784:AAHAFhg1ov9F38QUcc0j2x2WdiUHuCUFARw' 
 
# Configure logging 
logging.basicConfig(level=logging.INFO) 
 
# Initialize bot 
bot = Bot(token=API_TOKEN) 
 


# Create Dispatcher 
dp = Dispatcher() 


menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='📝Film qisimlari', callback_data='uy' ),InlineKeyboardButton(text='📲Boglanish', callback_data='help')] 
] 
)

inlne = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Obuna bolish ⬅', callback_data='ob1', url="https://t.me/kunuzofficial")],
    [InlineKeyboardButton(text='Obuna bolish ⬅', callback_data='ob2', url="https://t.me/Xorazmtelefon_bozori_N1")],
    [InlineKeyboardButton(text='Obuna bolish ⬅', callback_data='ob3', url='https://t.me/mohirdev')],
    [InlineKeyboardButton(text='Tekshirish ✅', callback_data='tek')]
])

part = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Uyda yolgiz 1 🎬', callback_data='uy1'), InlineKeyboardButton(text='Uyda yolgiz 2 🎬', callback_data='uy2')],
    [InlineKeyboardButton(text='Uyda yolgiz 3 🎬', callback_data='uy3'), InlineKeyboardButton(text='Uyda yolgiz 4 🎬', callback_data='uy4')],
    [InlineKeyboardButton(text='Uyda yolgiz 5 🎬', callback_data='uy5')],
    [InlineKeyboardButton(text='Ortga 🛑', callback_data='back')]
]
)

dpart = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Uyda yolgiz 1 🎬', callback_data='uy1'), InlineKeyboardButton(text='Uyda yolgiz 2 🎬', callback_data='uy2')],
    [InlineKeyboardButton(text='Uyda yolgiz 3 🎬', callback_data='uy3'), InlineKeyboardButton(text='Uyda yolgiz 4 🎬', callback_data='uy4')],
    [InlineKeyboardButton(text='Uyda yolgiz 5 🎬', callback_data='uy5')]
]
)




@dp.message(Command(commands=["start"])) 
async def send_welcome(message: Message): 
    await message.reply(f"Salom {message.from_user.first_name} \nBotga hush kelibsiz bu bot uyda yolgiz ishqibozlari uchun", reply_markup=inlne) 

# @dp.message(Command(commands=["film"])) 
# async def send_btn(message: Message): 
#     await message.answer('film', reply_markup=menu) 


@dp.callback_query(F.data == 'uy')
async def film(callback: CallbackQuery):
    await callback.message.edit_text('Film qismini tanlang' , reply_markup=part)
    await callback.answer('')
    
@dp.callback_query(F.data == 'uy1')
async def film(callback: CallbackQuery):
    await callback.message.answer_video(video='https://t.me/Uyda_Yolgizy/583', caption='Uyda yolgiz 1-qism', reply_markup=dpart)
    await callback.answer('')

@dp.callback_query(F.data == 'uy2')
async def film(callback: CallbackQuery):
    await callback.message.answer_video(video='https://t.me/Uyda_Yolgizy/584', caption='Uyda yolgiz 2-qism', reply_markup=dpart)
    await callback.answer('')


@dp.callback_query(F.data == 'uy3')

async def film(callback: CallbackQuery):
    await callback.message.answer_video(video='https://t.me/Uyda_Yolgizy/585', caption='Uyda yolgiz 3-qism', reply_markup=dpart)
    await callback.answer('')

@dp.callback_query(F.data == 'uy4')
async def film(callback: CallbackQuery):
    await callback.message.answer_video(video='https://t.me/Uyda_Yolgizy/586', caption='Uyda yolgiz 4-qism', reply_markup=dpart)
    await callback.answer('')


@dp.callback_query(F.data == 'uy5')
async def film(callback: CallbackQuery):
    await callback.message.answer_video(video='https://t.me/Uyda_Yolgizy/587', caption='Uyda yolgiz 5-qism', reply_markup=dpart)
    await callback.answer('')



@dp.callback_query(F.data == 'tek')
async def check(callback: CallbackQuery):
    await callback.message.edit_text('obuna bolish muvaffqiyatli amalga oshdi', reply_markup=menu )

@dp.callback_query(F.data == 'back')
async def back(callback: CallbackQuery):
    await callback.message.edit_text('film', reply_markup=menu)


@dp.callback_query(F.data == 'help')
async def send_help(callback: CallbackQuery):
    await callback.message.answer('@t1mur4ik_008')
 
@dp.message(Command(commands=["help"])) 
async def help_users(message: Message): 
    await message.reply("Sizga qanday yordam kerak?")

# @dp.message() 
# async def echo(message: Message): 
#     await message.answer(message.text) 
 
 
async def main(): 
    await dp.start_polling(bot) 
 
 
if __name__ == "__main__": 
    asyncio.run(main())
