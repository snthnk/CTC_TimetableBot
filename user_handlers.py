from aiogram import Router, F, Bot, types
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from datetime import datetime, timedelta
import excel_utils

router = Router()

@router.message(Command('timetable_today'))
async def process_timetable_command(message: Message):
    current_time = datetime.now()
    date = current_time.strftime("%d.%m.%Y")
    if not excel_utils.download_excel(date):
        
    excel_utils.find_schedule_for_group()
    await message.reply(f"Раписание на {date}")

@router.message(Command('timetable_tomorrow'))
async def show_today_timetable(message: Message):
    current_datetime = datetime.now()
    next_day = current_datetime + timedelta(days=1)
    date = next_day.strftime("%d.%m.%Y")
    excel_utils.download_excel(date)
    await message.reply(f"Расписание на {date}")


