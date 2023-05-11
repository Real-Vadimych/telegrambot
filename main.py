from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from dbwork import inserttodb, selectfromdb
from settings import BOT_TOKEN, logger

storage = MemoryStorage()
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
logger.info("Bot has started")

@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):
	logger.info(f"/start command was invoked by {message.from_user.username}")
	await message.answer(
		"Hi! I'm your note saver :)\n" "Commands:\n" "/new_note\n" "/get_notes"
	)

if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)
