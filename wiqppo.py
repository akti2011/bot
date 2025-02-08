from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message,InlineKeyboardMarkup,InlineKeyboardButton
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

BOT_API_TOKEN ='8094884508:AAE-nrIvIz5JBzVgXx6p-evXAkkuBpzXElM'
bot = Bot(token=BOT_API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
router = Router()

@router.message(Command("start"))
async def cmd_start_2(message: Message):
    await message.answer('Запуск сообщения по команде /start_2 используя фильтр CommandStart()')

@router.message(Command('catalog'))
async def catalog_com(message:Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Каталог товаров ", callback_data="catalog")],
        [InlineKeyboardButton(text="партнерство ", callback_data="reviews")],
        [InlineKeyboardButton(text="Часто задаваемые вопросы ", callback_data="materials")],
        [InlineKeyboardButton(text="Связаться с нами ", callback_data="contact")],
    ])
    await message.answer( 'dadddsd', reply_markup=keyboard)

@router.callback_query(lambda c: c.data in ['contact'])
async def handle_callback_query(callback_query: types.CallbackQuery):
    data = callback_query.data
    if data =='contact':
        await callback_query.message.answer('sssss')

@router.message(text='hi')
async def asd(message : Message):
    await message.answer('sdads')


dp.include_router(router)


async def main():
    await bot.delete_webhook()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())





