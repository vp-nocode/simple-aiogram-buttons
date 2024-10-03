import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from config import TOKEN
import keyboards as kb


bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)

@dp.message(CommandStart())
async def start(message: Message):
    # await message.answer(f"Hi, {message.from_user.first_name} ({message.from_user.full_name}), I'm a bot!")
    await message.answer(text='Bot started!', reply_markup=kb.main_kb)
    # await message.answer(f"Hi, {message.from_user.first_name}, I'm a bot!", reply_markup=kb.inline_keyboard_test)
    # await message.answer(f"Hi, {message.from_user.first_name}, I'm a bot!", reply_markup=await kb.test_keyboard())

@dp.message(Command('help'))
async def command_help(message: Message):
    await message.answer("This bot can execute the commands:\n /start\n /help\n /link\n /dynamic")

@dp.message(Command('link'))
async def command_link(message: Message):
    await message.answer(text='Bot started!', reply_markup=kb.inline_kb)

@dp.message(Command('dynamic'))
async def command_dynamic(message: Message):
    button_set = ["Show more ..."]
    await message.answer('Dyn inline button!', reply_markup=await kb.inline_kb_dynamic(button_set))

@dp.callback_query(F.data == 'Show more ...')
async def show_more(callback: CallbackQuery):
    button_set = ['Option 1', 'Option 2']
    await callback.answer("news is loading", show_alert=True)
    await callback.message.edit_text('Breaking news!', reply_markup=await kb.inline_kb_dynamic(button_set))

@dp.callback_query(F.data == 'Option 1')
async def option1(callback: CallbackQuery):
    await callback.answer("Option 1 selected", show_alert=True)

@dp.callback_query(F.data == 'Option 2')
async def option2(callback: CallbackQuery):
    await callback.answer("Option 2 selected", show_alert=True)

@dp.message(F.text == "Hello!")
async def test_button(message: Message):
   await message.answer(f"Hi, {message.from_user.first_name}!")

@dp.message(F.text == "Good bye!")
async def test_button(message: Message):
   await message.answer(f"Good bye, {message.from_user.first_name}!")

@dp.message()
async def start(message: Message):
    await message.answer("Sorry, I didn't understand that command or message. Please try again.")


if __name__ == "__main__":
    asyncio.run(main())
