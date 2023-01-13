from aiogram import executor
from controller import dp

executor.start_polling(dp, skip_updates=True)