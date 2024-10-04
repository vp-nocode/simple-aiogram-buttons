from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


main_kb = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Hello!"), KeyboardButton(text="Good bye!")]
], resize_keyboard=True)

inline_kb = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="News - China breaking", url='https://www.cgtn.com/')],
   [InlineKeyboardButton(text="Music - Billboard Hot 100", url='https://www.billboard.com/charts/hot-100/')],
   [InlineKeyboardButton(text="Video - Youtube trends", url='https://www.youtube.com/feed/trending')]
])

async def inline_kb_dynamic(button_set):
   keyboard = InlineKeyboardBuilder()
   for key in button_set:
       #button = InlineKeyboardButton(text=key, callback_data=MyCallbackData(action=key).pack())
      button = InlineKeyboardButton(text=key, callback_data=key)
      keyboard.add(button)
   return keyboard.adjust(2).as_markup()
