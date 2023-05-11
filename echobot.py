
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

from settings import BOT_TOKEN

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Handler for messages (echo)
@dp.message_handler()
async def echo(message: types.Message):
    text = message.text
    await message.answer(f'*You said:* {text}', parse_mode=ParseMode.MARKDOWN)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)