from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from imei_checker_bot.views import get_imei_view
from imei_checker_bot.states import ImeiForm


router = Router(name=__name__)


@router.message(Command(commands='help'))
async def help_command(message: Message) -> None:
    """Асинхронная функция для отправки сообщения со списком команд"""

    text = ('Меню help:\n\n'
        '/help - список доступных команд\n'
        '/info - информация о боте\n'
        '/check_imei - проверить imei устройства')
    await message.answer(text=text, parse_mode=None)


@router.message(Command(commands='info'))
async def info_command(message: Message) -> None:
    """Асинхронная функция для отправки сообщения информации о боте"""

    text = ('Бот IMEI-Checker info:\n\n'
        'Здесь вы можете проверить IMEI устройства.\n'
        'Для получения полного списка команд отправьте /help')
    await message.answer(text=text, parse_mode=None)


@router.message(Command(commands='check_imei'))
async def check_imei_command(message: Message, state: FSMContext) -> None:
    """Запрос у пользователя ввода IMEI и установка состояния"""
    
    await message.answer("Введите IMEI устройства:")
    await state.set_state(ImeiForm.IMEI)


@router.message(ImeiForm.IMEI, F.text.regexp(r'^\d{15}$'))
async def receive_imei(message: Message, state: FSMContext) -> None:
    """Обработчик для получения данных устройства по imei"""

    imei = message.text
    text = await get_imei_view(imei=imei)
    
    await message.answer(text=text, parse_mode=None)
    await state.clear()
