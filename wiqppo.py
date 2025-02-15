from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message,InlineKeyboardMarkup,InlineKeyboardButton, KeyboardButton
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from aiogram.utils.keyboard import ReplyKeyboardBuilder


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

@dp.message(Command('start'))
async def asd(message : Message):
    kb = [
        [
            KeyboardButton(text="С пюрешкой"),
            KeyboardButton(text="Без пюрешки")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбирите способ подачи"
    )


    await message.answer("Как подавать котлеты ?", reply_markup=keyboard)

@dp.message(F.text.lower() == "с пюрешкой")
async def with_puree(message: types.Message):
    await message.reply("Отличный выбор!")

@dp.message(F.text.lower() == "без пюрешки")
async def without_puree(message: types.Message):
    await message.reply("Так невкусно")

@dp.message(Command("reply_builder"))
async def reply_builder(message: Message):
    builder = ReplyKeyboardBuilder()
    for i in range(1, 17):
        builder.add(KeyboardButton(text=str(i)))
    builder.adjust(4)
    await message.answer(
        "Выбирите число:",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )

@dp.message(Command("special_buttons"))
async def cmd_special_buttons(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Запросить геолакацию", request_location=True),
        types.KeyboardButton(text="Запросить контакт", request_contact=True)
    )
    builder.row(
    types.KeyboardButton(
            text="Выбрать премиум пользователя",
            request_user=types.KeyboardButtonRequestUser(
                request_id=1,
                user_is_premium=True
            )
        ),
        types.KeyboardButton(
            text="Выбрать супергруппу с форумами",
            request_chat=types.KeyboardButtonRequestChat(
                  request_id=2,
                  chat_is_channel=False,
                  chat_is_forum=True
            )
        )
    )

    await message.answer(
         "Выбирите дейсвие:",
         reply_markup=builder.as_markup(resize_keyboard=True),
)

dp.include_router(router)


async def main():
    await bot.delete_webhook()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())








